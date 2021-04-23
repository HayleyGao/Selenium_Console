import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class robotsPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def robots_list_btn(self):
        robots_menu_btn = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[4]')
        return robots_menu_btn

    def robots_list(self):
        # 机器人模块
        self.robots_list_btn().click()
        time.sleep(2)

    def viewJobs_btn(self):
        viewJobs_btn = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
        return viewJobs_btn

    def more_btn(self):
        more_btn = self.driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
        return more_btn

    def robot_searchBox(self):
        """
        搜索框
        :return:
        """
        robot_searchBox = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
        return robot_searchBox

    def robot_search(self):
        """
        搜索框搜索
        :return:
        """
        # 进入robots模块/列表
        self.robots_list_btn().click()
        time.sleep(3)

        # 点击搜索框
        self.robot_searchBox().clear()
        self.robot_searchBox().send_keys('robot')
        time.sleep(1)
        self.robot_searchBox().send_keys(Keys.ENTER)
        time.sleep(2)

    def robots_list_ViewJobs(self):
        # 点击“查看作业”
        robots_list = self.driver.find_elements(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        if len(robots_list) == 0:
            pass
        else:  # 点击查看作业
            robot_first_lookjobs = self.driver.find_element(By.XPATH,
                                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
            robot_first_lookjobs.click()
            time.sleep(2)
            # 点击作业的查看日志
            # 先判断该机器人是否有作业列表
            # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]"
            job_list = self.driver.find_elements(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
            if len(job_list) == 0:
                pass
            else:
                print(len(job_list))
                time.sleep(3)
                # 作业列表，查看日志。【万历环境，td是第10个，test环境第9个，因为存在“环境区别”情况，所以需要加异常处理。】
                job_list0_log = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[9]/div/a')
                job_list0_log.click()  # 万历环境的xpath："/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[10]/div/a"
                time.sleep(2)
                # 关闭展示日志的窗口
                close_logDialog = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
                close_logDialog.click()
                time.sleep(1)
                # 返回机器人列表
                back2robotList_href = self.driver.find_element(By.XPATH,
                                                               '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
                back2robotList_href.click()
                time.sleep(2)
            # 点击“更多”
            robot_first_more = self.driver.find_element(By.XPATH,
                                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
            # robot_first_more.click()
            # 点击，并且悬停在该位置
            ActionChains(self.driver).click(robot_first_more).move_to_element(robot_first_more).perform()
            update_robot = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div/div/ul/bixi-table-operations-group[2]/li')
            update_robot.click()
            time.sleep(5)
            # 填写robot的名称,为什么会定位不到呢？
            # robot_name_input=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-form-item/nz-form-control/div/div/input')
            #
            # robot_name_input.clear()
            # robot_name_input.send_keys('robot_updated')
            # time.sleep(1)
            # robotupdate_confirmBtn=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
            # robotupdate_confirmBtn.click()
            # time.sleep(1)

            # 点击搜索框
            robot_searchBox = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
            robot_searchBox.clear()
            robot_searchBox.send_keys('robot')
            time.sleep(1)
            robot_searchBox.send_keys(Keys.ENTER)
            time.sleep(2)

    def robots_list(self):
        # 机器人模块
        robots_menu_btn = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[4]')
        robots_menu_btn.click()
        time.sleep(2)
        # 点击“查看作业”
        robots_list = self.driver.find_elements(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        if len(robots_list) == 0:
            pass
        else:  # 点击查看作业
            robot_first_lookjobs = self.driver.find_element(By.XPATH,
                                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
            robot_first_lookjobs.click()
            time.sleep(2)
            # 点击作业的查看日志
            # 先判断该机器人是否有作业列表
            # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]"
            job_list = self.driver.find_elements(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
            if len(job_list) == 0:
                pass
            else:
                print(len(job_list))
                time.sleep(3)
                # 作业列表，查看日志。【万历环境，td是第10个，test环境第9个，因为存在“环境区别”情况，所以需要加异常处理。】
                job_list0_log = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[9]/div/a')
                job_list0_log.click()  # 万历环境的xpath："/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[10]/div/a"
                time.sleep(2)
                # 关闭展示日志的窗口
                close_logDialog = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
                close_logDialog.click()
                time.sleep(1)
                # 返回机器人列表
                back2robotList_href = self.driver.find_element(By.XPATH,
                                                               '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
                back2robotList_href.click()
                time.sleep(2)
            # 点击“更多”
            robot_first_more = self.driver.find_element(By.XPATH,
                                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
            # robot_first_more.click()
            # 点击，并且悬停在该位置
            ActionChains(self.driver).click(robot_first_more).move_to_element(robot_first_more).perform()
            update_robot = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div/div/ul/bixi-table-operations-group[2]/li')
            update_robot.click()
            time.sleep(5)
            # 填写robot的名称,为什么会定位不到呢？
            # robot_name_input=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-form-item/nz-form-control/div/div/input')
            #
            # robot_name_input.clear()
            # robot_name_input.send_keys('robot_updated')
            # time.sleep(1)
            # robotupdate_confirmBtn=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
            # robotupdate_confirmBtn.click()
            # time.sleep(1)
