import time

def get_current_time():
    """
    返回当前时间
    :return:
    """
    timestamp=time.time()#获取当前时间戳
    print(timestamp)


def get_currentTime_fromat():
    timestamp = time.time()  # 获取当前时间戳
    time_format=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp))
    print(time_format)
    return time_format


if __name__=="__main__":
    #get_current_time()
    get_currentTime_fromat()



