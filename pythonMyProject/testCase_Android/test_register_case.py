import allure
from pages.page_register import PageRegister
import pytest

from project_utils.random_util import get_random_email, get_random_pwd
from project_utils.utilfile import *


@allure.step("获取邮箱已经存在的测试数据")
def get_data_email_already_register():
    env = returnAppEnvFromInitFile()
    if env == "test":
       datas = Utilfile("../data/data_testEnv/test_android_email_already_register.csv").get_csv_data()
       return datas
    elif env == "release":
        pass

@allure.step("获取邮箱格式错误的测试数据")
def get_data_email_format_error():
    env = returnAppEnvFromInitFile()
    if env == "test":
       datas = Utilfile("../data/data_testEnv/test_android_email_format_error.csv").get_csv_data()
       return datas
    elif env == "release":
        pass


# @allure.feature("注册")
class TestRegisterCase():
    def setup(self):
        self.PageRegister = PageRegister()
        self.PageRegister.log.logger.info("—————————开始执行注册账号用例————————————")
    def teardow(self):
        self.PageRegister.driver.quit()
        self.PageRegister.log.logger.info("———————————结束执行注册用例————————————————")




    @allure.story("注册成功的用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_register_success(self):
        env = returnAppEnvFromInitFile()
        try:
            if env == "test":
                self.PageRegister.click_register_button()
                self.PageRegister.click_agree_privacy_button()
                self.PageRegister.click_get_push_button()
                self.PageRegister.click_Iagree_button()
                # 获取随机邮箱
                email = get_random_email()
                self.PageRegister.input_email(email)
                # 获取随机密码
                password = get_random_pwd()
                self.PageRegister.input_password(password)
                self.PageRegister.click_confirm_button()
                # 获取验证码
                code = self.PageRegister.get_email_VCode(email)
                self.PageRegister.input_verify_code(code)
                assert self.PageRegister.get_perfect_personal_information_page_title() == "Get started"


            elif env == "release":
                 pass

        except Exception:
            self.PageRegister.driver.get_screenshot("执行注册成功的用例，过程中出现了异常")
            self.PageRegister.driver.log.logger.error("执行注册成功的用例，过程中出现了异常")
            raise Exception

    @allure.story("邮箱已注册的失败用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("email", get_data_email_already_register())
    def test_email_already_register(self, email):
        env = returnAppEnvFromInitFile()
        try:
            if env == "test":
                self.PageRegister.click_register_button()
                self.PageRegister.click_agree_privacy_button()
                self.PageRegister.click_get_push_button()
                self.PageRegister.click_Iagree_button()
                self.PageRegister.input_email(email)
                self.PageRegister.input_password("123456")
                self.PageRegister.click_confirm_button()
                assert self.PageRegister.get_email_already_registered_prompt() == "Email has been registered！"

        except Exception:
            self.PageRegister.driver.get_screenshot("执行邮箱已经注册的用例，过程中出现了异常")
            self.PageRegister.driver.log.logger.error("执行邮箱已经注册的用例，过程中出现了异常")
            raise Exception

    @allure.story("注册时邮箱格式错误的用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("email,prompt", get_data_email_format_error())
    def test_email_format_error(self, email, prompt):
        env = returnAppEnvFromInitFile()
        try:
            if env == "test":
                self.PageRegister.click_register_button()
                self.PageRegister.click_agree_privacy_button()
                self.PageRegister.click_get_push_button()
                self.PageRegister.click_Iagree_button()
                self.PageRegister.input_email(email)
                self.PageRegister.input_password("123456")
                result = self.PageRegister.get_email_format_error_prompt()
                assert prompt == result
            else:
                pass
        except Exception:
            self.PageRegister.driver.log.logger.info("执行注册时邮箱格式错误的用例失败")
            raise Exception

    @allure.story("注册时验证码错误的用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_email_verify_code_error(self):
        env = returnAppEnvFromInitFile()
        try:
            if env == "test":
                self.PageRegister.click_register_button()
                self.PageRegister.click_agree_privacy_button()
                self.PageRegister.click_get_push_button()
                self.PageRegister.click_Iagree_button()
                email = get_random_email()
                self.PageRegister.input_email(email)
                self.PageRegister.input_password("123456")
                self.PageRegister.click_confirm_button()
                self.PageRegister.input_verify_code("1111")
                assert self.PageRegister.get_email_verify_code_error_prompt() == "Email was not registered"
            else:
                pass

        except Exception:
            self.PageRegister.driver.log.logger.info("执行注册时邮箱验证码错误的用例失败")
            raise Exception













