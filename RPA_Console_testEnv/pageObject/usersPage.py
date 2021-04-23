import random
import time

import win32con
import win32gui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class usersPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def account_menu(self):
        # 进入“用户管理”
        time.sleep(1)
        account_menu_btn = self.driver.find_element(By.XPATH,
                                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[4]")
        account_menu_btn.click()
        time.sleep(2)
        # 新增用户
        add_account_btn = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-user-list/section/div[1]/div/button')
        add_account_btn.click()
        time.sleep(5)
        # 登录账号
        # 总是容易异常的这里加个异常处理吧
        try:
            login_account = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/div/input")
            # login_account=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/div/input')
        except Exception:
            raise
        account_str = 'account_test' + str(random.randrange(1, 65535))
        account_email = account_str + '@' + 'datagrand_test.com'
        login_account.clear()
        login_account.send_keys(account_email)  # 此处当前设置为免激活模式
        time.sleep(1)
        # 用户名#
        account_name = self.driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/div/input')
        account_name.send_keys(account_str)
        time.sleep(1)
        '''
        #角色权限,需要匹配到“租户管理员”选项。
        role_authorities=self.driver.find_elements(By.XPATH,'/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/div/div/span[1]/label/span[1]/input')
        for x in role_authorities:
            print('x.value:',x.get_attribute("value"))
            if x.get_attribute("value")=='租户管理员':
                if  x.is_selected()==True:
                    pass
                else:
                    x.click()
                    time.sleep(1)
        time.sleep(2)
        '''

        account_submit_btn = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
        account_submit_btn.click()
        time.sleep(3)
        # 点击确定按钮"密码为123456"的对话框。
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button').click()
        time.sleep(3)

        # 用户批量导入
        account_batchImportBtn = self.driver.find_element(By.XPATH,
                                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-user-list/section/div[1]/div/nz-upload/div/div/button')
        account_batchImportBtn.click()
        time.sleep(2)
        # 弹出window文件路径窗口，和上传日历的处理方式是一样的。

        account_batchImport_path = r"C:\download\RPA10.0\batch_import_users.xlsx"
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

        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, account_batchImport_path)  # 输入文件路径
        time.sleep(1)
        win32gui.SendMessage(dialog_upload, win32con.WM_COMMAND, 1, button)  # 点击”打开“按钮
        time.sleep(3)

        # 点击对话框的确定按钮
        account_batchImport_ConfirmBtn = self.driver.find_element(By.XPATH,
                                                                  '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div/section/div[3]/button')
        account_batchImport_ConfirmBtn.click()
        time.sleep(3)

        # 用户管理的搜索框
        account_searchBox = self.driver.find_element(By.XPATH,
                                                     "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-user-list/section/div[1]/nz-input-group/input")
        account_searchBox.click()
        account_searchBox.send_keys("account")
        time.sleep(1)
        account_searchBox.send_keys(Keys.ENTER)
        time.sleep(3)
