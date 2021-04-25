import unittest

from RPA_Console_testEnv.common.readExcel import readExcel
from RPA_Console_testEnv.common.readConfig import  ReadConfig
from RPA_Console_testEnv.common.log import logger


from selenium.webdriver import Chrome

from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.taskPage import tasksPage
import math,time
#task_name_str = readExcel()[1]


class task_manual_Test(unittest.TestCase):

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
        #task_name_str='task_manual_demo0421_0001'
        task_name_str = 'task_' + str(math.ceil(time.time())) + 'manual'
        task_page.addTask_byManual(task_name_str)
        task_name_latest = task_page.getLatestTask()
        self.assertEqual(task_name_str, task_name_latest, '新建任务失败。')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger().debug('driver is setup.')


if __name__ == "__main__":
    unittest.main()
