import os
import time
import unittest

from RPA_Console_testEnv.lib.HTMLTestRunner import HTMLTestRunner

# 测试套件的执行
# 指定路径
test_dir = os.getcwd() + os.sep + 'test_case'
pattern = 'test*.py'  # 这里是字符串匹配
print(os.path.join(test_dir, pattern))
# 构建套件suite
suite = unittest.TestLoader().discover(test_dir, pattern)

if __name__ == "__main__":
    # 定义测试报告文件路径
    current_dir = os.path.dirname(os.path.realpath(__file__))
    report_dir = r"\report"
    now = time.strftime("%Y%m%d-%H%M%S")  # "%Y:%m:%d-%H%M%S"，不要加：，否则不符合文件命名规则。
    report_name = current_dir + report_dir + os.sep + now + "_report.html"

    with open(report_name, 'wb') as fp:
        runner = HTMLTestRunner(fp, verbosity=2, title='RPA_Console_Test')
        runner.run(suite)

