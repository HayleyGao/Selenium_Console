import random
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class organizationPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def organization_menu(self):
        # 组织架构
        organization_menu_btn = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[3]')
        organization_menu_btn.click()
        time.sleep(3)

        # 新建个专门UIAuto的目录,UIAuto_DP。
        # 直接新建个测试目录
        self.org_add_subDepartment('UIAuto_DP')
        # 先判断当前环境是否存在此目录,无则新建。
        departments_topDP = self.driver.find_elements(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/section/div/div/nz-tree/div[2]/div/div/nz-tree-node/nz-tree-node-title')
        # 使用遍历列表，找出对应的目录
        # 查找一下
        for x in departments_topDP:
            if x.get_attribute("title") == 'UIAuto_DP':
                # 直接开始右键功能
                ActionChains(self.driver).context_click(x).perform()
                time.sleep(3)

                # 获取第一项，新建子部门。
                right_menu_add = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[1]")
                right_menu_add.click()
                time.sleep(2)
                department_name_str = 'DP_' + str(random.randrange(1, 65535))
                self.org_add_subDepartment_contextClick(department_name_str)

                # 右键第二项，编辑“部门”
                # 直接开始右键功能
                ActionChains(self.driver).context_click(x).perform()
                time.sleep(3)
                right_menu_editor = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[2]")
                right_menu_editor.click()
                time.sleep(2)
                self.org_add_subDepartment_contextClick(department_name_str + '_edited')
                time.sleep(2)

                # 右键，第三项添加成员
                ActionChains(self.driver).context_click(x).perform()
                time.sleep(3)
                right_menu_addMember = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[3]")
                right_menu_addMember.click()
                time.sleep(4)
                first_account = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/label/span[1]/input')
                if first_account.is_selected() == True:
                    continue
                else:
                    first_account.click()
                    time.sleep(1)
                add_member_confirmBtn = self.driver.find_element(By.XPATH,
                                                                 '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
                add_member_confirmBtn.click()
                time.sleep(5)

                # 右键，第四项
                ActionChains(self.driver).context_click(x).perform()
                time.sleep(3)
                right_menu_deleteDP = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[4]")
                right_menu_deleteDP.click()
                time.sleep(3)
                # 会弹出确认提示对话框
                # org_deleteConfirmBtn=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
                # org_deleteConfirmBtn.click()
                # time.sleep(5)
                org_deleteCancelBtn = self.driver.find_element(By.XPATH,
                                                               '/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[1]')
                org_deleteCancelBtn.click()
                time.sleep(5)
                # 先移除右侧的被添加成功的成员，然后再双击删除其子部门
                first_member = self.driver.find_element(By.XPATH,
                                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/nz-card/div/div/div[2]/nz-table/nz-spin/div/div/nz-table-inner-scroll/div[2]/table/tbody/tr[3]/td[4]/shared-actions/shared-action-item[2]/span[2]/a')
                first_member.click()  # 点击移除按钮
                time.sleep(2)
                # 点击确定提示按钮
                delete_member_confirmBtn = self.driver.find_element(By.XPATH,
                                                                    '/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
                delete_member_confirmBtn.click()
                time.sleep(3)
                break  # 达成目的之后，不再继续遍历。

    def org_add_subDepartment(self, department_name_str):
        # 新建子部门
        add_department_btn = self.driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-department-list/section/main/section/header/div[1]/button[1]')
        add_department_btn.click()
        time.sleep(1)
        # 组织名称
        # department_name_str='DP_'+str(random.randrange(1,65535))
        department_name = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/section/nz-form-item/nz-form-control/div/div/input')
        department_name.send_keys(department_name_str)
        time.sleep(1)
        # 配置组织权限
        any_role_authority = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/div/div/span[1]/label/span[1]/input')
        if any_role_authority.is_selected() == True:
            pass
        else:
            any_role_authority.click()
            time.sleep(1)
        organization_submit_btn = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
        organization_submit_btn.click()
        time.sleep(5)

    def org_add_subDepartment_contextClick(self, department_name_str):
        # 填写表单

        # 组织名称
        # department_name_str='DP_'+str(random.randrange(1,65535))
        department_name = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/form/section/nz-form-item/nz-form-control/div/div/input')
        department_name.clear()
        department_name.send_keys(department_name_str)
        time.sleep(1)
        # 配置组织权限
        any_role_authority = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/div/div/span[1]/label/span[1]/input')
        if any_role_authority.is_selected() == True:
            pass
        else:
            any_role_authority.click()
            time.sleep(1)
        organization_submit_btn = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]')
        organization_submit_btn.click()
        time.sleep(5)
