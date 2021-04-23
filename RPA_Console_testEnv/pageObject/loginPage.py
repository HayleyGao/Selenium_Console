import time

from selenium.webdriver.common.by import By


# import  base
# import tasksManagement


class loginPage():
    def __init__(self, driver):
        """
        构造函数，需要传参driver。
        :param driver:
        """
        self.driver = driver

    def username(self):
        """
        获取账号输入框对象
        :return:
        """
        account_input = self.driver.find_element(By.XPATH,
                                                 "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                                 "2]/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")
        return account_input

    def password(self):
        """
        密码输入框
        :return:
        """
        pwd_input = self.driver.find_element(By.XPATH,
                                             "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                             "2]/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")
        return pwd_input

    def loginBtn(self):
        """
        登录按钮
        :return:
        """
        login_btn = self.driver.find_element(By.XPATH,
                                             "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                             "2]/form/nz-form-item[4]/button")
        return login_btn

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

    def loginIn(self, account, pwd):
        """
        登录函数
        :param account:
        :param pwd:
        :return:
        """
        self.username().send_keys(account)
        self.driver.implicitly_wait(1)
        self.password().send_keys(pwd)
        self.driver.implicitly_wait(1)
        self.loginBtn().click()
        time.sleep(5)
