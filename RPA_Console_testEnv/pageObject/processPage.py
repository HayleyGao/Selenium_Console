import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class processPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def applications_list(self):
        # 流程管理
        self.driver.refresh()
        time.sleep(2)
        applications_menu = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[6]')
        applications_menu.click()
        time.sleep(2)


    def isApplicationsEmpty(self):
        """
        判断流程列表是否为空
        :return:
        """
        # 流程列表
        applications_list = self.driver.find_elements(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        length=len(applications_list)
        if length==0:
            return True
        else:
            print('applications_list is empty', length)
            return False



    def applications_historyVersion(self):
        """
        流程列表-历史版本
        :return:
        """
        self.driver.refresh()
        time.sleep(3)
        # 流程管理
        applications_menu = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[6]')
        applications_menu.click()
        time.sleep(2)

        # 流程列表
        if self.isApplicationsEmpty() == True:
            return None
        else:
            # 点击记录的“历史版本”对话框
            history_version = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[4]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
            history_version.click()
            time.sleep(2)
            # 点击关闭窗口
            history_version_closeBtn = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/button')
            history_version_closeBtn.click()
            time.sleep(2)




    def applications_sharingSetting(self):
        """
        流程列表-共享设置
        :return:
        """
        self.driver.refresh()
        time.sleep(3)
        # 流程管理
        applications_menu = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[6]')
        applications_menu.click()
        time.sleep(2)

        # 流程列表
        if self.isApplicationsEmpty() == True:
            return None
        else:
            # 点击“共享设置”
            sharing_setting = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[4]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
            sharing_setting.click()
            time.sleep(2)
            # 返回至流程列表
            back2_applicationsList = self.driver.find_element(By.XPATH,
                                                              '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
            back2_applicationsList.click()
            time.sleep(2)


    def applications_search(self):
        """
        流程列表-搜索
        :return:
        """
        self.driver.refresh()
        time.sleep(3)
        # 流程管理
        applications_menu = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[6]')
        applications_menu.click()
        time.sleep(2)

        # 流程列表
        if self.isApplicationsEmpty() == True:
            return None
        else:
            # 流程搜索框
            applications_searchBox = self.driver.find_element(By.XPATH,
                                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
            applications_searchBox.clear()
            applications_searchBox.send_keys('流程')
            time.sleep(1)
            applications_searchBox.send_keys(Keys.ENTER)
            time.sleep(2)


    def emptyGraph(self):
        """
        空态图
        :return:
        """
        pass

    def pageination(self):
        """
        翻页处理
        :return:
        """
        pass


