import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.keys import Keys

class rolesPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver


    def role_list_btn(self):
        role_menu_btn = self.driver.find_element(By.XPATH,
                                                 "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[9]/div[2]/ul/li[5]")
        return  role_menu_btn


    def role_list(self):
        # 进入“角色管理”模块
        self.role_list_btn().click()
        time.sleep(2)

    def add_new_role_btn(self):
        add_role_btn = self.driver.find_element(By.XPATH,
                                                "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/shared-list-search/div/div/div[1]/button")
        return add_role_btn

    def add_new_role(self,role_name_str):
        # 新增角色
        self.add_new_role_btn().click()
        time.sleep(3)
        #新增角色表单填写
        #role_name_str="role_" + str(math.ceil(time.time()))
        self.add_new_role_form(role_name_str)


    def add_new_role_form(self,role_name_str):

        # 填写角色名称
        role_name = self.driver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/nz-spin/div/form/nz-form-item/nz-form-control/div/div/input")

        #role_name_str="role_" + str(math.ceil(time.time()))
        role_name.send_keys(role_name_str)
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

    def isRolelistEmpty(self):
        """
        判断角色列表是否为空。
        (一般的角色列表都会有个默认的“租户管理员”角色是部署包默认生成的。)
        :return:
        """
        #len==1的时候分为2中情况：1、空态图显示占据了一个tr 2、正常的数据显示占据了一行。
        role_list = self.driver.find_elements(By.XPATH,
                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
        print('role_list length:', len(role_list))


        if len(role_list) == 1:
            try:
                #空态图
                empty_graph_locator=(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr/td/nz-embed-empty/nz-empty/p')
                empty_graph=WebDriverWait(self.driver,5).until(EC.presence_of_element_located(empty_graph_locator))
                #empty_graph_text=empty_graph.get_attribute("innerText")
                return True
            except:
                return False
        else:
            return False

    def getFirstRecordName(self):
        """
        获取列表最前一条记录的name项。
        :return:
        """
        if self.isRolelistEmpty()==False:
            role_first_record_name=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/bixi-table-col-text/div/span')
            role_first_record_name_text=role_first_record_name.get_attribute("innerText")
            print('role_first_record_name_text',role_first_record_name_text)
            return role_first_record_name_text
        else:
            return None

    def role_delete(self):
        """
        获取列表最上方的一条记录进行删除操作，遇到“租户管理员”的角色时选择什么都不做。
        :return:
        """
        #先判断列表是否为空
        if self.isRolelistEmpty()==False:
            delete_btn=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[3]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
            delete_btn.click()
            time.sleep(2)
            #确认框操作，div弹窗
            confirm_btn=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]')
            confirm_btn.click()                         #"/html/body/div[2]/div[2]/div/nz-modal-confirm-container/div/div/div/div/div[2]/button[2]"
            time.sleep(3)
            return True
        else:
            return False

    def searchBox(self):
        searchBox=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/settings-role-list/section/shared-list-search/div/div/div[2]/nz-input-group/input')
        return searchBox

    def search(self,search_str):
        """
        搜索框功能
        :param search_str:
        :return:
        """
        self.searchBox().clear()
        time.sleep(1)
        self.searchBox().send_keys(search_str)
        time.sleep(1)
        self.searchBox().send_keys(Keys.ENTER)
        time.sleep(2)


