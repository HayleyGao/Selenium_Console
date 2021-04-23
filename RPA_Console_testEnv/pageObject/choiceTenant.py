import time

from selenium.webdriver.common.by import By


# import  base
# import tasksManagement


class choiceTenantPage():
    def __init__(self, driver):
        """
        构造函数，需要传参driver。
        :param driver:
        """
        self.driver = driver

    def enter_tenant_btn(self):
        """
        选择租户函数（当当前账号的租户在两个或以上时，进入console需要该步骤。）
        需要login_test()函数为前序步骤。
        :param driver:
        :return:
        """
        # 选择租户,现在选择当前默认的租户,单独一个租户时，直接默认进入。
        enter_tenant_btn = self.driver.find_element(By.XPATH,
                                                    "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div["
                                                    "2]/div[2]/div[2]/button")
        return enter_tenant_btn

    def choiceTenant(self):
        """
        登录函数
        :param account:
        :param pwd:
        :return:
        """
        self.enter_tenant_btn().click()
        time.sleep(3)
