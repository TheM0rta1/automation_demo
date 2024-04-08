import requests
import re
from time import sleep
from page.base_page import BasePage
from utils.parseConFile import ParseConFile
from selenium import webdriver
from utils.keyboard import KeyBoard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage(BasePage):

    do_conf = ParseConFile()

    login_url = do_conf.get_config_data("LoginAccount", "login_url")
    username = do_conf.get_config_data("LoginPageElements", "username")
    password = do_conf.get_config_data("LoginPageElements", "password")
    captcha = do_conf.get_config_data("LoginPageElements", "captcha")
    login_btn = do_conf.get_config_data("LoginPageElements", "login_btn")

    captcha_img = do_conf.get_config_data("LoginPageElements", "captcha_img")
    get_captcha_inf = do_conf.get_config_data("LoginPageElements", "get_captcha_inf")

    common_error_alert = do_conf.get_config_data("LoginPageElements", "common_error_alert")
    common_none = do_conf.get_config_data("LoginPageElements", "common_none")

    login_success_info = do_conf.get_config_data("HomePageElements", "avatar")

    def login(self, username, password, captcha_status):
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.input_captcha(captcha_status)
        self.click_login_btn()

    def get_captcha(self):
        captcha = self.get_element_text(*LoginPage.captcha_img, 'src', model='验证码链接')
        uuid = re.findall(r'=([^&=]+)', captcha)[0]
        params = {"uuid": uuid}
        response = requests.get(self.get_captcha_inf, params=params)
        captcha_code = response.json()['captcha']
        return captcha_code

    def open_url(self):
        """加载登录页面"""
        self.logger.info("===打开URL===")
        return self.load_url(LoginPage.login_url)

    def click_username(self, username):
        """点击用户名输入框"""
        self.wait_element_to_be_located(*LoginPage.username, model='用户名框')
        return self.click(*LoginPage.username, username, model='用户名框')

    def input_username(self, username):
        """输入用户名"""
        self.wait_element_to_be_located(*LoginPage.username, model='用户名框')
        return self.send_keys(*LoginPage.username, username, model='用户名框')

    def click_password(self, password):
        """点击密码输入框"""
        self.wait_element_to_be_located(*LoginPage.password, model='密码框')
        return self.click(*LoginPage.password, password, model='密码框')

    def input_password(self, password):
        """输入密码"""
        self.wait_element_to_be_located(*LoginPage.password, model='密码框')
        return self.send_keys(*LoginPage.password, password, model='密码框')

    def click_captcha(self):
        """点击验证码输入框"""
        return self.click(*LoginPage.captcha, self.get_captcha(), model='验证码框')

    def input_captcha(self, captcha_status):
        """输入验证码"""
        if captcha_status == 1:
            return self.send_keys(*LoginPage.captcha, self.get_captcha(), model='验证码框')
        elif captcha_status == 0:
            return self.send_keys(*LoginPage.captcha, '00000', model='验证码框')
        else:
            return self.send_keys(*LoginPage.captcha, '', model='验证码框')

    def click_login_btn(self):
        """点击登录按钮"""
        self.wait_element_to_be_located(*LoginPage.login_btn, model='登录按钮')
        return self.click(*LoginPage.login_btn, model='登录按钮')

    def login_success(self):
        """获取登录成功的信息"""
        self.wait_element_to_be_located(*LoginPage.login_success_info, model='用户头像')
        return self.is_element_exist(*LoginPage.login_success_info, model='用户头像')

    def get_account_error_text(self):
        """用户名或密码错误提示信息"""
        self.logger.info("===获取用户名或密码错误提示信息===")
        return self.get_element_text(*LoginPage.common_error_alert, model='用户名或密码错误的提示信息')

    def get_captcha_error(self):
        """验证码错误提示信息"""
        self.logger.info("===获取验证码错误提示信息===")
        return self.get_element_text(*LoginPage.common_error_alert, model='验证码错误的提示信息')

    def get_common_none(self):
        """用户名/密码/验证码为空提示信息"""
        self.logger.info("===获取用户名/密码/验证码为空提示信息===")
        return self.get_elements_text(*LoginPage.common_none, model='用户名/密码/验证码为空的提示信息')


if __name__ == '__main__':
    pass
    # login_page = LoginPage(driver)
    # captcha = login_page.get_element_text(*LoginPage.captcha_img, 'src', model='验证码图片')
    # uuid = re.findall(r'=([^&=]+)', captcha)[0]
    # params = {"uuid": uuid}
    # response = requests.get(login_page.get_captcha_inf, params=params)
    # captcha_code = response.json()['captcha']
    # print(captcha_code)
