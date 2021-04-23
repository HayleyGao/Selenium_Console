import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class auditLogPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def auditLog_menu(self):
        # 审计日志
        auditLog_menu_btn = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[8]')
        auditLog_menu_btn.click()
        time.sleep(3)

        # 下拉选择范围
        select_menu = self.driver.find_element(By.XPATH,
                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-select/nz-select-top-control/nz-select-search/input')
        select_menu.click()
        time.sleep(1)
        option_item3 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[3]/div')
        option_item3.click()
        time.sleep(1)
        # 点击导出按钮
        export_btn = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/button')
        export_btn.click()
        time.sleep(3)
        # 选择“全部”
        select_menu2 = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-select/nz-select-top-control/nz-select-search/input')
        select_menu2.click()
        time.sleep(2)
        option_item1 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div')
        option_item1.click()
        time.sleep(1)
        # 点击“日历组件
        # 开始时间
        # 通过jquery删除readonly属性或者改变readonly属性
        js = 'document.getElementsByTagName("input")[1].removeAttribute("readonly");'
        self.driver.execute_script(js)
        calerdate_input_begin = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-range-picker/div/div[1]/input')
        time.sleep(1)
        calerdate_input_begin.send_keys("2021-04-01 12:00")

        time.sleep(1)
        calerdate_input_end = self.driver.find_element(By.XPATH,
                                                       "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-range-picker/div/div[3]/input")
        js2 = 'document.getElementsByTagName("input")[2].removeAttribute("readonly");'
        self.driver.execute_script(js2)
        calerdate_input_end.send_keys("2021-04-12 12:00")
        time.sleep(1)

        # 点击日历组件的确定按钮
        calendar_confirm_btn = self.driver.find_element(By.XPATH,
                                                        '/html/body/div[2]/div[3]/div/div/div/date-range-popup/div/div[2]/calendar-footer/div/ul/li/button')
        calendar_confirm_btn.click()
        time.sleep(1)

        # 点击导出按钮
        export_btn = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/button')
        export_btn.click()
        time.sleep(3)

        # 点击搜索框
        auditLog_searchBox = self.driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/div/nz-input-group/input')
        auditLog_searchBox.clear()
        auditLog_searchBox.send_keys('登录')
        time.sleep(1)
        auditLog_searchBox.send_keys(Keys.ENTER)
        time.sleep(3)
