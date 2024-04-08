import os
import pytest
import config.conf

if __name__ == '__main__':
    # 当前时间
    now_time = config.conf.CURRENT_TIME
    # allure 测试报告路径
    cur_path = config.conf.cur_path
    report_path = os.path.join(cur_path, f'..\\reports\\{now_time}')
    # -s : 打印信息
    # -m ：运行含标签的用例
    # 指定某一模块的测试用例执行，例如：'./test_cases/test_login.py'
    pytest.main(['./test_cases/web/test_add_new_brand.py', "--alluredir", report_path])
    # 解析测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")
