import time
import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.calendarPage import calendarPage
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from selenium import webdriver


class calendarTest(unittest.TestCase):

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
        self.assertEqual(self.driver.current_url, url_)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/dashboard'
        self.assertEqual(self.driver.current_url, url_)

    def test_03(self):
        """
        上传本地的日历文件
        :return:
        """
        calendar = calendarPage(self.driver)
        time.sleep(3)
        calendar.calendar_list()
        calendarfile_path = ReadConfig().getOptionValue('calendar', 'calendarfile_path')
        carlendar_first_name_before = calendar.getFirstRecordName()
        calendar.add_calendar_by_upCalendarfile(calendarfile_path)
        carlendar_first_name_after = calendar.getFirstRecordName()
        self.assertNotEqual(carlendar_first_name_before, carlendar_first_name_after)

    def test_04(self):
        """
        判断，日历模板，是否下载成功。
        :return:
        """
        calendar = calendarPage(self.driver)
        time.sleep(3)
        calendar.calendar_list()
        console_download_path = ReadConfig().getOptionValue('console_download_path', 'console_download_path')
        templateDownload_brfore = calendar.isDownload(console_download_path)
        calendar.add_calendar_downloadTemplate()
        templateDownload_after = calendar.isDownload(console_download_path)
        self.assertEqual(templateDownload_after, templateDownload_brfore + 1)

    def wtest_05(self):
        """
        判断是否删除成功。
        :return:
        """
        calendar = calendarPage(self.driver)
        calendar.calendar_list()
        time.sleep(3)
        carlendar_first_name_before = calendar.getFirstRecordName()
        calendar.calendar_delete()
        carlendar_first_name_after = calendar.getFirstRecordName()
        self.assertNotEqual(carlendar_first_name_before, carlendar_first_name_after)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
