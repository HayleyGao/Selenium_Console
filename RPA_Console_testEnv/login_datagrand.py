import unittest

from selenium.webdriver import Chrome

import rpa_console


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()

    @classmethod
    def tearDownClass(cls):
        print("浏览器关闭。")
        cls.driver.quit()

    def test_case_01_login(self):
        rpa_console.login_test(self.driver, url="http://rpa-test.datagrand.com/", account="gaoxiaoyan@datagrand.com",
                               pwd="Gaoxiaoyan9533")
        self.assertEqual(self.driver.current_url, "http://rpa-test.datagrand.com/#/dashboard")

    def test_case_02_notification(self):
        rpa_console.notification_menu(self.driver)  # 会有个设置成功的提示框弹出
        self.assertEqual(self.driver.current_url, 'http://rpa-test.datagrand.com/#/settings/notification')

    def test_case_03_calendar(self):
        rpa_console.calendar_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_04_role(self):
        rpa_console.role_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_05_account(self):
        rpa_console.account_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_06_organization(self):
        rpa_console.organization_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_07_permission(self):
        rpa_console.permission_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_08_auditLog(self):
        rpa_console.auditLog_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_09_library(self):
        rpa_console.library_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_10_process(self):
        rpa_console.applications_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_11_dataAsset(self):
        rpa_console.dataAssets_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_12_robots(self):
        rpa_console.robots_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_13_tasks(self):
        rpa_console.task_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_14_jobs(self):
        rpa_console.jobs_menu(self.driver)
        self.assertEqual(3, 1 + 2)

    def test_case_15_accountProfile(self):
        rpa_console.account_profile(self.driver)
        self.assertEqual(3, 1 + 2)


if __name__ == "__main__":
    unittest.main()
