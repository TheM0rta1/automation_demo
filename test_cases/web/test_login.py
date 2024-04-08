import allure
import pytest
from data.login_data import LoginData


@allure.feature("登录功能")
@allure.description("登录界面功能测试")
class TestLogin(object):

    # 测试数据
    login_data = LoginData

    @pytest.mark.login
    @allure.story('登录成功测试')
    @allure.title('登录成功场景')
    @pytest.mark.parametrize('data', login_data.login_success_data)
    def test_login(self, open_url, data):
        login_page = open_url
        login_page.login(data["username"], data["password"], data["captcha_status"])
        actual = login_page.login_success()
        assert actual == data["expected"]

    @allure.story('登录失败测试')
    @allure.title('登录失败场景: 用户名/密码错误')
    @pytest.mark.parametrize('data', login_data.login_fail_data_username_password)
    def test_login_fail_username_password(self, open_url, data):
        login_page = open_url
        login_page.login(data["username"], data["password"], data["captcha_status"])
        actual = login_page.get_account_error_text()
        assert actual == data["expected"]

    @allure.story('登录失败测试')
    @allure.title('登录失败场景: 验证码错误')
    @pytest.mark.parametrize('data', login_data.login_fail_data_captcha)
    def test_login_fail_captcha(self, open_url, data):
        login_page = open_url
        login_page.login(data["username"], data["password"], data["captcha_status"])
        actual = login_page.get_captcha_error()
        assert actual == data["expected"]

    @allure.story('登录失败测试')
    @allure.title('登录失败场景: 用户名/密码/验证码为空')
    @pytest.mark.parametrize('data', login_data.login_none_data)
    def test_login_none(self, open_url, data):
        login_page = open_url
        login_page.login(data["username"], data["password"], data["captcha_status"])
        actual = login_page.get_common_none()
        assert actual == data["expected"]


if __name__ == '__main__':
    pytest.main()
