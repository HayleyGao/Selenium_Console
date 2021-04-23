import math
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class dataAssetPage:
    def __init__(self, driver):
        """
        构造函数，需要driver参数。
        :param driver:
        """
        self.driver = driver

    def dataAssets_menu(self):
        """
        数据资产模块
        :param driver:
        :return:
        """
        dataAssets_menu_btn = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[5]')
        dataAssets_menu_btn.click()
        time.sleep(3)
        # 新增数据资产
        add_data_assets_btn = self.driver.find_element(By.XPATH,
                                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-asset-list/section/shared-list-search/div/div/div[1]/button')
        add_data_assets_btn.click()
        time.sleep(2)
        # 基本信息
        # 数据资产名称
        assets_name_input = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/div/nz-form-item[1]/nz-form-control/div/div/input')
        assets_name_input.clear()
        assets_name_str = 'asset_' + str(math.ceil(time.time())) + '_test'
        assets_name_input.send_keys(assets_name_str)
        time.sleep(1)
        # 类型
        asset_type_select = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/div/nz-form-item[2]/nz-select')
        asset_type_select.click()
        time.sleep(1)
        ActionChains(self.driver).move_to_element(asset_type_select).perform()
        # 下拉框选择，此处选择“文本”item[2] #"/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[2]"
        item_text = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[2]')
        item_text.click()
        time.sleep(1)

        # 说明
        asset_explaination = self.driver.find_element(By.XPATH,
                                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[1]/div[2]/form/nz-form-item/nz-form-control/div/div/textarea')
        asset_explaination.clear()
        asset_explaination.send_keys("this is asset test explaination.")
        time.sleep(1)
        # 全局值
        # 文本,除非robot指定了具体的值，否则将使用全局值。
        global_value_text = self.driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[2]/div[2]/form/nz-form-item/nz-form-control/div/div/input')
        global_value_text.clear()
        global_value_text.send_keys("this_is_global_value")
        time.sleep(1)
        # 机器人定制值（开关按钮）
        # 该开关默认是“开启状态”，可以通过该button的class的状态识别是否是开启状态。（此处先不做处理）
        # 机器人定制值启用后，机器人使用列表中的值（若是机器人列表存在，则选择其一进行赋值）
        robot_addBtn = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/button')
        robot_addBtn.click()
        time.sleep(1)
        # 机器人
        # 点击“机器人下拉选择框”
        robot_select = self.driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/nz-form-item[1]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
        robot_select.click()
        ActionChains(self.driver).move_to_element(robot_select).perform()
        time.sleep(1)
        # 选择机器人
        robot_customized_select_list = self.driver.find_elements(By.XPATH,
                                                                 '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
        print('robot_select_list length:', len(robot_customized_select_list))
        if len(robot_customized_select_list) == 0:
            print("no robot can be select or customized value.")
        else:  # 选择最上方的那一个
            robot_customized_item = self.driver.find_element(By.XPATH,
                                                             '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
            robot_customized_item.click()
            time.sleep(1)
            # 文本
            robot_customized_item_text = self.driver.find_element(By.XPATH,
                                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/form/nz-form-item/nz-form-control/div/div/input')
            robot_customized_item_text.clear()
            robot_customized_item_text.send_keys(By.XPATH, "this is robot customized value.")
            time.sleep(1)
            # 确定按钮
            robot_customized_saveBtn = self.driver.find_element(By.XPATH,
                                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/section/div/section[3]/div[2]/asset-edit-robot-asset/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td/form/nz-form-item[2]/nz-form-control/div/div/div/button[2]')
            robot_customized_saveBtn.click()
            time.sleep(1)
            # 取消按钮
        # 添加数据资产整体的确定按钮
        add_assets_confirmBtn = self.driver.find_element(By.XPATH,
                                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/footer/button[2]')
        add_assets_confirmBtn.click()
        time.sleep(3)
        # 整体的取消按钮
        # add_assets_cancelBtn=self.driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/asset-aseet-edit/main/footer/button[1]')
        # add_assets_cancelBtn.click()
        # time.sleep(3)
