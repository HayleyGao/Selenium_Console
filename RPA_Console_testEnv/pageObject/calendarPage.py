import math
import os
import time

import win32con
import win32gui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class calendarPage:
    def __init__(self, driver):
        self.driver = driver

    def calendar_list(self):
        """
        进入“日历管理”列表
        :return:
        """
        time.sleep(2)
        calendar_menu_btn = self.driver.find_element(By.XPATH,
                                                     "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[6]")
                                                    #"/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[6]"
        calendar_menu_btn.click()
        time.sleep(3)

    def add_calendar_btn(self):
        """
         点击“新建日历”按钮
        :return:
        """
        add_calendar_btn = self.driver.find_element(By.XPATH,
                                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/shared-list-search/div/div/div[1]/button")
        return add_calendar_btn

    def calendarName(self):
        """
        新建日历对象的名称
        :return:
        """
        calendarName = self.driver.find_element(By.XPATH,
                                                "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[1]/form/nz-form-item/nz-form-control/div/div/input")
        return calendarName

    def calendar_template_downlink(self):
        """
        点击上传文件的链接
        :return:
        """
        # 点击下载模板的链接
        calendar_template_download = self.driver.find_element(By.XPATH,
                                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[2]/p[2]')
        return calendar_template_download

    def calendarfile_uplink(self):
        """
        点击上传文件的链接
        :return:
        """
        calendarfile_uplink = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[2]/p[1]/nz-upload/div/div/p')
        return calendarfile_uplink

    def calendarfile_upload_operation(self, calendarfile_path):
        """
        日历模块，上传文件的操作。
        （这个操作，和批量上传用户的操作是一致的，只是上传文件的路径不同）
        :param path:
        :return:
        """
        # calendarfile_path = r"C:\download\RPA10.0\Calendar template_20201110.csv"
        # 由于弹出了上传的对话框，所以，用pywin32解决.
        # 1.找窗口，获取窗口的句柄、文本、Class类型等方式。
        dialog_upload = win32gui.FindWindow("#32770", '打开')  # 32770是ClassName。
        print('dialog_upload', dialog_upload)
        # 2.输入本地文件的绝对路径，点击“打开”按钮
        # 找元素
        # 寻找子窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog_upload, 0, 'ComboBoxEx32', None)
        # print('ComboBoxEx32',ComboBoxEx32)
        combox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # print('combox',combox)
        edit = win32gui.FindWindowEx(combox, 0, 'Edit', None);  # 找到编辑框,这里返回的都是句柄。
        # print(edit)
        button = win32gui.FindWindowEx(dialog_upload, 0, 'Button', '打开(&O)');  # 找到“点击”按钮
        # print(button)

        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, calendarfile_path)  # 输入文件路径
        win32gui.SendMessage(dialog_upload, win32con.WM_COMMAND, 1, button)  # 点击”打开“按钮
        time.sleep(2)
        # 执行到此处为上传成功

    def show_all_selected_Btn(self):
        """
        点击“已选中”，下拉展开所有已选中的日期选项
        :return:
        """
        show_all_selected_btn = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[4]/p/span[2]')
        return show_all_selected_btn

    def save_btn(self):
        """
        保存按钮
        :return:
        """
        save_btn = self.driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/footer/div[2]/button[2]')
        return save_btn

    def add_calendar(self):
        """
        添加日历操作，手动添加。
        :return:
        """
        self.add_calendar_btn().click()
        time.sleep(1)
        # 日历名称
        self.calendarName().clear()
        # 先用时间戳进行连接吧。
        calendarName_str = "calendar_" + str(math.ceil(time.time()))
        self.calendarName().send_keys(calendarName_str)
        time.sleep(1)

        # 进行手动点击操作
        pass

        self.show_all_selected_Btn().click()
        time.sleep(1)

        self.save_btn().click()
        time.sleep(1)

    def add_calendar_by_upCalendarfile(self, calendarfile_path):
        """
        添加日历操作
        :return:
        """
        self.add_calendar_btn().click()
        time.sleep(1)
        # 日历名称
        self.calendarName().clear()
        # 先用时间戳进行连接吧。
        calendarName_str = "calendar_" + str(math.ceil(time.time()))
        self.calendarName().send_keys(calendarName_str)
        time.sleep(1)

        self.calendar_template_downlink().click()
        time.sleep(2)

        self.calendarfile_uplink().click()
        time.sleep(2)

        self.calendarfile_upload_operation(calendarfile_path)
        time.sleep(1)

        self.show_all_selected_Btn().click()
        time.sleep(1)

        self.save_btn().click()
        time.sleep(1)

    def add_calendar_downloadTemplate(self):
        """
        添加日历操作
        :return:
        """
        self.add_calendar_btn().click()
        time.sleep(1)
        # 日历名称
        self.calendarName().clear()
        # 先用时间戳进行连接吧。
        calendarName_str = "calendar_" + str(math.ceil(time.time()))
        self.calendarName().send_keys(calendarName_str)
        time.sleep(1)

        self.calendar_template_downlink().click()
        time.sleep(2)

    def isDownload(self, console_download_path):
        """
        判断日历模板下载是否成功
        :return:
        """
        # 浏览器下载文件夹的地址：
        download_list = os.listdir(console_download_path)
        print(len(download_list))
        return len(download_list)

    def isCalendarListEmpty(self):
        """
        判断日历列表是否为空
        需要除去第一行标题行。
        :return:
        """
        #len==1的时候分为2中情况：1、空态图显示占据了一个tr 2、正常的数据显示占据了一行。
        calendar_list = self.driver.find_elements(By.XPATH,
                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        print('calendar_list length:', len(calendar_list))


        if len(calendar_list) == 1:
            try:
                #空态图
                empty_graph_locator=(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr/td/nz-embed-empty/nz-empty/p')
                empty_graph=WebDriverWait(self.driver,5).until(EC.presence_of_element_located(empty_graph_locator))
                #empty_graph_text=empty_graph.get_attribute("innerText")
                return True
            except:
                return False
        else:
            return False

    def calendar_delete(self):
        if not self.isCalendarListEmpty():
            # 获取第一项的删除地址
            calendar_delete_btn = self.driver.find_element(By.XPATH,
                                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[5]/shared-actions/shared-action-item[2]/span[2]/a')
            calendar_delete_btn.click()
            time.sleep(2)
            # 弹出确认框,点击“确认”
            delete_confirmBtn = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
            delete_confirmBtn.click()
            time.sleep(2)
        else:
            print("no carlendar be delete.")
            return None

    def getFirstRecordName(self):
        """
        判断列表第一项的名称
        (新增、删除，都可以使用这个方法进行断言。)
        :return:
        """
        if self.isCalendarListEmpty()==True:
            return None
        else:
            carlendar_first_record = self.driver.find_element(By.XPATH,
                                                              "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr/td[1]/shared-ellipsis/div")

            carlendar_first_record_name = carlendar_first_record.get_attribute("innerText")
            print('carlendar_first_record_name', carlendar_first_record_name)
            return carlendar_first_record_name
