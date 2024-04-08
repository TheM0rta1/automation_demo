import pytest
from utils.parseConFile import ParseConFile
from page.login_page import LoginPage
from page.brand_page import BrandPage
do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
username = do_conf.get_config_data('LoginAccount', 'username')
password = do_conf.get_config_data('LoginAccount', 'password')
captcha_status = 1


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    brand_page = BrandPage(driver)
    yield driver, login_page, brand_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    # login_page.open_url()
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page, brand_page = ini_pages
    login_page.login(username, password, captcha_status)
    yield login_page, brand_page
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()
