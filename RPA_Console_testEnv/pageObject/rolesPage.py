import math
import time

from selenium.webdriver.common.by import By


class rolesPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def role_menu(self):
        # 进入“角色管理”模块
        role_menu_btn = self.driver.find_element(By.XPATH,
                                                 "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[5]")
        role_menu_btn.click()
        time.sleep(2)
        # 新增角色
        add_role_btn = self.driver.find_element(By.XPATH,
                                                "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/shared-list-search/div/div/div[1]/button")
        add_role_btn.click()
        time.sleep(3)
        # 填写角色名称
        role_name = self.driver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/nz-spin/div/form/nz-form-item/nz-form-control/div/div/input")
        role_name.send_keys("role_" + str(math.ceil(time.time())))
        time.sleep(1)
        # 选择权限
        authorities = self.driver.find_elements(By.XPATH,
                                                '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/nz-spin/div/nz-table/nz-spin/div/div/nz-table-inner-scroll/div[2]/table/tbody/tr/td/label/span/input')
        print(len(authorities))
        for x in authorities:
            if x.is_selected() == True:
                pass
            else:
                x.click()
        time.sleep(1)
        # 点击确定按钮
        role_confirm_btn = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]")
        role_confirm_btn.click()
        time.sleep(5)
