from utils.utilfile import *
from pages.page_forget_password import PageForgetPassword


def get_forget_pwd_success_data():







 class TestForgetPassword():
    def setup(self):
        self.PageForgetPassword = PageForgetPassword()
        self.PageForgetPassword.log.logger.info("—————————开始执行忘记密码用例————————————")
    def teardown(self):
        self.PageForgetPassword.driver.quit()
        self.PageForgetPassword.log.logger.info("———————————结束执行忘记密码用例————————————————")
