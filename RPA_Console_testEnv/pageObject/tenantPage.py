import random
import time

from selenium.webdriver.common.by import By


class tenantPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def tenant_menu(self):
        # 租户管理
        tenant_menu_btn = self.driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[2]')
        tenant_menu_btn.click()
        time.sleep(2)
        # 新增租户
        add_tenant = self.driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-tenant-list/section/shared-list-search/div/div/div[1]/button')
        add_tenant.click()
        time.sleep(2)
        tenant_name = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/div/input')
        tenant_name_str = 'tenant_' + str(random.randrange(1, 25535))
        tenant_name.send_keys(tenant_name_str)
        time.sleep(1)
        adminName = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/div/input')
        adminName.send_keys(tenant_name_str)
        time.sleep(1)
        admin_email = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[3]/nz-form-control/div/div/input')
        admin_email.send_keys(tenant_name_str + '@datagrand_test.com')
        time.sleep(1)
        # 分配许可
        rootCount = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[1]/div/div[2]/nz-form-control/div/div/input')
        rootCount.send_keys(1)
        time.sleep(1)
        studioCount = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[2]/div/div[2]/nz-form-control/div/div/input')
        studioCount.send_keys(1)
        time.sleep(1)
        expire = self.driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[3]/div/div[2]/nz-form-control/div/div/input')
        expire.send_keys(5)
        time.sleep(1)
        # 点击确定按钮
        tenant_submit_btn = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]')
        tenant_submit_btn.click()
        time.sleep(1)
        # 确认对话框
        tenant_confirm_btn = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button')
        tenant_confirm_btn.click()
        time.sleep(5)
