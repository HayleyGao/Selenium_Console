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

    '''
    作业状态切换后的标签检查
    '''

    def test_03(self):
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Waiting()
        time.sleep(3)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('待执行', status_tag)

    def test_04(self):
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Succeed()
        time.sleep(3)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('成功', status_tag)

    def test_05(self):
        jobs_page = jobsPage(self.driver)
        jobs_page.jobs_status_Terminated()
        time.sleep(5)
        status_tag = jobs_page.job_first_record_status_tag()
        self.assertEqual('已终止', status_tag)

    '''
    用例设计：
    1、更多，不同状态的作业，更多的下拉菜单的操作选项的个数也是不一致的。
        待执行状态，更多-（查看日志、执行、终止）
        成功状态，更多-（查看日志）
        已终止状态，更多-（查看日志）
    2、作业详情，判断弹出的第二列的内容是否为空（看代码是被table包起来的，这就很好解决了），为空则不正常。
    3、作业的导出功能，这部分和审计日志是完全类似的，已经存在。
    
    '''

    '''
    作业详情部分
    '''

    def test_06(self):
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


    def test_07(self):
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



    def test_08(self):
        """
        判断作业详情
        :return:
        """
        jobs_page = jobsPage(self.driver)
        #进入作业列表
        jobs_page.job_list()
        job_details = jobs_page.job_first_record_details_href()
        self.assertEqual('作业详情', job_details)


    def test_08_01(self):
        """
        判断作业详情,作业详情的任务名称是否为空。
        :return:
        """
        jobs_page = jobsPage(self.driver)
        self.driver.refresh()
        #进入作业列表
        jobs_page.job_list()

        #作业详情的任务名称
        job_details = jobs_page.job_first_record_details_dialog()
        self.assertIsNotNone(job_details)

    '''
    更多-不同状态的作业，更多的下拉选项是不一致的。
    '''
    def test_09_01(self):
        """
        判断，作业待执行状态，更多-下拉选项
        :return:
        """
        jobs_page = jobsPage(self.driver)
        self.driver.refresh()
        #进入作业列表
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Waiting()
        time.sleep(3)
        #判断，更多-下拉选项
        options_num=jobs_page.more_options()
        self.assertEqual(3, options_num)

    def test_09_02(self):
        """
        判断，作业成功状态，更多-下拉选项
        :return:
        """
        jobs_page = jobsPage(self.driver)
        #进入作业列表
        self.driver.refresh()
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Succeed()
        time.sleep(3)
        #判断，更多-下拉选项
        options_num=jobs_page.more_options()
        self.assertEqual(1, options_num)

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
        time.sleep(3)
        #判断，更多-下拉选项
        options_num=jobs_page.more_options()
        self.assertEqual(1, options_num)


    '''
    更多-日志-不同状态的日志是不同的：
    1、待执行状态的日志-无日志
    2、成功状态-两种情况：无日志、不为空
    '''
    def test_09_01_01(self):
        """
        判断，作业待执行状态，更多-日志-日志内容-无日志
        :return:
        """
        jobs_page = jobsPage(self.driver)
        self.driver.refresh()
        #进入作业列表
        jobs_page.job_list()

        #切换至“待执行”状态
        jobs_page.jobs_status_Waiting()
        time.sleep(3)
        #判断，更多-日志内容
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertEqual('无日志', log_content)

    @unittest.skip('无条件跳过')
    def test_09_02_01(self):
        """
        判断，作业成功状态，更多-日志-日志内容不为空。
        (作业管理-成功状态-日志-无日志/内容不为空)
        :return:
        """
        jobs_page = jobsPage(self.driver)
        self.driver.refresh()
        #进入作业列表
        jobs_page.job_list()
        #切换至“待执行”状态
        jobs_page.jobs_status_Succeed()
        time.sleep(3)
        #判断，更多-下拉选项
        log_content=jobs_page.more_job_log()
        jobs_page.job_logDialog_closeBtn()
        self.assertIsNotNone(log_content)


    def test_09_03_01(self):
        """
        判断，作业已终止状态，更多-日志
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


    def test_10(self):
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
