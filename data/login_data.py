class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        {
            "case": "用户名正确, 密码正确",
            "username": "admin",
            "password": "admin",
            "captcha_status": 1,
            "expected": True
        }
    ]

    #   登录失败
    login_fail_data_username_password = [
        {
            "case": "用户名正确, 密码错误, 验证码正确",
            "username": "admin",
            "password": "admin123",
            "captcha_status": 1,
            "expected": "账号或密码不正确"
        },
        {
            "case": "用户名错误, 密码正确, 验证码正确",
            "username": "admin123",
            "password": "admin",
            "captcha_status": 1,
            "expected": "账号或密码不正确"
        },
        {
            "case": "用户名错误, 密码错误, 验证码正确",
            "username": "admin123",
            "password": "admin123",
            "captcha_status": 1,
            "expected": "账号或密码不正确"
        },
    ]

    login_fail_data_captcha = [
        {
            "case": "用户名正确, 密码正确, 验证码错误",
            "username": "admin",
            "password": "admin",
            "captcha_status": 0,
            "expected": "验证码不正确"
        },
        {
            "case": "用户名错误, 密码错误, 验证码错误",
            "username": "admin123",
            "password": "admin123",
            "captcha_status": 0,
            "expected": "验证码不正确"
        },
    ]

    #   用户名、密码都为空
    login_none_data = [
        {
            "case": "用户名为空, 密码为空, 验证码为空",
            "username": "",
            "password": "",
            "captcha_status": 2,
            "expected": ["帐号不能为空", "密码不能为空", "验证码不能为空"]
        }
    ]


if __name__ == '__main__':
    pass
