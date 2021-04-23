import os
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class jobsPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def job_list_btn(self):
        """
        作业管理菜单栏的链接
        :return:
        """
        jobs_menun_btn = self.driver.find_element(By.XPATH,
                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[2]')
        return jobs_menun_btn

    def job_list(self):
        """
        进入作业管理列表
        :return:
        """
        self.job_list_btn().click()
        time.sleep(5)

    def jobs_expert_btn(self):
        # 点击“导出按钮”
        jobs_expert_button = self.driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/button')
        return jobs_expert_button

    def isExpert(self, console_download_path):
        """
        判断作业导出是否成功
        :return:
        """
        # 浏览器下载文件夹的地址：
        # console_download_path = r"C:\Users\caiwenjie\Downloads"
        download_list = os.listdir(console_download_path)
        print(len(download_list))
        return len(download_list)

    def jobs_list_expert_byToday(self):
        # 进入作业列表
        self.job_list_btn().click()
        time.sleep(3)

        # 选择作业范围，导出
        job_select = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-select')
        job_select.click()
        time.sleep(1)
        # 点击“今天”范围
        item_today = self.driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div[2]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[3]')
        item_today.click()
        time.sleep(2)
        self.jobs_expert_btn().click()

    def getDate(self):
        date = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        return date

    def jobs_list_expert_byAll(self):
        # 进入作业列表
        self.job_list_btn().click()
        time.sleep(3)

        # select选择“全部”范围
        job_select = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-select')
        job_select.click()
        time.sleep(3)
        item_all = self.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
        item_all.click()
        time.sleep(1)
        # 点击，日历的起始和终止范围<这里需要js辅助>
        # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[1]/input"
        js_start = 'document.getElementsByTagName("input")[0].removeAttribute("readonly");'
        js_end = 'document.getElementsByTagName("input")[1].removeAttribute("readonly");'
        self.driver.execute_script(js_start)
        self.driver.execute_script(js_end)

        startTime = "2021-03-01 12:00"
        endTime = self.getDate()

        calendar_start = self.driver.find_element(By.XPATH,
                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[1]/input')
        calendar_start.send_keys(startTime)
        time.sleep(1)
        calendar_end = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[3]/input')
        calendar_end.send_keys(endTime)
        time.sleep(3)
        # 点击“确定”按钮
        calendar_end_confirmBtn = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[3]/div/div/div/date-range-popup/div/div[2]/calendar-footer/div/ul/li/button')
        calendar_end_confirmBtn.click()
        time.sleep(1)
        self.jobs_expert_btn().click()
        time.sleep(4)

    def jobs_list_statusBtn(self):
        """
        点击列表的“状态”选择
        :return:
        """
        job_statusFilter = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/thead/tr/th[6]/nz-table-filter/nz-filter-trigger/span')
        return job_statusFilter

    def jobs_status_item(self, i):
        status_item_xpath = "/html/body/div[2]/div[2]/div/div/div/ul/li[" + str(i) + "]"
        print(status_item_xpath)
        status_item = self.driver.find_element(By.XPATH, status_item_xpath)
        status_item.click()
        time.sleep(2)

    def status_confirmBtn(self):
        # 状态列表，确定按钮
        status_confirmBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/button[2]')
        status_confirmBtn.click()
        time.sleep(3)

    def status_resetBtn(self):
        # 状态列表，“重置”按钮
        status_resetBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[1]')
        status_resetBtn.click()
        time.sleep(2)

    def jobs_status_Waiting(self):
        """
        作业管理，等待状态
        :return:
        """
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(1)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Executing(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(2)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Terminating(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(3)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Paused(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(4)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Terminated(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(5)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Succeed(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(6)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Exception(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(7)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Lost(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)
        # 点击“选项”
        self.jobs_status_item(8)
        time.sleep(1)
        # 点击“确定”按钮
        self.status_confirmBtn()
        time.sleep(3)

    def jobs_status_Reset(self):
        # 进入“作业管理”列表
        self.job_list()

        # 点击“状态”按钮
        self.jobs_list_statusBtn().click()
        time.sleep(2)

        # 点击“重置”按钮
        self.status_resetBtn()
        time.sleep(3)

    def isJobListEmpty(self):
        """
        判断，作业列表是否为空
        :return:
        """
        job_list = self.driver.find_elements(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr')
        if len(job_list) == 0:
            return True
        else:
            print('job_list length:', len(job_list))
            return False

    def job_first_record_status_tag(self):
        """
        作业列表中，第一条记录的"状态标签"
        :return:返回状态标签的文本名称
        """
        global job_item_status_tag_text
        if not self.isJobListEmpty():
            job_item_status_tag = self.driver.find_element(By.XPATH,
                                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr[2]/td[6]/shared-status-tag/div/span')
            job_item_status_tag_text = job_item_status_tag.get_attribute("innerText")  # "text"
            print('job_item_status_tag_text', job_item_status_tag_text)
        return job_item_status_tag_text

    def job_details(self):
        job_first_record_details = self.driver.find_element(By.XPATH,
                                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr[2]/td[11]/shared-actions/shared-action-item/span[2]/a')
        return job_first_record_details

    def job_first_record_details(self):
        """
        作业列表中，第一条记录的"作业详情"
        :return:返回作业详情超链接的文本
        """
        global job_first_record_details_text
        if not self.isJobListEmpty():
            job_first_record_details_text = self.job_details().get_attribute("innerText")  # "text"
            print('job_first_record_details_text', job_first_record_details_text)
        return job_first_record_details_text

    def more(self):
        """
        “更多”
        :return:
        """
        jobs_more = self.driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr[2]/td[11]/shared-actions/shared-action-overlay/a')
        return jobs_more

    def more_job_log(self):
        ActionChains(self.driver).click(self.more()).move_to_element(self.more()).perform()
        time.sleep(1)
        job_log = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/ul/li[1]')
        job_log.click()
        time.sleep(2)
        job_logDialog_closeBtn = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button")
        job_logDialog_closeBtn.click()
        time.sleep(2)

    def more_execute(self):
        """
        执行情况，分很多种，待后续...
        :return:
        """
        ActionChains(self.driver).click(self.more()).move_to_element(self.more()).perform()
        time.sleep(1)
        job_execute = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/ul/li[2]')
        job_execute.click()
        time.sleep(2)

    def more_terminal(self):
        """
        终止操作，待后续...
        :return:
        """
        ActionChains(self.driver).click(self.more()).move_to_element(self.more()).perform()
        time.sleep(1)
        job_execute = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/ul/li[3]')
        job_execute.click()
        time.sleep(2)

    def job_searchBox(self, search_str):
        """
        作业模块的搜索框
        :return:
        """
        # search_str='task'
        searchBox_input = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/div/nz-input-group/input')
        searchBox_input.clear()
        searchBox_input.send_keys(search_str)
        time.sleep(1)
        searchBox_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def pagination(self):
        """
        分页处理
        :return:
        """
        pass
