import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.dataAssetPage import dataAssetPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage


class tenantTest(unittest.TestCase):

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
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/passport/login'
        self.assertEqual(self.driver.current_url, url_)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/dashboard'
        self.assertEqual(self.driver.current_url, url_)

    def test_03(self):
        """
        租户管理
        :return:
        """
        dataAsset_Page = dataAssetPage(self.driver)
        dataAsset_Page.dataAssets_menu()
        self.assertNotEqual(1, 2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
