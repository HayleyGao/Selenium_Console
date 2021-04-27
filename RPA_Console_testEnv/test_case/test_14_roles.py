import math
import time
import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.rolesPage import rolesPage
from selenium import  webdriver


class rolesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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
        角色管理
        :return:
        """
        roles_Page = rolesPage(self.driver)
        time.sleep(3)
        roles_Page.role_list()
        role_name_str="role_" + str(math.ceil(time.time()))
        roles_Page.add_new_role(role_name_str)
        add_role_after=roles_Page.getFirstRecordName()
        self.assertEqual(role_name_str, add_role_after)

    def test_04(self):
        """
        角色管理,删除
        :return:
        """
        roles_Page = rolesPage(self.driver)
        time.sleep(3)
        roles_Page.role_list()
        delete_before=roles_Page.getFirstRecordName()
        roles_Page.role_delete()
        delete_after=roles_Page.getFirstRecordName()
        self.assertNotEqual(delete_before, delete_after)

    def test_05(self):
        """
        角色管理,搜索
        :return:
        """
        roles_Page = rolesPage(self.driver)
        time.sleep(3)
        roles_Page.role_list()
        search_str='role'
        roles_Page.search(search_str)
        search_result=roles_Page.getFirstRecordName()
        self.assertIn(search_str, search_result)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
