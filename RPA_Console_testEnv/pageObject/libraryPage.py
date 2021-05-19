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


    def isLibraryEmpty(self):
        """
        库管理列表不为空
        :return:
        """
        # 判断，列表是否有记录
        libs_list = self.driver.find_elements(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        length=len(libs_list)
        if length==0:
            return True
        else:
            print(print('libs_list length:', len(libs_list)))
            return False


    def library_list(self):
        """
        库管理列表
        :return:
        """
        self.driver.refresh()
        time.sleep(2)
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)


    def library_historyVersion(self):
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)

        if self.isLibraryEmpty()==True:
            print('no library can be used.')
        else:
            lib_first_versions = self.driver.find_element(By.XPATH,
                                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[7]/bixi-table-col-operations/bixi-col-operations-template/a')
            lib_first_versions.click()
            time.sleep(3)
            # 关闭“历史版本”窗口  #"/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button"
            version_dialog_closeBtn = self.driver.find_element(By.XPATH,
                                                               '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/button')
            version_dialog_closeBtn.click()
            time.sleep(2)




    def library_search(self):
        """
        库管理列表-搜索
        :return:
        """
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)

        if self.isLibraryEmpty() == True:
            print('no library can be used.')
        else:
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


    def library_type_Visual(self):
        """
        库管理列表-类型-可视化类型
        :return:
        """
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)

        if self.isLibraryEmpty() == True:
            print('no library can be used.')
        else:
            # 类型
            lib_type=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
            lib_type.click()
            time.sleep(1)
            # 可视化搜索库和代码流程库
            lib_type_codeLibrary = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/ul/li[1]/label/span[1]/input')
            lib_type_codeLibrary.click()
            time.sleep(1)
            # 点击确定按钮
            lib_type_confirmBtn2 = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/div/button[2]')
            lib_type_confirmBtn2.click()
            time.sleep(4)



    def library_type_Code(self):
        """
        库管理列表-类型-代码类型
        :return:
        """
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)

        if self.isLibraryEmpty() == True:
            print('no library can be used.')
        else:
            # 类型
            lib_type=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
            lib_type.click()
            time.sleep(1)
            # 可视化搜索库和代码流程库
            lib_type_codeLibrary = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/ul/li[2]/label/span[1]/input')
            lib_type_codeLibrary.click()
            time.sleep(1)
            # 点击确定按钮
            lib_type_confirmBtn2 = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/div/button[2]')
            lib_type_confirmBtn2.click()
            time.sleep(4)



    def library_type_Reset(self):
        """
        库管理列表-类型-代码类型
        :return:
        """
        library_menu_Btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
        library_menu_Btn.click()
        time.sleep(3)

        if self.isLibraryEmpty() == True:
            print('no library can be used.')
        else:
            # 类型
            lib_type=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
            lib_type.click()
            time.sleep(1)
            # 可视化搜索库和代码流程库
            lib_type_codeLibrary = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/ul/li[2]/label/span[1]/input')
            lib_type_codeLibrary.click()
            time.sleep(1)
            # 点击确定按钮
            lib_type_confirmBtn2 = self.driver.find_element(By.XPATH,
                                                                '/html/body/div[2]/div[2]/div/div/div/div/button[2]')
            lib_type_confirmBtn2.click()
            time.sleep(4)

            lib_type.click()
            time.sleep(1)
            # 点击“重置按钮”                                 #"/html/body/div[2]/div[3]/div/div/div/div/button[1]"
            lib_type_resetBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/button[1]')
            lib_type_resetBtn.click()
            time.sleep(4)


    def getFirstRecordTypeText(self):
        """
        获取第一行记录的类型标签
        :return:
        """
        if self.isLibraryEmpty()==True:
            return None
        else:                                #"/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[2]/bixi-table-col-text/div/span"
            typeText=self.driver.find_element(By.XPATH,"/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[2]/bixi-table-col-text/div/span").get_attribute("innerText")
            print('typeText',typeText)
            return typeText


    def pageination(self):
        """
        翻页
        :return:
        """
        self.library_list()
        time.sleep(2)
        if self.isLibraryEmpty()==True:
            print('no library can be used.')
        else:
            pass


