import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class notificationPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def notification_menu_btn(self):
        """
        点击进入通知设置模块
        :return:
        """
        notification_menu_btn = self.driver.find_element(By.XPATH,
                                                         "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div["
                                                         "2]/ul/li[7]")
        return notification_menu_btn

    def notification_panel(self):
        """
        通知设置表单
        :return:
        """

        # 进入通知设置界面
        # 1.1 勾选“通知内容”
        checkboxs_notice_content = self.driver.find_elements(By.XPATH,
                                                             "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[1]/nz-form-control/div/div/nz-checkbox-group/label/span/input")
        # print(len(checkboxs))
        for x in checkboxs_notice_content:
            if x.is_selected() == True:
                pass
            else:
                x.click()
        time.sleep(2)
        # 1.2 勾选“通知类型”
        checkboxs_notice_type = self.driver.find_elements(By.XPATH,
                                                          "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[2]/nz-form-control/div/div/nz-checkbox-wrapper/div/div/label/span/input")

        for y in checkboxs_notice_type:
            if y.is_selected() == True:
                pass
            else:
                y.click()
        time.sleep(2)
        # 填写“每天通知时间”
        hours = self.driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[2]/nz-form-control/div/div/nz-checkbox-wrapper/div/div[2]/input[1]')
        seconds = self.driver.find_element(By.XPATH,
                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[2]/nz-form-control/div/div/nz-checkbox-wrapper/div/div[2]/input[2]')
        hours.clear()
        seconds.clear()
        time.sleep(1)
        hours.send_keys("12")
        time.sleep(1)
        seconds.send_keys("30")
        time.sleep(1)

    def notification_mail(self):
        """
        填写邮箱信息区域
        :return:
        """
        # server_domain
        print("start fill email information.")
        email_address = self.driver.find_element(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[3]/nz-form-control/div/div/div/div/input')
        email_address.clear()
        email_address.send_keys("smtp.mxhichina.com")
        time.sleep(1)
        email_port = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[4]/nz-form-control/div/div/div/div/nz-input-number/div[2]/input')
        time.sleep(1)

        if email_port.get_attribute("value") == "465":
            pass
        else:
            email_port.clear()
            email_port.send_keys("465")  # 端口这里的输入框是属于复合输入框。

        time.sleep(1)
        email_sender = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[5]/nz-form-control/div/div/div/div/input')
        email_sender.clear()
        email_sender.send_keys("notice@datagrand.com")
        time.sleep(1)
        email_sender_pwd = self.driver.find_element(By.XPATH,
                                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[6]/nz-form-control/div/div/div/div/nz-input-group/input")
        email_sender_pwd.clear()
        email_sender_pwd.send_keys("DAguan123.")
        time.sleep(1)

    def notification_sumbitBtn(self):
        """
        提交按钮和确认框
        :return:
        """
        notification_sumbitBtn = self.driver.find_element(By.XPATH,
                                                          "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/div/button")
        notification_sumbitBtn.send_keys(Keys.ENTER)
        time.sleep(3)
        # 可能会弹出确认对话框
        confirm_btn = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
        confirm_btn.click()  # 这里点击了“确定按钮”
        time.sleep(3)


    def notification_menu(self):
        """
        通知设置
        :return:
        """
        self.notification_menu_btn().click()
        time.sleep(3)
        # 进入通知设置界面
        self.notification_panel()
        self.notification_mail()
        self.notification_sumbitBtn()

    def getToast(self):
        pass

    def getDivMessageBox(self):
        """
        div弹窗，类似toast的弹窗。
        :return:
        """
        #元素位置
        message_content_locator=(By.XPATH,'/html/body/div[2]/div/div/nz-message-container/div/nz-message/div/div/div/span')
        #显式等待获取元素
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(message_content_locator))
        #获取toast
        message_content_text=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/nz-message-container/div/nz-message/div/div/div/span').get_attribute("innerText")
        print(message_content_text)
        return  message_content_text
