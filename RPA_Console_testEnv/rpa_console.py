import math
import random
import time

import win32con
import win32gui
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import accountProfile
import tasksManagement


def login_test(driver, url, account, pwd):
    driver.get(url)
    time.sleep(1)
    driver.maximize_window();
    time.sleep(1)
    account_input = driver.find_element(By.XPATH, "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                                  "2]/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")
    time.sleep(1)
    account_input.send_keys(account);
    time.sleep(1)
    pwd_input = driver.find_element(By.XPATH, "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                              "2]/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")
    pwd_input.send_keys(pwd);
    time.sleep(1)
    login_btn = driver.find_element(By.XPATH, "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div[1]/div["
                                              "2]/form/nz-form-item[4]/button")
    login_btn.send_keys(Keys.ENTER);
    time.sleep(4)
    choiceTenant(driver)  # 选择租户


def choiceTenant(driver):
    """
    选择租户函数（当当前账号的租户在两个或以上时，进入console需要该步骤。）
    需要login_test()函数为前序步骤。
    :param driver:
    :return:
    """
    # 选择租户,现在选择当前默认的租户,单独一个租户时，直接默认进入。
    enter_tenant_btn = driver.find_element(By.XPATH, "/html/body/rpa-root/rpa-login/div/div[2]/div/div[2]/div/div["
                                                     "2]/div[2]/div[2]/button")
    enter_tenant_btn.send_keys(Keys.ENTER)
    time.sleep(5)


