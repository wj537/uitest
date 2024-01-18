from pages.page_login import PageLogin
from utils.utilfile import *
import pytest
import allure


def get_data_success_login():
    """
    获取登录成功的数据
    :return:
    """
    env = returnAppEnvFromInitFile()
    if env == "test":
        try:
            datas = Utilfile("./data/data_testEnv/test_android_login_success.csv").get_csv_data()

        except Exception:
            datas = Utilfile("../data/data_testEnv/test_android_login_success.csv").get_csv_data()
        return datas
    else:
        try:
            datas = Utilfile("./TestData/Data_releaseEnv/test_Android_login_Success.csv").get_csv_data()
        except Exception:
            datas = Utilfile("../TestData/Data_releaseEnv/test_Android_login_Success.csv").get_csv_data()
        return datas


def get_data_all_login():
    """
    获取登录失败的数据
    :return:
    """
    env = returnAppEnvFromInitFile()
    if env == "test":
        try:
            datas = Utilfile("./data/data_testEnv/test_android_login.csv").get_csv_data()
        except Exception:
            datas = Utilfile("../data/data_testEnv/test_android_login.csv").get_csv_data()
        return datas
    else:
        try:
            datas = Utilfile("./TestData/Data_releaseEnv/test_LoginCase.csv").get_csv_data()
        except Exception:
            datas = Utilfile("../TestData/Data_releaseEnv/test_LoginCase.csv").get_csv_data()
        return datas




@allure.feature("登录")
class TestLoginCase():

    def setup(self):
        self.PageLogin = PageLogin()
        self.PageLogin.log.logger.info("----------开始执行登录用例-------------")

    def teardown(self):
        self.PageLogin.log.logger.info("----------结束执行登录用例-------------")
        try:
            self.PageLogin.driver.quit()
        except Exception:
            print("teardown")

    @allure.step("步骤：判断页面告警提示")
    def assert_Prompt(self, prompt):
        if prompt == "You may have entered an incorrect email address or password. Please check and try again.":
            errorPrompt = self.PageLogin.prompt_account_password_error()  # 获取页面提示语
            self.PageLogin.log.logger.info("登录页当前展示提示语：%s", errorPrompt)  # 打印提示语
            # assert errorPrompt == prompt  # 断言
            if errorPrompt == prompt:
                assert True
            else:
                self.PageLogin.driver.get_screenshot()
                self.PageLogin.log.logger.error("登录页提示语与：'%s' ,与预期结果：'%s' 不一致", errorPrompt, prompt)
                assert False
        elif prompt == "Please enter a valid email address.":
            errorPrompt = self.PageLogin.prompt_emailbox_isEmpty()
            if errorPrompt == prompt:
                assert True
            else:
                self.PageLogin.driver.get_screenshot()
                self.PageLogin.log.logger.error("登录页提示语与：'%s' ,与预期结果：'%s' 不一致", errorPrompt, prompt)
                assert False
        elif prompt == "Email was not registered":
            errorPrompt = self.PageLogin.prompt_email_no_register()
            self.PageLogin.log.logger.info("登录页当前展示提示语：%s", errorPrompt)
            if errorPrompt == prompt:
                assert True
            else:
                self.PageLogin.driver.get_screenshot()
                self.PageLogin.log.logger.error("登录页提示语与：'%s' ,与预期结果：'%s' 不一致", errorPrompt, prompt)
                assert False

    @allure.story("登录成功的用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("email, pwd", get_data_success_login())
    def test_login_success_case(self, email, pwd):
        try:
            self.PageLogin.common_login(email, pwd)
            self.PageLogin.log.logger.info('检查是否有位置获取位置信息的提示，有则选择否')
            self.PageLogin.choose_prompt_refuse()
            assert self.PageLogin.get_home_title() == "Home"
        except Exception:
            self.PageLogin.log.logger.info("执行登录成功的用例，过程中出现异常")
            raise Exception

    @allure.story("登录失败的用例")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("email, pwd, prompt,isInHomePage", get_data_all_login())
    def test_login_failure_case(self,email,pwd,prompt,isInHomePage):
        try:
            self.PageLogin.common_login(email, pwd)
            self.assert_Prompt(prompt)                            #判断错误提示语是否正确
            if prompt not in ("Email was not registered"):
                self.PageLogin.assert_IsInHomePage(isInHomePage)  #判断是否还在登录页
            self.PageLogin.log.logger.info("登录失败的用例执行结束")
        except Exception:
            self.PageLogin.log.logger.info("登录失败的用例执行失败")
            self.PageLogin.driver.get_screenshot("执行登录失败的用例的失败截图")
            assert False




if __name__ == '__main__':
    print(get_data_success_login())
