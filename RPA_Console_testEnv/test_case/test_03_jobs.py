import time
import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.jobPage import jobsPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage


class jobsTest(unittest.TestCase):

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
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Waiting()
        time.sleep(2)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('待执行', status_tag)

    def test_04(self):
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Succeed()
        time.sleep(2)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('成功', status_tag)

    def test_05(self):
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Terminated()
        time.sleep(2)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('已终止', status_tag)

    def test_10(self):
        """
        判断"今天范围"作业是否导出成功
        :return:
        """
        jobs_page = jobsPage(self.driver)
        console_download_path = ReadConfig().getOptionValue('console_download_path', 'console_download_path')
        isExpert_before = jobs_page.isExpert(console_download_path)
        jobs_page.jobs_list_expert_byToday()
        time.sleep(2)
        isExpert_after = jobs_page.isExpert(console_download_path)
        self.assertEqual(isExpert_after, isExpert_before + 1)

    def test_11(self):
        """
        判断"全部-自定义范围"作业是否导出成功
        :return:
        """
        jobs_page = jobsPage(self.driver)
        console_download_path = ReadConfig().getOptionValue('console_download_path', 'console_download_path')
        isExpert_before = jobs_page.isExpert(console_download_path)
        jobs_page.jobs_list_expert_byAll()
        time.sleep(2)
        isExpert_after = jobs_page.isExpert(console_download_path)
        self.assertEqual(isExpert_after, isExpert_before + 1)

    def test_12(self):
        """
        判断作业详情
        :return:
        """
        jobs_page = jobsPage(self.driver)
        job_details = jobs_page.job_first_record_details()
        self.assertEqual('作业详情', job_details)

    def test_13(self):
        """
        判断，更多，查看日志
        :return:
        """
        jobs_page = jobsPage(self.driver)
        jobs_page.more_job_log()
        self.assertEqual(1, 1)

    def test_13(self):
        """
        搜索框
        :return:
        """
        jobs_page = jobsPage(self.driver)
        jobs_page.job_searchBox("task")
        self.assertEqual(1, 1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger().debug('driver is quit.')


if __name__ == "__main__":
    unittest.main()
