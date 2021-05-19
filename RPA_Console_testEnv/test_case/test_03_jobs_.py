import time
import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.jobPage import jobsPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from selenium import  webdriver

class jobsTest(unittest.TestCase):

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




    def test_09_01(self):
        """
        判断，作业待执行状态，更多-日志-日志内容
        :return:
        """
        jobs_page = jobsPage(self.driver)
        #进入作业列表
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Waiting()
        time.sleep(2)
        #判断，更多-日志内容
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertEqual('无日志', log_content)


    def test_09_02_01(self):
        """
        判断，作业成功状态，更多-日志-无日志/不为空。
        :return:
        """
        jobs_page = jobsPage(self.driver)
        #进入作业列表
        self.driver.refresh()
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Succeed()
        time.sleep(2)
        #判断，更多-下拉选项
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertEqual('无日志', log_content)

    def test_09_02_02(self):
        """
        判断，作业成功状态，更多-日志-无日志/不为空。
        :return:
        """
        jobs_page = jobsPage(self.driver)
        #进入作业列表
        self.driver.refresh()
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Succeed()
        time.sleep(2)

        #判断，更多-无日志/不为空
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertIsNotNone(log_content)



    def test_09_03(self):
        """
        判断，作业已终止状态，更多-下拉选项
        :return:
        """
        jobs_page = jobsPage(self.driver)
        self.driver.refresh()
        #进入作业列表
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Terminated()
        time.sleep(2)
        #判断，更多-下拉选项
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertEqual('无日志', log_content)





    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger().debug('driver is quit.')


if __name__ == "__main__":
    unittest.main()
