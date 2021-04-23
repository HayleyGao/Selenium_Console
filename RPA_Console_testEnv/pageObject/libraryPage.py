import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class libraryPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def library_menu(self):
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)
        # 判断，列表是否有记录
        libs_list = self.driver.find_elements(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        print('libs_list length:', len(libs_list))
        if len(libs_list) == 0:
            print('no library can be used.')
        else:
            lib_first_versions = self.driver.find_element(By.XPATH,
                                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[7]/bixi-table-col-operations/bixi-col-operations-template/a')
            lib_first_versions.click()
            time.sleep(3)
            # 关闭“历史版本”窗口  #"/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button"
            version_dialog_closeBtn = self.driver.find_element(By.XPATH,
                                                               '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
            version_dialog_closeBtn.click()
            time.sleep(2)
            # 搜索框
            library_searchBox = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
            library_searchBox.clear()
            library_searchBox.send_keys('lib')
            time.sleep(1)
            library_searchBox.send_keys(Keys.ENTER)
            time.sleep(3)
            # 清空搜索框
            library_searchBox.clear()  # 会默认输出所有的内容
            library_searchBox.send_keys(Keys.ENTER)
            time.sleep(4)
            # 类型
            lib_type = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
            lib_type.click()
            time.sleep(1)
            # 可视化搜索库和代码流程库  #"/html/body/div[2]/div[3]/div/div/div/ul/li[1]/label/span[1]/input"
            lib_type_visualLibrary = self.driver.find_element(By.XPATH,
                                                              '/html/body/div[2]/div[3]/div/div/div/ul/li[1]/label/span[1]/input')
            lib_type_visualLibrary.click()
            time.sleep(1)
            # 点击确定按钮
            lib_type_confirmBtn = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
            lib_type_confirmBtn.click()
            time.sleep(4)
            # 类型
            # lib_type=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
            lib_type.click()
            time.sleep(1)
            # 可视化搜索库和代码流程库
            lib_type_codeLibrary = self.driver.find_element(By.XPATH,
                                                            '/html/body/div[2]/div[3]/div/div/div/ul/li[2]/label/span[1]/input')
            lib_type_codeLibrary.click()
            time.sleep(1)
            # 点击确定按钮
            lib_type_confirmBtn2 = self.driver.find_element(By.XPATH,
                                                            '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
            lib_type_confirmBtn2.click()
            time.sleep(4)

            lib_type.click()
            time.sleep(1)
            # 点击“重置按钮”                                 #"/html/body/div[2]/div[3]/div/div/div/div/button[1]"
            lib_type_resetBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[1]')
            lib_type_resetBtn.click()
            time.sleep(4)
