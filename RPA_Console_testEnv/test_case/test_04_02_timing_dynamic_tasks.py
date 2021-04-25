import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.taskPage import tasksPage

from RPA_Console_testEnv.common.readExcel import readExcel
from RPA_Console_testEnv.common.readConfig import  ReadConfig
from RPA_Console_testEnv.common.log import logger
import math,time


class task_timing_dynamic_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
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
        # http://rpa-test.datagrand.com/#/passport/login
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/passport/login'
        self.assertEqual(self.driver.current_url, url_)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/dashboard'
        self.assertEqual(self.driver.current_url, url_)


    def test_03(self):
        task_page = tasksPage(self.driver)
        task_name_str = 'task_' + str(math.ceil(time.time())) + '_dynamicAllocation'
        task_page.addTask_byTiming_dynamicAllocation_Every(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    def test_04(self):
        task_page = tasksPage(self.driver)
        task_name_str = 'task_' + str(math.ceil(time.time())) + '_dynamicAllocation'
        task_page.addTask_byTiming_dynamicAllocation_Daily(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    def test_05(self):
        task_page = tasksPage(self.driver)
        task_name_str = 'task_' + str(math.ceil(time.time())) + '_dynamicAllocation'

        task_page.addTask_byTiming_dynamicAllocation_Weekly(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    def test_06(self):
        task_page = tasksPage(self.driver)
        task_name_str = 'task_' + str(math.ceil(time.time())) + '_dynamicAllocation'

        task_page.addTask_byTiming_dynamicAllocation_Monthly(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    def test_07(self):
        task_page = tasksPage(self.driver)
        task_name_str = 'task_' + str(math.ceil(time.time())) + '_dynamicAllocation'
        task_page.addTask_byTiming_dynamicAllocation_Once(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
