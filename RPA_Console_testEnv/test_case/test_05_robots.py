import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.robotPage import robotsPage
from RPA_Console_testEnv.common.readExcel import readExcel
from RPA_Console_testEnv.common.readConfig import  ReadConfig
from RPA_Console_testEnv.common.log import logger
import math,time



class robotsTest(unittest.TestCase):

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
        搜索，是否包含搜索的内容。
        :return:
        """
        robots_page = robotsPage(self.driver)
        search_str='robot'
        robots_page.robot_search(search_str)
        robot_firstRaw_name_text=robots_page.getFirstRecord_name()
        self.assertIn(search_str, robot_firstRaw_name_text)



    def test_04(self):
        """
        机器人管理-查看作业
        :return:
        """
        robots_page = robotsPage(self.driver)
        robots_page.viewJobs()
        url_=self.url+'#/rpa/robot-list'
        self.assertEqual(url_,self.driver.current_url)

    def wtest_05(self):
        """
        机器人管理-查看作业-不同状态作业的日志
        :return:
        """

        robots_page = robotsPage(self.driver)
        robots_page.viewJobs()
        url_=self.url+'#/rpa/robot-list'
        self.assertEqual(url_,self.driver.current_url)



    @unittest.skip
    def test_06(self):
        """
        机器人管理-更多
        :return:
        """
        robots_page = robotsPage(self.driver)
        robots_page.more()



    def test_07(self):
        """
        机器人状态-在线状态。
        :return:
        """
        robots_page = robotsPage(self.driver)
        robots_page.status_online()
        status_text=robots_page.getRobotStatusText()
        self.assertEqual('在线',status_text)


    def test_08(self):
        """
        没有禁用状态的机器人，会出现"空态图"
        :return:
        """
        robots_page = robotsPage(self.driver)
        robots_page.status_disable()
        status_text=robots_page.emptyGraph()
        self.assertEqual('暂无数据',status_text)



    def test_09(self):
        robots_page = robotsPage(self.driver)
        robots_page.status_offline()
        status_text=robots_page.getRobotStatusText()
        self.assertEqual('离线',status_text)




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()
