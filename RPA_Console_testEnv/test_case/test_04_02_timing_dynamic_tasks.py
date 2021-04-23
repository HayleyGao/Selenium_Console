import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.taskPage import tasksPage


class calendarTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://rpa-test.datagrand.com")
        cls.driver.implicitly_wait(3)

    def test_01(self):
        account = "gaoxiaoyan@datagrand.com"
        pwd_testEnv = 'Gaoxiaoyan9533'
        lo = loginPage(self.driver)  # 这里构造函数设置了driver参数，其余的方法便无须重复继承。
        lo.loginIn(account, pwd_testEnv)  # 这里，loginPage中的方法便无须重复继承。
        self.driver.implicitly_wait(3)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        self.assertEqual(self.driver.current_url, 'http://rpa-test.datagrand.com/#/dashboard')

    def test_03(self):
        task_page = tasksPage(self.driver)
        task_page.addTask_byTiming_dynamicAllocation_Every()
        self.assertEqual(self.driver.current_url,
                         'http://rpa-test.datagrand.com/#/rpa/task-list/create-task?taskId=_NEW_')

    def test_04(self):
        task_page = tasksPage(self.driver)
        task_page.addTask_byTiming_dynamicAllocation_Daily()
        self.assertEqual(self.driver.current_url,
                         'http://rpa-test.datagrand.com/#/rpa/task-list/create-task?taskId=_NEW_')

    def test_05(self):
        task_page = tasksPage(self.driver)
        task_page.addTask_byTiming_dynamicAllocation_Weekly()
        self.assertEqual(self.driver.current_url,
                         'http://rpa-test.datagrand.com/#/rpa/task-list/create-task?taskId=_NEW_')

    def test_06(self):
        task_page = tasksPage(self.driver)
        task_page.addTask_byTiming_dynamicAllocation_Monthly()
        self.assertEqual(self.driver.current_url,
                         'http://rpa-test.datagrand.com/#/rpa/task-list/create-task?taskId=_NEW_')

    def test_07(self):
        task_page = tasksPage(self.driver)
        task_page.addTask_byTiming_dynamicAllocation_Once()
        self.assertEqual(self.driver.current_url,
                         'http://rpa-test.datagrand.com/#/rpa/task-list/create-task?taskId=_NEW_')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
