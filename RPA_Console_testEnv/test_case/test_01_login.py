import unittest

from selenium.webdriver import Chrome
from selenium import  webdriver
from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.loginPage import loginPage


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.maximize_window()
        cls.url = ReadConfig().getOptionValue('environment', 'url')  # 定义了url为当前类范围。
        print(cls.url)
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger().debug('driver is quit.')


if __name__ == "__main__":
    unittest.main()
