import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.robotPage import robotsPage


class robotsTest(unittest.TestCase):

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
        robots_page = robotsPage(self.driver)
        robots_page.robot_search()
        self.assertEqual(3, 1 + 2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
