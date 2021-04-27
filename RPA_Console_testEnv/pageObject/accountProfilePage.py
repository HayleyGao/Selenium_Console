import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def accountProfile_personalCenter(driver, account, old_pwd, new_pwd):
    """
    用户中心,个人中心
    :param driver:
    :return:
    """
    account_center_ImageHref = driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[2]/div/header-user/div/div[1]/nz-avatar/img')
    account_center_ImageHref.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(account_center_ImageHref).perform()
    # 个人中心
    personal_center = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/section[2]/div[1]')
    personal_center.click()
    time.sleep(2)
    # 个人信息tab
    accountProfile_personalCenter_personalInfo_tab(driver, account)
    time.sleep(1)
    # 修改密码tab
    accountProfile_personalCenter_pwd_Tab(driver, old_pwd, new_pwd)
    time.sleep(1)
    # 密钥tab
    accountProfile_personalCenter_secretKey_Tab(driver)
    time.sleep(1)


def accountProfile_personalCenter_personalInfo_tab(driver, account):
    """
    用户中心,个人中心,个人信息
    :param driver:
    :return:
    """
    # 个人信息tab
    personal_info_tab = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/nz-tabs-nav/div/div/div[1]/div')
    personal_info_tab.click()
    time.sleep(1)
    # 修改用户名
    account_name = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[1]/div/form/section/div[2]/nz-form-item[2]/nz-form-control/div/div/input')
    account_name.clear()
    account_name.send_keys(account + "_")
    time.sleep(1)
    # 点击确定按钮
    presonal_center_confirmBtn = driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[1]/div/form/section/div[2]/nz-form-item[3]/nz-form-control/div/div/button')
    presonal_center_confirmBtn.click()
    time.sleep(1)


def accountProfile_personalCenter_pwd_Tab(driver, old_pwd, new_pwd):
    # 个人中心，密码
    personal_pwd_tab = driver.find_element(By.XPATH,
                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/nz-tabs-nav/div/div/div[2]/div')
    personal_pwd_tab.click()
    time.sleep(1)
    old_pwd_input = driver.find_element(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[2]/div/form/section/div[2]/nz-form-item[1]/nz-form-control/div/div/input')
    old_pwd_input.clear()
    old_pwd_input.send_keys(old_pwd)  # 直接使用全局变量的用户名密码。]
    time.sleep(1)
    new_pwd_input = driver.find_element(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[2]/div/form/section/div[2]/nz-form-item[2]/nz-form-control/div/div/input')
    new_pwd_input.clear()
    new_pwd_input.send_keys(new_pwd)
    time.sleep(1)
    new_pwd_confirm = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[2]/div/form/section/div[2]/nz-form-item[3]/nz-form-control/div/div/input')
    new_pwd_confirm.clear()
    new_pwd_confirm.send_keys(new_pwd)
    time.sleep(1)
    # 点击确认的提交按钮
    update_pwd_submitBtn = driver.find_element(By.XPATH,
                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[2]/div/form/section/div[2]/nz-form-item[4]/nz-form-control/div/div/button')
    # update_pwd_submitBtn.click()
    time.sleep(2)


def accountProfile_personalCenter_secretKey_Tab(driver):
    """
    个人中心，密钥
    :param driver:
    :return:
    """
    secret_key_tab = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/nz-tabs-nav/div/div/div[3]/div')
    secret_key_tab.click()
    time.sleep(2)
    # 密钥，复制
    # copy_secretKey_svg=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[3]/div/form/section/i/svg/path')
    # ActionChains(driver).move_to_element(copy_secretKey_svg).perform()
    # time.sleep(1)
    # copy_secretKey_svg.click()  #"/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-profile/section/nz-card/div/nz-tabset/div/div/div[3]/div/form/section/i/svg"
    # time.sleep(2)


def accountProfile_setting(driver):
    """
    用户配置-设置
    :param driver:
    :return:
    """
    # 用户中心
    account_center_ImageHref2 = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[2]/div/header-user/div/div[1]/nz-avatar/img')
    account_center_ImageHref2.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(account_center_ImageHref2).perform()
    # 设置
    personal_setting = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/section[2]/div[2]')
    personal_setting.click()  # "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/section[2]/div[2]"
    time.sleep(2)
    # 监控大屏展示配置tab
    # 设置语言tab
    monitor_screen_config_tab = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-slef-config/section/nz-tabset/nz-tabs-nav/div/div/div[1]/div')
    monitor_screen_config_tab.click()
    time.sleep(1)
    language_config_tab = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/account-slef-config/section/nz-tabset/nz-tabs-nav/div/div/div[2]/div')
    language_config_tab.click()
    time.sleep(1)


def accountProfile_changeTenant(driver):
    """
    用户配置-切换租户
    切换租户的条件是：该用户一般至少有2个或以上的租户。
    :param driver:
    :return:
    """
    # 用户中心
    account_center_ImageHref2 = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[2]/div/header-user/div/div[1]/nz-avatar/img')
    account_center_ImageHref2.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(account_center_ImageHref2).perform()
    # 切换租户
    personal_setting = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/section[2]/div[3]')
    personal_setting.click()
    time.sleep(2)


def accountProfile_logout(driver):
    """
    用户配置-退出登录
    :param driver:
    :return:
    """
    # 用户中心
    account_center_ImageHref2 = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[2]/div/header-user/div/div[1]/nz-avatar/img')
    account_center_ImageHref2.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(account_center_ImageHref2).perform()
    # 退出登录
    personal_setting = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/section[2]/div[4]')
    personal_setting.click()
    time.sleep(2)
