import time

from selenium.webdriver.common.by import By


class licensePage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def permission_menu(self):
        # 继续“许可管理”
        permission_menu_btn = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[1]')
        permission_menu_btn.click()
        time.sleep(3)
        # 机器人列表
        robot_device_list = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-device-list/section/nz-card/div[2]/nz-tabset/nz-tabs-nav/div/div/div[1]/div')
        robot_device_list.click()
        time.sleep(2)
        # studio列表
        studio_device_list = self.driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-device-list/section/nz-card/div[2]/nz-tabset/nz-tabs-nav/div/div/div[2]/div')
        studio_device_list.click()
        time.sleep(2)
