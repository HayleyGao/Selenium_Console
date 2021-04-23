import math
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def task_menu_btn(driver):
    """
    进入任务管理模块
    :param driver:
    :return:
    """
    # 任务管理
    time.sleep(4)
    task_menu = driver.find_element(By.XPATH,
                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[3]')
    task_menu.click()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[3]"
    time.sleep(4)


def addTask_byTiming_dynamicAllocation(driver):
    """
    新建任务，定时任务,动态分配
    前提条件：先判断机器人列表中至少有2个或以上个数的机器人。
    （新建任务，获取机器人列表的接口，和robot管理的列表接口是同一个。）
    :param driver:
    :return:
    """
    # #进入任务管理模块
    # task_menu_btn(driver)

    # 新增任务
    addTask_btn = driver.find_element(By.XPATH,
                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/shared-list-search/div/div/div[1]/button')
    addTask_btn.click()
    time.sleep(2)
    # 任务名称
    task_name = driver.find_element(By.XPATH,
                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[1]/nz-form-control/div/div/input")
    task_name.click()
    task_name.send_keys('task_' + str(math.ceil(time.time())) + '_dynamicAllocation')
    time.sleep(1)
    # 流程，先输入，然后选择下拉列表的第一个
    process_name = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[2]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    process_name.send_keys("编程")  # 以"编程"为关键字
    ActionChains(driver).move_to_element(process_name).perform()
    time.sleep(2)
    process_select_item = driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
    process_select_item.click()  # "/html/body/div[2]/div[2]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div"
    time.sleep(1)
    # 版本选择
    # 先点击下拉框
    version_select = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[3]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    version_select.click()
    ActionChains(driver).move_to_element(version_select).perform()
    time.sleep(1)

    # 选择最近的一项
    version_items = driver.find_elements(By.XPATH,
                                         '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
    # console的版本号是按照由最新的排序在最上方。
    print('len(version_items)', len(version_items))
    if len(version_items) == 1:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item")
        version_item.click()
        time.sleep(1)
    else:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div")
        version_item.click()
        time.sleep(1)

    # 选择机器人
    addtask_robotList = driver.find_elements(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    print('addtask_robotList length:', len(addtask_robotList))
    if len(addtask_robotList) == 0:
        print('no robot to add task.')
    else:
        if (len(addtask_robotList) == 1):
            print("只有一个机器人，也无法进行动态分配。")
        else:  # 添加前2个，动态分配3个。
            robot1 = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/label/span[1]/input')
            robot1.click()
            time.sleep(1)
            robot2 = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[2]/td[1]/label/span[1]/input')
            robot2.click()
            time.sleep(1)
    # 选择动态分配
    dynamic_allocation = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[1]/nz-form-control/div/div/nz-radio-group/div[2]/label/span[1]/input')
    dynamic_allocation.click()
    time.sleep(1)
    # 输入动态分配次数
    dynamic_allocation_input = driver.find_element(By.XPATH,
                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[1]/nz-form-control/div/div/nz-radio-group/div[2]/div/nz-form-control/div/div/input')
    time.sleep(1)
    dynamic_allocation_input.clear()
    dynamic_allocation_input.send_keys("3")
    time.sleep(1)

    # 这里设置个滚动吧
    # 由于下方选择日期时间的确定按钮被挡住，需要滚动下屏幕，需要js操作
    # main包含的范围有滚动条
    main_section_scroll = 'document.getElementsByTagName("main")[0].scrollTop=100;'
    driver.execute_script(main_section_scroll)
    time.sleep(1)


def addTask_byTiming_dynamicAllocation_Every(driver):
    """
    定时，动态分配，每隔
    :param driver:
    :return:
    """
    addTask_byTiming_dynamicAllocation(driver)
    addTask_byTiming_Every(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_dynamicAllocation_Daily(driver):
    """
    定时，动态分配，每天
    :param driver:
    :return:
    """
    addTask_byTiming_dynamicAllocation(driver)
    addTask_byTiming_Daily(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_dynamicAllocation_Weekly(driver):
    """
    定时，动态分配，每周
    :param driver:
    :return:
    """
    addTask_byTiming_dynamicAllocation(driver)
    addTask_byTiming_Weekly(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_dynamicAllocation_Monthly(driver):
    """
    定时，动态分配，每月
    :param driver:
    :return:
    """
    addTask_byTiming_dynamicAllocation(driver)
    addTask_byTiming_Mouthly(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_dynamicAllocation_Once(driver):
    """
    定时，动态分配，执行一次
    :param driver:
    :return:
    """
    addTask_byTiming_dynamicAllocation(driver)
    addTask_byTiming_Once(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_selectRobot(driver):
    """
    新增任务，定时，选定机器人
    定时，选定机器人、动态分配
    :param driver:
    :return:
    """
    # #进入任务管理模块
    # task_menu_btn(driver)

    # 新增任务
    addTask_btn = driver.find_element(By.XPATH,
                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/shared-list-search/div/div/div[1]/button')
    addTask_btn.click()
    time.sleep(2)
    # 任务名称
    task_name = driver.find_element(By.XPATH,
                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[1]/nz-form-control/div/div/input")
    task_name.click()
    task_name.send_keys('task_' + str(math.ceil(time.time())))
    time.sleep(1)
    # 流程，先输入，然后选择下拉列表的第一个
    process_name = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[2]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    process_name.send_keys("编程")  # 以"编程"为关键字
    ActionChains(driver).move_to_element(process_name).perform()
    time.sleep(2)
    process_select_item = driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
    process_select_item.click()  # "/html/body/div[2]/div[2]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div"
    time.sleep(1)
    # 版本选择
    # 先点击下拉框
    version_select = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[3]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    version_select.click()
    ActionChains(driver).move_to_element(version_select).perform()
    time.sleep(1)

    # 选择最近的一项
    version_items = driver.find_elements(By.XPATH,
                                         '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
    # console的版本号是按照由最新的排序在最上方。
    print('len(version_items)', len(version_items))
    if len(version_items) == 1:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item")
        version_item.click()
        time.sleep(1)
    else:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div")
        version_item.click()
        time.sleep(1)
    # 选择机器人
    # 先选择第一个
    robots_list = driver.find_elements(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    if len(robots_list) == 0:
        print("no robot to add task.")
        return
    else:
        first_robot = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/label/span[1]/input')
        first_robot.click()
        time.sleep(1)

    trigger_timing = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-trigger/section/div/section[1]/span[1]')
    trigger_timing.click()
    time.sleep(1)
    # 执行目标
    # 选定机器人
    select_robot = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[1]/nz-form-control/div/div/nz-radio-group/div[1]/label/span[1]/input')
    select_robot.click()
    time.sleep(1)
    # 由于下方选择日期时间的确定按钮被挡住，需要滚动下屏幕，需要js操作
    # main包含的范围有滚动条
    main_section_scroll = 'document.getElementsByTagName("main")[0].scrollTop=200;'
    driver.execute_script(main_section_scroll)
    time.sleep(2)


def addTask_byTiming_Every(driver):
    """
    前序步骤为新建任务
    #触发方式
    #定时，选定机器人，每隔
    :param driver:
    :return:
    """

    # 设置定时
    # 每隔
    every = driver.find_element(By.XPATH,
                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[1]/span[1]/input')
    every.click()
    # 开始执行时间
    js1 = 'document.getElementsByTagName("input")[18].removeAttribute("readonly");'
    js2 = 'document.getElementsByTagName("input")[19].removeAttribute("readonly");'
    driver.execute_script(js1)
    driver.execute_script(js2)
    time.sleep(1)
    # 获取当前日期 年、月、日,先直接给个时间试试。
    # 获取当前时间时、分
    execute_time_By_day = driver.find_element(By.XPATH,
                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/rpa-full-time/nz-date-picker/div/div/input')
    execute_time_By_day.clear()
    execute_time_By_day.send_keys("2021-04-16")
    time.sleep(1)
    execute_time_By_day.send_keys(Keys.ENTER)
    time.sleep(2)
    # #需要再点击下任何空白处（不会有影响的地方），使用发送回车enter按键替代。

    execute_time_By_second = driver.find_element(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/rpa-full-time/nz-time-picker/div/input')
    execute_time_By_second.clear()
    execute_time_By_second.send_keys("22:00")
    time.sleep(1)
    execute_time_By_second.send_keys(Keys.ENTER)
    time.sleep(2)
    # #点击时刻的确定按钮,使用发送回车enter按键替代。

    # 周期类型
    # 每隔*分
    every_by_Minutes_item = driver.find_element(By.XPATH,
                                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[2]/div/section/nz-radio-group/div[3]/nz-form-control/div/div/label/span[1]/input')
    every_by_Minutes_item.click()
    time.sleep(1)

    # 填写数目
    every_by_Minutes_input = driver.find_element(By.XPATH,
                                                 '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[2]/div/section/nz-radio-group/div[3]/nz-form-control/div/div/span/nz-input-number/div[2]/input')
    time.sleep(1)
    # every_by_Minutes_input.clear() #这里的clear()没有生效。那么，发送退格键试试。分钟的话，一般最多填写59，也就是2位数，所以，2个退格键足够了。
    every_by_Minutes_input.send_keys(Keys.BACKSPACE)
    every_by_Minutes_input.send_keys(Keys.BACKSPACE)
    every_by_Minutes_input_value = every_by_Minutes_input.get_attribute("value")
    print(every_by_Minutes_input_value)
    time.sleep(1)
    every_by_Minutes_input.send_keys('2')
    time.sleep(1)


def addTask_byTiming_Daily(driver):
    """
    前序步骤为新建任务
    #触发方式
    #定时，执行目标：选定机器人，每日重复。
    :param driver:
    :return:
    """
    # 设置定时
    # 每日重复
    daily = driver.find_element(By.XPATH,
                                '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[2]/span[1]/input')
    daily.click()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[2]/span[1]/input"
    time.sleep(1)
    # 单个周期内的执行时间
    executeTime_inSingleCycle = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/nz-time-picker/div/input')
    executeTime_inSingleCycle.clear()
    time.sleep(1)
    executeTime_inSingleCycle.send_keys("14:00")
    time.sleep(1)
    executeTime_inSingleCycle.send_keys(Keys.ENTER)
    time.sleep(2)


def addTask_byTiming_Weekly(driver):
    """
    前序步骤为新建任务
    #触发方式
    #定时，执行目标：选定机器人，每周重复。
    :param driver:
    :return:
    """
    # 设置定时
    # 每周重复
    mouthly = driver.find_element(By.XPATH,
                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[3]/span[1]/input')
    mouthly.click()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[3]/span[1]/input"
    time.sleep(1)
    # 单个周期内的执行时间
    executeTime_inSingleCycle = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/nz-time-picker/div/input')
    executeTime_inSingleCycle.clear()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/nz-time-picker/div/input"
    time.sleep(1)
    executeTime_inSingleCycle.send_keys("14:00")
    time.sleep(1)
    executeTime_inSingleCycle.send_keys(Keys.ENTER)
    time.sleep(1)
    # 周期日,目前全选。
    cycle_day = driver.find_elements(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[2]/div/nz-form-control/div/div/nz-checkbox-wrapper/div/div/label/span[1]/input')
    for x in cycle_day:
        x.click()
        time.sleep(1)


def addTask_byTiming_Mouthly(driver):
    """
    前序步骤为新建任务
    #触发方式
    #定时，执行目标：选定机器人，每月重复。
    :param driver:
    :return:
    """
    # 设置定时
    # 每月重复
    mouthly = driver.find_element(By.XPATH,
                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[4]/span[1]/input')
    mouthly.click()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[4]/span[1]/input"
    time.sleep(1)
    # 单个周期内的执行时间
    executeTime_inSingleCycle = driver.find_element(By.XPATH,
                                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/nz-time-picker/div/input')
    executeTime_inSingleCycle.clear()  # "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/nz-time-picker/div/input"
    time.sleep(1)
    executeTime_inSingleCycle.send_keys("14:00")
    time.sleep(1)
    executeTime_inSingleCycle.send_keys(Keys.ENTER)
    time.sleep(1)
    # 周期日,目前全选。
    cycle_day = driver.find_elements(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[2]/div/nz-form-control/div/div/nz-checkbox-wrapper/div/div/label/span[1]/input')
    for x in cycle_day:
        x.click()
        time.sleep(1)


def addTask_byTiming_Once(driver):
    """
    前序步骤为新建任务
    #触发方式
    #定时，执行目标：选定机器人，执行一次。
    :param driver:
    :return:
    """
    # 设置定时
    # 执行一次
    once = driver.find_element(By.XPATH,
                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[1]/nz-radio-group/label[5]/span[1]/input')
    once.click()
    time.sleep(1)
    # 开始执行时间
    start_ExecuteTime_byDay = driver.find_element(By.XPATH,
                                                  '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/rpa-full-time/nz-date-picker/div/div/input')
    start_ExecuteTime_byDay.clear()
    start_ExecuteTime_byDay.send_keys("2021-04-16")
    time.sleep(1)
    start_ExecuteTime_byDay.send_keys(Keys.ENTER)
    time.sleep(1)
    start_ExecuteTime_bySecond = driver.find_element(By.XPATH,
                                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-type/div/form/nz-form-item[2]/nz-form-control/div/div/div/div[2]/div[1]/nz-form-control/div/div/rpa-full-time/nz-time-picker/div/input')
    start_ExecuteTime_bySecond.clear()
    start_ExecuteTime_bySecond.send_keys("16:00")
    time.sleep(1)
    start_ExecuteTime_bySecond.send_keys(Keys.ENTER)
    time.sleep(1)


def addTask_byTiming_selectRobot_Every(driver):
    """
    定时，选定机器人，每隔
    :param driver:
    :return:
    """
    addTask_byTiming_selectRobot(driver)
    addTask_byTiming_Every(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_selectRobot_Daily(driver):
    """
    定时，选定机器人，每天
    :param driver:
    :return:
    """
    addTask_byTiming_selectRobot(driver)
    addTask_byTiming_Daily(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_selectRobot_Weekly(driver):
    """
    定时，选定机器人，每天
    :param driver:
    :return:
    """
    addTask_byTiming_selectRobot(driver)
    addTask_byTiming_Weekly(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_selectRobot_Monthly(driver):
    """
    定时，选定机器人，每天
    :param driver:
    :return:
    """
    addTask_byTiming_selectRobot(driver)
    addTask_byTiming_Mouthly(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byTiming_selectRobot_Once(driver):
    """
    定时，选定机器人，每天
    :param driver:
    :return:
    """
    addTask_byTiming_selectRobot(driver)
    addTask_byTiming_Once(driver)
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_byManualTrigger(driver):
    """
    前序步骤为新建任务
    #触发方式
    #手动
    :param driver:
    :return:
    """
    # 新增任务
    addTask_btn = driver.find_element(By.XPATH,
                                      '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/shared-list-search/div/div/div[1]/button')
    addTask_btn.click()
    time.sleep(2)
    # 任务名称
    task_name = driver.find_element(By.XPATH,
                                    "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[1]/nz-form-control/div/div/input")
    task_name.click()
    task_name.send_keys('task_' + str(math.ceil(time.time())))
    time.sleep(1)
    # 流程，先输入，然后选择下拉列表的第一个
    process_name = driver.find_element(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[2]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    process_name.send_keys("编程")  # 以"编程"为关键字
    ActionChains(driver).move_to_element(process_name).perform()
    time.sleep(2)
    process_select_item = driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]')
    process_select_item.click()  # "/html/body/div[2]/div[2]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div"
    time.sleep(1)
    # 版本选择
    # 先点击下拉框
    version_select = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-info/form/nz-form-item[3]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
    version_select.click()
    ActionChains(driver).move_to_element(version_select).perform()
    time.sleep(1)

    # 选择最近的一项
    version_items = driver.find_elements(By.XPATH,
                                         '/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
    # console的版本号是按照由最新的排序在最上方。
    print('len(version_items)', len(version_items))
    if len(version_items) == 1:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item")
        version_item.click()
        time.sleep(1)
    else:
        version_item = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div")
        version_item.click()
        time.sleep(1)
    # 选择机器人
    # 先选择第一个
    robots_list = driver.find_elements(By.XPATH,
                                       '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    if len(robots_list) == 0:
        print("no robot to add task.")
        return
    else:
        first_robot = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[1]/rpa-edit-task-robots/div/nz-form-item/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]/label/span[1]/input')
        first_robot.click()
        time.sleep(1)

    # 选择触发方式
    trigger_manual = driver.find_element(By.XPATH,
                                         '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-trigger/section/div/section[2]/span[2]')
    trigger_manual.click()
    time.sleep(1)

    # 执行作业前，手动配置输入参数
    setup_argumentsManually_beforeRuning_Btn = driver.find_element(By.XPATH,
                                                                   '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/div[1]/nz-switch/button')
    setup_argumentsManually_beforeRuning_Btn.click()
    time.sleep(2)
    # 其它三个开关按钮
    addTask_notification_switchBtn(driver)
    addTask_submit_confirmBtn(driver)


def addTask_submit_confirmBtn(driver):
    """
    新增作业，最后提交步骤的确定按钮
    :param driver:
    :return:
    """
    # 点击“确定”按钮
    addTask_confirmBtn = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/footer/button[2]')
    addTask_confirmBtn.click()
    time.sleep(3)


def addTask_notification_switchBtn(driver):
    """
    新建任务，无论是定时或手动，公共区域的三个开关式按钮。
    :param driver:
    :return:
    """
    # 作业执行中，录制计算机屏幕，开关按钮
    record_screen_during_running_job_btn = driver.find_element(By.XPATH,
                                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-recording/form/nz-form-item[1]/nz-form-control/div/div/nz-switch/button')
    record_screen_during_running_job_btn.click()
    time.sleep(1)
    # 作业异常时，截屏开关按钮
    capture_screen_when_job_abnormal_btn = driver.find_element(By.XPATH,
                                                               '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-recording/form/nz-form-item[2]/nz-form-control/div/div/nz-switch/button')
    capture_screen_when_job_abnormal_btn.click()
    time.sleep(2)
    # 作业异常时，短信通知开关
    notificateSMS_when_job_abnormal_btn = driver.find_element(By.XPATH,
                                                              '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-recording/form/nz-form-item[3]/nz-form-control/div/div/nz-switch/button')
    notificateSMS_when_job_abnormal_btn.click()
    time.sleep(1)
    # 若是开启了短信通知设置，需要输入接收短信的号码
    smsReceiver_input = driver.find_element(By.XPATH,
                                            '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-create-task/div/nz-spin/div/main/div[2]/rpa-edit-task-recording/form/nz-form-item[3]/nz-form-control/div/div/nz-form-control/div/div/input')
    smsReceiver_input.clear()
    smsReceiver_input.send_keys("19925865728")  # 11位,这里有手机号输入校验。
    time.sleep(1)


def task_searchBox(driver):
    # task_menu_btn(driver)
    # 任务管理搜索框，输入任务名称搜索
    taskName_searchBox = driver.find_element(By.XPATH,
                                             "/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/shared-list-search/div/div/div[2]/nz-input-group/input")
    taskName_searchBox.clear()
    taskName_searchBox.send_keys("task")
    taskName_searchBox.send_keys(Keys.ENTER)
    time.sleep(4)
    taskName_searchBox.clear()
    taskName_searchBox.send_keys(Keys.ENTER)
    time.sleep(4)


def task_list(driver):
    # task_menu_btn(driver)
    # 任务列表状态
    task_status_btn = driver.find_element(By.XPATH,
                                          '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr/th[7]/nz-table-filter/nz-filter-trigger/span')
    task_status_btn.click()
    ActionChains(driver).move_to_element(task_status_btn).perform()
    task_status_list = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/ul/li/label/span[1]/input')
    print(len(task_status_list))
    i = 1
    for x in task_status_list:  # "/html/body/div[2]/div[3]/div/div/div/ul/li[1]/label/span[1]/input"
        task_status_xpath = '/html/body/div[2]/div[3]/div/div/div/ul/li[' + str(i) + ']/label/span[1]/input'
        print(task_status_xpath)
        status = driver.find_element(By.XPATH, task_status_xpath)
        status.click()
        time.sleep(1)
        status_confirmBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[2]')
        status_confirmBtn.click()
        time.sleep(3)
        i = i + 1
        task_status_btn.click()
        time.sleep(1)
    # 最后，再重置一下
    status_resetBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button[1]')
    status_resetBtn.click()
    time.sleep(3)

    # 检查下作业列表是否为空，不为空，可以进行“操作”
    task_list = driver.find_elements(By.XPATH,
                                     '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr')
    print('task_list length:', len(task_list))
    if len(task_list) == 0:
        print("任务列表为空")
    else:
        # 操作-查看作业
        view_jobs = driver.find_element(By.XPATH,
                                        '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[1]')
        view_jobs.click()
        time.sleep(3)
        # 返回任务列表
        back2_taskList = driver.find_element(By.XPATH,
                                             '/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
        back2_taskList.click()  # "/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a"
        time.sleep(3)

        # 操作-更多
        # task_more=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
        # task_more.click()
        # ActionChains(driver).move_to_element(task_more).perform()
        # time.sleep(1)
        # task_more_list=driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div/ul/bixi-table-operations-group/li')
        # print('task_more_list length:',len(task_more_list))
        # k=1
        # for x in task_more_list:#"/html/body/div[2]/div/div/div/ul/bixi-table-operations-group[2]/li"
        #     more_item_xpath='/html/body/div[2]/div/div/div/ul/bixi-table-operations-group['+str(k)+']/li'
        #     print(more_item_xpath)
        #     more_item=driver.find_element(By.XPATH,more_item_xpath)
        #     more_item.click()
        #     time.sleep(2)
        #     #返回任务列表
        #     back2_taskList2=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/bixi-layout-header/div[2]/div[1]/div/span[1]/a')
        #     back2_taskList2.click()
        #     time.sleep(3)
        #     k=k+1
        #     #继续点击“更多”
        #     task_more2=driver.find_element(By.XPATH,'/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-content/rpa-task-list/section/div/bixi-table/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[8]/bixi-table-col-operations/bixi-col-operations-template/a[2]')
        #     task_more2.click()
        #     ActionChains(driver).move_to_element(task_more2).perform()
        #     time.sleep(1)

    # 任务列表，滚动条滚动,滚动到底部。
    consoleJS_scrollTop = 'document.getElementsByClassName("bixi-layout-content ng-star-inserted")[0].scrollTop=10000;'
    driver.execute_script(consoleJS_scrollTop)
    time.sleep(1)
    # 分页管理
    # 总共记录条数
    # 总共页数、当前页数、跳转到指定页数、分页记录条数的指定


def task_menu(driver):
    # 任务管理
    time.sleep(2)
    task_menu = driver.find_element(By.XPATH,
                                    '/html/body/rpa-root/layout-default/bixi-layout/div/bixi-layout-menu/ul/li[3]')
    task_menu.click()
    time.sleep(4)

    # 添加自动触发方式
    # addTask_byTiming_Every(driver)
    # time.sleep(2)
    # addTask_byTiming_Daily(driver)
    # time.sleep(2)
    # addTask_byTiming_Weekly(driver)
    # time.sleep(2)
    # addTask_byTiming_Mouthly(driver)
    # time.sleep(2)
    # addTask_byTiming_Once(driver)
    # time.sleep(2)
    # addTask_byTiming_DynamicAllocation(driver)
    # time.sleep(2)
    # addTask_byManualTrigger(driver)
    # time.sleep(2)
    # addTask_byTiming_selectRobot_Every(driver)
    # time.sleep(2)
    # addTask_byTiming_dynamicAllocation_Every(driver)
    # time.sleep(2)
    task_menu(driver)
    print("UI travel success!")


if __name__ == '__main__':
    account = "gaoxiaoyan@datagrand.com"
    url_testEnv = "http://rpa-test.datagrand.com"
    pwd_testEnv = 'Gaoxiaoyan9533'