def notification_menu(driver):
    # 通知设置模块
    notification_menu_btn = driver.find_element(By.XPATH,
                                                "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div["
                                                "2]/ul/li[7]")
    notification_menu_btn.click()
    time.sleep(3)
    # 进入通知设置界面
    # 1.1 勾选“通知内容”
    checkboxs_notice_content = driver.find_elements(By.XPATH,
                                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[1]/nz-form-control/div/div/nz-checkbox-group/label/span/input")
    # print(len(checkboxs))
    # print(type(checkboxs))
    for x in checkboxs_notice_content:
        if x.is_selected() == True:
            pass
        else:
            x.click()
    time.sleep(2)
    # 1.2 勾选“通知类型”
    checkboxs_notice_type = driver.find_elements(By.XPATH,
                                                 "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[2]/nz-form-control/div/div/nz-checkbox-wrapper/div/div/label/span/input")
    # print(len(checkboxs_notice_type))
    # print(type(checkboxs_notice_type))
    for y in checkboxs_notice_type:
        if y.is_selected() == True:
            pass
        else:
            y.click()
    time.sleep(2)
    # 填写邮箱信息区域
    # server_domain
    print("start fill email information.")
    email_address = driver.find_element(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[3]/nz-form-control/div/div/div/div/input')
    email_address.clear()
    email_address.send_keys("smtp.mxhichina.com")
    time.sleep(1)
    email_port = driver.find_element(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[4]/nz-form-control/div/div/div/div/nz-input-number/div[2]/input')
    time.sleep(1)

    # print("email_port.text",email_port.text)
    # print(email_port.get_attribute("value"))
    if email_port.get_attribute("value") == "465":
        pass
    else:
        email_port.clear()
        email_port.send_keys("465")  # 端口这里的输入框是属于复合输入框。

    time.sleep(1)
    email_sender = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[5]/nz-form-control/div/div/div/div/input')
    email_sender.clear()
    email_sender.send_keys("notice@datagrand.com")
    time.sleep(1)
    email_sender_pwd = driver.find_element(By.XPATH,
                                           "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/form/nz-form-item[6]/nz-form-control/div/div/div/div/nz-input-group/input")
    email_sender_pwd.clear()
    email_sender_pwd.send_keys("DAguan123.")
    time.sleep(1)
    notification_sumbitBtn = driver.find_element(By.XPATH,
                                                 "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-settings-notification/section/nz-card/div[2]/div/button")
    notification_sumbitBtn.send_keys(Keys.ENTER)
    time.sleep(3)
    # 可能会弹出确认对话框
    confirm_btn = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
    confirm_btn.click()  # 这里点击了“确定按钮”
    time.sleep(3)


def calendar_menu(driver):
    # 进入“日历管理”
    time.sleep(1)
    calendar_menu_btn = driver.find_element(By.XPATH,
                                            "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[6]/span")
    calendar_menu_btn.click()
    time.sleep(3)
    # 点击“新建日历”
    add_calendar_btn = driver.find_element(By.XPATH,
                                           "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-list/section/shared-list-search/div/div/div[1]/button")
    add_calendar_btn.click()
    time.sleep(1)
    # 日历名称
    calendarName = driver.find_element(By.XPATH,
                                       "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[1]/form/nz-form-item/nz-form-control/div/div/input")
    calendarName.clear()
    # 先用时间戳进行连接吧。
    calendarName.send_keys("calendar_" + str(math.ceil(time.time())))
    time.sleep(1)

    # 点击下载模板的链接
    calendar_template_download = driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[2]/p[2]')
    calendar_template_download.click()
    time.sleep(2)

    # 点击上传文件的链接
    calendarfile_uplink = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[2]/p[1]/nz-upload/div/div/p')
    calendarfile_uplink.click()
    time.sleep(2)

    calendarfile_path = r"C:\download\RPA10.0\Calendar template_20201110.csv"
    # 由于弹出了上传的对话框，所以，用pywin32解决.
    # 1.找窗口，获取窗口的句柄、文本、Class类型等方式。
    dialog_upload = win32gui.FindWindow("#32770", '打开')  # 32770是ClassName。
    print('dialog_upload', dialog_upload)
    # 2.输入本地文件的绝对路径，点击“打开”按钮
    # 找元素
    # 寻找子窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog_upload, 0, 'ComboBoxEx32', None)
    # print('ComboBoxEx32',ComboBoxEx32)
    combox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    # print('combox',combox)
    edit = win32gui.FindWindowEx(combox, 0, 'Edit', None);  # 找到编辑框,这里返回的都是句柄。
    # print(edit)
    button = win32gui.FindWindowEx(dialog_upload, 0, 'Button', '打开(&O)');  # 找到“点击”按钮
    # print(button)

    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, calendarfile_path)  # 输入文件路径
    win32gui.SendMessage(dialog_upload, win32con.WM_COMMAND, 1, button)  # 点击”打开“按钮
    time.sleep(2)
    # 此处为上传成功
    # 点击“已选中”的日期
    show_all_selected = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/main/div[4]/p/span[2]')
    show_all_selected.click()
    time.sleep(1)  # 等待展开所有的内容
    # 点击保存按钮
    save_btn = driver.find_element(By.XPATH,
                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-calendar-edit/section/nz-spin/div/footer/div[2]/button[2]')
    save_btn.click()
    time.sleep(2)


def role_menu(driver):
    # 进入“角色管理”模块
    role_menu_btn = driver.find_element(By.XPATH,
                                        "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[5]")
    role_menu_btn.click()
    time.sleep(2)
    # 新增角色
    add_role_btn = driver.find_element(By.XPATH,
                                       "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/shared-list-search/div/div/div[1]/button")
    add_role_btn.click()
    time.sleep(3)
    # 填写角色名称
    role_name = driver.find_element(By.XPATH,
                                    "/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/nz-spin/div/form/nz-form-item/nz-form-control/div/div/input")
    role_name.send_keys("role_" + str(math.ceil(time.time())))
    time.sleep(1)
    # 选择权限
    authorities = driver.find_elements(By.XPATH,
                                       '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/nz-spin/div/nz-table/nz-spin/div/div/nz-table-inner-scroll/div[2]/table/tbody/tr/td/label/span/input')
    print(len(authorities))
    for x in authorities:
        if x.is_selected() == True:
            pass
        else:
            x.click()
    time.sleep(1)
    # 点击确定按钮
    role_confirm_btn = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]")
    role_confirm_btn.click()
    time.sleep(5)


def tenant_menu(driver):
    # 租户管理
    tenant_menu_btn = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[2]')
    tenant_menu_btn.click()
    time.sleep(2)
    # 新增租户
    add_tenant = driver.find_element(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-tenant-list/section/shared-list-search/div/div/div[1]/button')
    add_tenant.click()
    time.sleep(2)
    tenant_name = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/div/input')
    tenant_name_str = 'tenant_' + str(random.randrange(1, 25535))
    tenant_name.send_keys(tenant_name_str)
    time.sleep(1)
    adminName = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/div/input')
    adminName.send_keys(tenant_name_str)
    time.sleep(1)
    admin_email = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[3]/nz-form-control/div/div/input')
    admin_email.send_keys(tenant_name_str + '@datagrand_test.com')
    time.sleep(1)
    # 分配许可
    rootCount = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[1]/div/div[2]/nz-form-control/div/div/input')
    rootCount.send_keys(1)
    time.sleep(1)
    studioCount = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[2]/div/div[2]/nz-form-control/div/div/input')
    studioCount.send_keys(1)
    time.sleep(1)
    expire = driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-form-item[4]/nz-form-item[3]/div/div[2]/nz-form-control/div/div/input')
    expire.send_keys(5)
    time.sleep(1)
    # 点击确定按钮
    tenant_submit_btn = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]')
    tenant_submit_btn.click()
    time.sleep(1)
    # 确认对话框
    tenant_confirm_btn = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button')
    tenant_confirm_btn.click()
    time.sleep(5)


def permission_menu(driver):
    # 继续“许可管理”
    permission_menu_btn = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[1]')
    permission_menu_btn.click()
    time.sleep(3)
    # 机器人列表
    robot_device_list = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-device-list/section/nz-card/div[2]/nz-tabset/nz-tabs-nav/div/div/div[1]/div')
    robot_device_list.click()
    time.sleep(2)
    # studio列表
    studio_device_list = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-device-list/section/nz-card/div[2]/nz-tabset/nz-tabs-nav/div/div/div[2]/div')
    studio_device_list.click()
    time.sleep(2)


def auditLog_menu(driver):
    # 审计日志
    auditLog_menu_btn = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[8]')
    auditLog_menu_btn.click()
    time.sleep(3)

    # 下拉选择范围
    select_menu = driver.find_element(By.XPATH,
                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-select/nz-select-top-control/nz-select-search/input')
    select_menu.click()
    time.sleep(1)
    option_item3 = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[3]/div')
    option_item3.click()
    time.sleep(1)
    # 点击导出按钮
    export_btn = driver.find_element(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/button')
    export_btn.click()
    time.sleep(3)
    # 选择“全部”
    select_menu2 = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-select/nz-select-top-control/nz-select-search/input')
    select_menu2.click()
    time.sleep(2)
    option_item1 = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div')
    option_item1.click()
    time.sleep(1)
    # 点击“日历组件
    # 开始时间
    # 通过jquery删除readonly属性或者改变readonly属性
    js = 'document.getElementsByTagName("input")[1].removeAttribute("readonly");'
    driver.execute_script(js)
    calerdate_input_begin = driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-range-picker/div/div[1]/input')
    time.sleep(1)
    calerdate_input_begin.send_keys("2021-04-01 12:00")

    time.sleep(1)
    calerdate_input_end = driver.find_element(By.XPATH,
                                              "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/rpa-time-range/div/nz-range-picker/div/div[3]/input")
    js2 = 'document.getElementsByTagName("input")[2].removeAttribute("readonly");'
    driver.execute_script(js2)
    calerdate_input_end.send_keys("2021-04-12 12:00")
    time.sleep(1)

    # 点击日历组件的确定按钮
    calendar_confirm_btn = driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div[3]/div/div/div/date-range-popup/div/div[2]/calendar-footer/div/ul/li/button')
    calendar_confirm_btn.click()
    time.sleep(1)

    # 点击导出按钮
    export_btn = driver.find_element(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/button')
    export_btn.click()
    time.sleep(3)

    # 点击搜索框
    auditLog_searchBox = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-audit-list/section/div/div/nz-input-group/input')
    auditLog_searchBox.clear()
    auditLog_searchBox.send_keys('登录')
    time.sleep(1)
    auditLog_searchBox.send_keys(Keys.ENTER)
    time.sleep(3)


def organization_menu(driver):
    # 组织架构
    organization_menu_btn = driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[3]')
    organization_menu_btn.click()
    time.sleep(3)

    # 新建个专门UIAuto的目录,UIAuto_DP。
    # 直接新建个测试目录
    org_add_subDepartment(driver, 'UIAuto_DP')
    # 先判断当前环境是否存在此目录,无则新建。
    departments_topDP = driver.find_elements(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/section/div/div/nz-tree/div[2]/div/div/nz-tree-node/nz-tree-node-title')
    # 使用遍历列表，找出对应的目录
    # 查找一下
    for x in departments_topDP:
        if x.get_attribute("title") == 'UIAuto_DP':
            # 直接开始右键功能
            ActionChains(driver).context_click(x).perform()
            time.sleep(3)

            # 获取第一项，新建子部门。
            right_menu_add = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[1]")
            right_menu_add.click()
            time.sleep(2)
            department_name_str = 'DP_' + str(random.randrange(1, 65535))
            org_add_subDepartment_contextClick(driver, department_name_str)

            # 右键第二项，编辑“部门”
            # 直接开始右键功能
            ActionChains(driver).context_click(x).perform()
            time.sleep(3)
            right_menu_editor = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[2]")
            right_menu_editor.click()
            time.sleep(2)
            org_add_subDepartment_contextClick(driver, department_name_str + '_edited')
            time.sleep(2)

            # 右键，第三项添加成员
            ActionChains(driver).context_click(x).perform()
            time.sleep(3)
            right_menu_addMember = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[3]")
            right_menu_addMember.click()
            time.sleep(4)
            first_account = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/label/span[1]/input')
            if first_account.is_selected() == True:
                continue
            else:
                first_account.click()
                time.sleep(1)
            add_member_confirmBtn = driver.find_element(By.XPATH,
                                                        '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]')
            add_member_confirmBtn.click()
            time.sleep(5)

            # 右键，第四项
            ActionChains(driver).context_click(x).perform()
            time.sleep(3)
            right_menu_deleteDP = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[4]")
            right_menu_deleteDP.click()
            time.sleep(3)
            # 会弹出确认提示对话框
            # org_deleteConfirmBtn=driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
            # org_deleteConfirmBtn.click()
            # time.sleep(5)
            org_deleteCancelBtn = driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[1]')
            org_deleteCancelBtn.click()
            time.sleep(5)
            # 先移除右侧的被添加成功的成员，然后再双击删除其子部门
            first_member = driver.find_element(By.XPATH,
                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/nz-card/div/div/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div[2]/table/tbody/tr[3]/td[4]/shared-actions/shared-action-item[2]/span[2]/a')
            first_member.click()  # 点击移除按钮
            time.sleep(2)
            # 点击确定提示按钮
            delete_member_confirmBtn = driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
            delete_member_confirmBtn.click()
            time.sleep(3)
            break  # 达成目的之后，不再继续遍历。


def org_add_subDepartment(driver, department_name_str):
    # 新建子部门
    add_department_btn = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/section/header/div[1]/button[1]')
    add_department_btn.click()
    time.sleep(1)
    # 组织名称
    # department_name_str='DP_'+str(random.randrange(1,65535))
    department_name = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/section/nz-form-item/nz-form-control/div/div/input')
    department_name.send_keys(department_name_str)
    time.sleep(1)
    # 配置组织权限
    any_role_authority = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/div/div/span[1]/label/span[1]/input')
    if any_role_authority.is_selected() == True:
        pass
    else:
        any_role_authority.click()
        time.sleep(1)
    organization_submit_btn = driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]')
    organization_submit_btn.click()
    time.sleep(5)


def org_add_subDepartment_contextClick(driver, department_name_str):
    # 填写表单

    # 组织名称
    # department_name_str='DP_'+str(random.randrange(1,65535))
    department_name = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/form/section/nz-form-item/nz-form-control/div/div/input')
    department_name.clear()
    department_name.send_keys(department_name_str)
    time.sleep(1)
    # 配置组织权限
    any_role_authority = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/div/div/span[1]/label/span[1]/input')
    if any_role_authority.is_selected() == True:
        pass
    else:
        any_role_authority.click()
        time.sleep(1)
    organization_submit_btn = driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[3]/button[2]')
    organization_submit_btn.click()
    time.sleep(5)


def robots_menu(driver):
    # 机器人模块
    robots_menu_btn = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[4]')
    robots_menu_btn.click()
    time.sleep(2)
    # 点击“查看作业”
    robots_list = driver.find_elements(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    if len(robots_list) == 0:
        pass
    else:  # 点击查看作业
        robot_first_lookjobs = driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
        robot_first_lookjobs.click()
        time.sleep(2)
        # 点击作业的查看日志
        # 先判断该机器人是否有作业列表
        # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]"
        job_list = driver.find_elements(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        if len(job_list) == 0:
            pass
        else:
            print(len(job_list))
            time.sleep(3)
            # 作业列表，查看日志。【万历环境，td是第10个，test环境第9个，因为存在“环境区别”情况，所以需要加异常处理。】
            job_list0_log = driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[9]/div/a')
            job_list0_log.click()  # 万历环境的xpath："/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[10]/div/a"
            time.sleep(2)
            # 关闭展示日志的窗口
            close_logDialog = driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
            close_logDialog.click()
            time.sleep(1)
            # 返回机器人列表
            back2robotList_href = driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
            back2robotList_href.click()
            time.sleep(2)
        # 点击“更多”
        robot_first_more = driver.find_element(By.XPATH,
                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
        # robot_first_more.click()
        # 点击，并且悬停在该位置
        ActionChains(driver).click(robot_first_more).move_to_element(robot_first_more).perform()
        update_robot = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div/div/ul/bixi-table-operations-group[2]/li')
        update_robot.click()
        time.sleep(5)
        # 填写robot的名称,为什么会定位不到呢？
        # robot_name_input=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-form-item/nz-form-control/div/div/input')
        #
        # robot_name_input.clear()
        # robot_name_input.send_keys('robot_updated')
        # time.sleep(1)
        # robotupdate_confirmBtn=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
        # robotupdate_confirmBtn.click()
        # time.sleep(1)

        # 点击搜索框
        robot_searchBox = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-robot-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
        robot_searchBox.clear()
        robot_searchBox.send_keys('robot')
        time.sleep(1)
        robot_searchBox.send_keys(Keys.ENTER)
        time.sleep(2)


def library_menu(driver):
    # 第三方库/库管理
    library_menu = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
    library_menu.click()
    time.sleep(2)


def applications_menu(driver):
    # 流程管理
    applications_menu = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[6]')
    applications_menu.click()
    time.sleep(2)
    # 流程列表
    applications_list = driver.find_elements(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    if len(applications_list) == 0:
        pass
    else:
        # 点击记录的“历史版本”对话框
        history_version = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[4]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
        history_version.click()
        time.sleep(2)
        # 点击关闭窗口 #"/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button"
        history_version_closeBtn = driver.find_element(By.XPATH,
                                                       '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
        history_version_closeBtn.click()
        time.sleep(2)
        # 点击“共享设置”
        sharing_setting = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[4]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
        sharing_setting.click()
        time.sleep(2)
        # 返回至流程列表
        back2_applicationsList = driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
        back2_applicationsList.click()
        time.sleep(2)
        # 流程搜索框
        applications_searchBox = driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/apps-app-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
        applications_searchBox.clear()
        applications_searchBox.send_keys('流程')
        time.sleep(1)
        applications_searchBox.send_keys(Keys.ENTER)
        time.sleep(2)


def jobs_menu(driver):
    # 作业管理
    jobs_menu = driver.find_element(By.XPATH,
                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[2]')
    jobs_menu.click()
    time.sleep(5)  # 为了防止网络较慢导致的加载问题，应该延长请求的响应时间
    # 选择作业范围，导出
    job_select = driver.find_element(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-select')
    job_select.click()
    time.sleep(1)
    # 点击“今天”范围
    item_today = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[3]')
    item_today.click()
    time.sleep(2)
    # 点击“导出按钮”
    jobs_expert_button = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/button')
    jobs_expert_button.click()
    time.sleep(3)
    # select选择“全部”范围
    job_select.click()
    time.sleep(3)
    item_all = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
    item_all.click()
    time.sleep(1)
    # 点击，日历的起始和终止范围<这里需要js辅助>
    # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[1]/input"
    js_start = 'document.getElementsByTagName("input")[0].removeAttribute("readonly");'
    js_end = 'document.getElementsByTagName("input")[1].removeAttribute("readonly");'
    driver.execute_script(js_start)
    driver.execute_script(js_end)

    calendar_start = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[1]/input')
    calendar_start.send_keys("2021-03-01 12:00")
    time.sleep(1)
    calendar_end = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[1]/rpa-time-range/div/nz-range-picker/div/div[3]/input')
    calendar_end.send_keys("2021-04-14 12:00")
    time.sleep(3)
    # 点击“确定”按钮
    calendar_end_confirmBtn = driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[3]/div/div/div/date-range-popup/div/div[2]/calendar-footer/div/ul/li/button')
    calendar_end_confirmBtn.click()
    time.sleep(1)
    jobs_expert_button.click()
    time.sleep(4)
    # 查看作业详情
    jobs_list = driver.find_elements(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr')
    if len(jobs_list) == 0:
        pass
    else:
        # 查看作业详情
        jobs_detail = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr[2]/td[11]/shared-actions/shared-action-item/span[2]/a')
        jobs_detail.click()
        time.sleep(1)
        # 关闭详细信息对话框
        jobs_detailDialog_closeBtn = driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
        jobs_detailDialog_closeBtn.click()
        time.sleep(1)
        # 点击“更多”
        jobs_more = driver.find_element(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/tbody/tr[2]/td[11]/shared-actions/shared-action-overlay/a')
        ActionChains(driver).click(jobs_more).move_to_element(jobs_more).perform()
        job_log = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/ul/li[1]')
        job_log.click()
        time.sleep(2)
        job_logDialog_closeBtn = driver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button")
        job_logDialog_closeBtn.click()
        time.sleep(2)

    # 点击列表的“状态”选择
    job_statusFilter = driver.find_element(By.XPATH,
                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-job-job-list/section/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/div/table/thead/tr/th[6]/nz-table-filter/nz-filter-trigger/span')
    job_statusFilter.click()
    time.sleep(2)

    status = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/ul/li')
    # print('status length:',len(status)) #"/html/body/div[2]/div[3]/div/div/div/ul/li[2]/label/span[1]/input"

    i = 1
    while (i < len(status) + 1):  # "/html/body/div[2]/div[3]/div/div/div/ul/li[1]"
        status_item_xpath = "/html/body/div[2]/div[3]/div/div/div/ul/li[" + str(i) + "]"
        print(status_item_xpath)
        status_item = driver.find_element(By.XPATH, status_item_xpath)
        status_item.click()
        time.sleep(2)
        # 点击确定按钮
        status_confirmBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
        status_confirmBtn.click()
        time.sleep(3)
        job_statusFilter.click()  # 点击“状态”
        time.sleep(2)
        i = i + 1
        # print('i',i)
    # 最后，点击下“重置”按钮
    status_resetBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[1]')
    status_resetBtn.click()
    time.sleep(2)


def task_menu(driver):
    """
    进入任务管理列表
    :param driver:
    :return:
    """
    tasksManagement.task_menu_btn(driver)
    # 新建任务
    # 新建，定时，选定机器人。
    tasksManagement.addTask_byTiming_selectRobot_Every(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_selectRobot_Daily(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_selectRobot_Weekly(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_selectRobot_Monthly(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_selectRobot_Once(driver)
    time.sleep(2)

    # 新建，定时，动态分配。
    tasksManagement.addTask_byTiming_dynamicAllocation_Every(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_dynamicAllocation_Daily(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_dynamicAllocation_Weekly(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_dynamicAllocation_Monthly(driver)
    time.sleep(2)
    tasksManagement.addTask_byTiming_dynamicAllocation_Once(driver)
    time.sleep(2)

    # 新建，手动触发。
    tasksManagement.addTask_byManualTrigger(driver)
    time.sleep(2)


def library_menu(driver):
    library_menu_Btn = driver.find_element(By.XPATH,
                                           '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[7]')
    library_menu_Btn.click()
    time.sleep(3)
    # 判断，列表是否有记录
    libs_list = driver.find_elements(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    print('libs_list length:', len(libs_list))
    if len(libs_list) == 0:
        print('no library can be used.')
    else:
        lib_first_versions = driver.find_element(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[7]/bixi-table-col-operations/bixi-col-operations-template/a')
        lib_first_versions.click()
        time.sleep(3)
        # 关闭“历史版本”窗口  #"/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button"
        version_dialog_closeBtn = driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[3]/div/nz-modal-container/div/div/button')
        version_dialog_closeBtn.click()
        time.sleep(2)
        # 搜索框
        library_searchBox = driver.find_element(By.XPATH,
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
        lib_type = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
        lib_type.click()
        time.sleep(1)
        # 可视化搜索库和代码流程库  #"/html/body/div[2]/div[3]/div/div/div/ul/li[1]/label/span[1]/input"
        lib_type_visualLibrary = driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div[3]/div/div/div/ul/li[1]/label/span[1]/input')
        lib_type_visualLibrary.click()
        time.sleep(1)
        # 点击确定按钮
        lib_type_confirmBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
        lib_type_confirmBtn.click()
        time.sleep(4)
        # 类型
        # lib_type=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-library-manage-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[2]/nz-table-filter/nz-filter-trigger/span')
        lib_type.click()
        time.sleep(1)
        # 可视化搜索库和代码流程库
        lib_type_codeLibrary = driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div[3]/div/div/div/ul/li[2]/label/span[1]/input')
        lib_type_codeLibrary.click()
        time.sleep(1)
        # 点击确定按钮
        lib_type_confirmBtn2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
        lib_type_confirmBtn2.click()
        time.sleep(4)

        lib_type.click()
        time.sleep(1)
        # 点击“重置按钮”                                 #"/html/body/div[2]/div[3]/div/div/div/div/button[1]"
        lib_type_resetBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[1]')
        lib_type_resetBtn.click()
        time.sleep(4)


def dataAssets_menu(driver):
    """
    数据资产模块
    :param driver:
    :return:
    """
    dataAssets_menu_btn = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[5]')
    dataAssets_menu_btn.click()
    time.sleep(3)
    # 新增数据资产
    add_data_assets_btn = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-asset-list/section/shared-list-search/div/div/div[1]/button')
    add_data_assets_btn.click()
    time.sleep(2)
    # 基本信息
    # 数据资产名称
    assets_name_input = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/div/nz-form-item[1]/nz-form-control/div/div/input')
    assets_name_input.clear()
    assets_name_str = 'asset_' + str(math.ceil(time.time())) + '_test'
    assets_name_input.send_keys(assets_name_str)
    time.sleep(1)
    # 类型
    asset_type_select = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/div/nz-form-item[2]/nz-select')
    asset_type_select.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(asset_type_select).perform()
    # 下拉框选择，此处选择“文本”item[2] #"/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[2]"
    item_text = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[2]')
    item_text.click()
    time.sleep(1)

    # 说明
    asset_explaination = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/nz-form-item/nz-form-control/div/div/textarea')
    asset_explaination.clear()
    asset_explaination.send_keys("this is asset test explaination.")
    time.sleep(1)
    # 全局值
    # 文本,除非robot指定了具体的值，否则将使用全局值。
    global_value_text = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[2]/div[2]/form/nz-form-item/nz-form-control/div/div/input')
    global_value_text.clear()
    global_value_text.send_keys("this_is_global_value")
    time.sleep(1)
    # 机器人定制值（开关按钮）
    # 该开关默认是“开启状态”，可以通过该button的class的状态识别是否是开启状态。（此处先不做处理）
    # 机器人定制值启用后，机器人使用列表中的值（若是机器人列表存在，则选择其一进行赋值）
    robot_addBtn = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/button')
    robot_addBtn.click()
    time.sleep(1)
    # 机器人
    # 点击“机器人下拉选择框”
    robot_select = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/nz-form-item[1]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    robot_select.click()
    ActionChains(driver).move_to_element(robot_select).perform()
    time.sleep(1)
    # 选择机器人
    robot_customized_select_list = driver.find_elements(By.XPATH,
                                                        '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
    print('robot_select_list length:', len(robot_customized_select_list))
    if len(robot_customized_select_list) == 0:
        print("no robot can be select or customized value.")
    else:  # 选择最上方的那一个
        robot_customized_item = driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
        robot_customized_item.click()
        time.sleep(1)
        # 文本
        robot_customized_item_text = driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/form/nz-form-item/nz-form-control/div/div/input')
        robot_customized_item_text.clear()
        robot_customized_item_text.send_keys(By.XPATH, "this is robot customized value.")
        time.sleep(1)
        # 确定按钮
        robot_customized_saveBtn = driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/nz-form-item[2]/nz-form-control/div/div/div/button[2]')
        robot_customized_saveBtn.click()
        time.sleep(1)
        # 取消按钮
    # 添加数据资产整体的确定按钮
    add_assets_confirmBtn = driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/footer/button[2]')
    add_assets_confirmBtn.click()
    time.sleep(3)
    # 整体的取消按钮
    # add_assets_cancelBtn=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/footer/button[1]')
    # add_assets_cancelBtn.click()
    # time.sleep(3)


def account_profile(driver):
    account = "gaoxiaoyan@datagrand.com"
    pwd_testEnv = 'Gaoxiaoyan9533'

    accountProfile.accountProfile_personalCenter(driver, account, pwd_testEnv, pwd_testEnv)
    accountProfile.accountProfile_setting(driver)
    # accountProfile.accountProfile_changeTenant(driver)
    back2TopLogMenu(driver)
    accountProfile.accountProfile_logout(driver)


def back2TopLogMenu(driver):
    # 点击“顶部菜单log”，回到数据监控大屏。
    data_monitor_scree = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[1]/img')
    data_monitor_scree.click()
    time.sleep(3)
    # driver.implicitly_wait()
    data_monitor_scree.is_selected()


def run(url, account, pwd):
    global driver  # 申明为全局变量
    driver = Chrome()
    login_test(driver, url, account, pwd)
    notification_menu(driver)
    # calendar_menu(driver)
    # role_menu(driver)
    # account_menu(driver)
    # organization_menu(driver)
    # robots_menu(driver)
    # library_menu(driver)
    # applications_menu(driver)
    # jobs_menu(driver)
    # tenant_menu(driver)
    # permission_menu(driver)
    # auditLog_menu(driver)
    # task_menu(driver)
    # library_menu(driver)
    # dataAssets_menu(driver)
    # account_center(driver)
    account_profile(driver)

    print("UI travel success!")



if __name__ == '__main__':
    account = "gaoxiaoyan@datagrand.com"
    url_testEnv = "http://rpa-test.datagrand.com"
    pwd_testEnv = 'Gaoxiaoyan9533'

    run(url_testEnv, account, pwd_testEnv)
