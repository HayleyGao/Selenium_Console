import time
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.notificationPage import notificationPage


class notificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #添加options的目的是为了解决https多出来的页面问题。
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.maximize_window()
        cls.url = ReadConfig().getOptionValue('environment', 'url')  # 变成类范围的变量。
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(3)
        logger().debug('driver is setup.')

    def test_01(self):
        account = ReadConfig().getOptionValue('test_account01', 'account')
        password = ReadConfig().getOptionValue('test_account01', 'password')
        lo = loginPage(self.driver)
        lo.loginIn(account, password)
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/passport/login'
        self.assertEqual(self.driver.current_url, url_)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/dashboard'
        self.assertEqual(self.driver.current_url, url_)


    def test_03(self):
        """
        通知设置,设置成功。
        :return:
        """
        notification = notificationPage(self.driver)
        time.sleep(3)
        server_address="smtp.mxhichina.com"
        server_port="465"
        sender_account="notice@datagrand.com"
        sender_pwd="DAguan123."
        notification.notification_menu(server_address,server_port,sender_account,sender_pwd)
        message_content_text=notification.getDivMessageBox()
        self.assertEqual("设置成功", message_content_text)

    def wtest_04(self):
        """
        通知设置,邮箱信息，异常。
        :return:
        """
        notification = notificationPage(self.driver)
        time.sleep(3)
        server_address=""
        server_port="465"
        sender_account="notice@datagrand.com"
        sender_pwd="DAguan123."
        notification.notification_menu(server_address,server_port,sender_account,sender_pwd)
        message_content_text=notification.getDivMessageBox()
        self.assertEqual("请将信息填写完整", message_content_text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
