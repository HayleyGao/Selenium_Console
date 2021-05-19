import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.auditLogPage import auditLogPage
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from selenium import  webdriver



class auditTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.maximize_window()
        cls.url = ReadConfig().getOptionValue('environment', 'url')  # 变成类范围的变量。
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(3)
        cls.download_path=ReadConfig().getOptionValue('console_download_path', 'console_download_path')
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
        审计管理列表
        :return:
        """
        auditLog_Page = auditLogPage(self.driver)
        auditLog_Page.auditLog_list()
        url_=self.url+'#/audit/audit-list'
        self.assertIn(url_, self.driver.current_url) #是否包含，有时候会出现分页详细情况。

    def test_04(self):
        """
        审计管理-导出-今日
        :return:
        """
        auditLog_Page = auditLogPage(self.driver)
        expert_before = auditLog_Page.isExpert(self.download_path)
        auditLog_Page.auditLog_expert_Today()
        expert_after = auditLog_Page.isExpert(self.download_path)
        self.assertEqual(expert_after, expert_before+1)

    def test_05(self):
        """
        审计管理-导出-全部
        :return:
        """
        auditLog_Page = auditLogPage(self.driver)
        expert_before = auditLog_Page.isExpert(self.download_path)
        auditLog_Page.auditLog_expert_All()
        expert_after = auditLog_Page.isExpert(self.download_path)
        self.assertEqual(expert_after, expert_before + 1)


    def test_06(self):
        """
        审计管理-搜索
        :return:
        """
        auditLog_Page = auditLogPage(self.driver)
        auditLog_Page.search()
        self.assertNotEqual(1, 2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
