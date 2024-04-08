import allure
import pytest
from selenium import webdriver

driver = None


# 测试失败时添加截图
def allure_screenshot():
    # 添加allure失败截图
    allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# 设置为session，全部用例执行一次
@pytest.fixture(scope='session')
def driver():
    global driver
    print('------------open browser------------')
    chromeOptions = webdriver.ChromeOptions()
    # 设定下载文件的保存目录，
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": "D:\\testDownload"}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument("--ignore-certificate-errors")
    # chromeOptions.add_argument('--disable-gpu')
    chromeOptions.add_argument('--unlimited-storage')
    driver = webdriver.Chrome(options=chromeOptions)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(10)

    yield driver
    print('------------close browser------------')
    driver.quit()
