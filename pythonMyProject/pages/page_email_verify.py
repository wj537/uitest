import allure
from pages.page_login import PageLogin








class PageEmailVerify(PageLogin):
    def get_email_verify_page_name(self):
        """
        获取邮箱验证页的标题
        :return:
        """
        text = self.driver.fendElement(by="ID", value="com.renpho.health:id/tv_include_title").text
        return text

    def el_verify_code_input_box(self):
        """
        验证码输入框
        :return:
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/cet_vg")
        except Exception:
            el = self.driver.fendElement(by='class', value="android.widget.EditText")
        return el

    @allure.step("步骤：输入验证码")
    def input_verify_code(self, VCode):
        try:
            self.el_verify_code_input_box().click()
            self.el_verify_code_input_box().clear()
            self.el_verify_code_input_box().send_keys(VCode)
        except Exception:
            self.driver.get_screenshot()
            self.log.logger.error("输入验证码时发生异常，验证码：%s", VCode)
            raise Exception

    def get_email_verify_code_error_prompt(self):
        """
        验证码错误的提示语
        :return:
        """
        text = self.driver.fendElement("id", "com.renpho.health:id/tv_vg_error").text
        return text

    def get_email_verify_code_limit_prompt(self):
        """
        验证码次数上限提示语
        :return:
        """
        text = self.driver.fendElement(by="ID", value="com.renpho.health:id/tv_vg_error").text
        return text
