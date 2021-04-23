import logging


def logger():
    # logger = logging.getLogger("RPA_Console") #"RPA_Console",这里就是日志器名称。
    logger = logging.getLogger(__name__)  # __name__,运行文件的名称
    logger.setLevel(logging.DEBUG)  # 这里，控制整体的日志输出等级。无论其余的handler写任何等级都不影响。

    # 添加前进行判断是否已经有handler,防止日志重复输出。
    if not logger.handlers:  # logger对象含有handlers的list.
        # 创建 handler 输出到文件

        # handler = logging.FileHandler("my.log")
        log_path = r"C:\Users\caiwenjie\PycharmProjects\selenium_demo\RPA_Console_testEnv\log\my.log"
        handler = logging.FileHandler(log_path)
        handler.setLevel(logging.DEBUG)

        # handler 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建 logging format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  # (name,日志器名称)
        handler.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)
        logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    logger().info("hello, guoweikuang")
    logger().debug("print to debug")
    logger().error("error logging")
    logger().warning("warning logging")
    logger().critical("critical logging")
