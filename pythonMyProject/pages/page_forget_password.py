import allure

from pages.page_login import PageLogin
class PageForgetPassword(PageLogin):

    #------------------------------忘记密码页-------------------------------
    def get_title(self):
        text = self.driver.fendElement('id', 'com.renpho.health:id/tv_include_title').text
        return text
    def el_email_input_box(self):
       el = self.driver.fendElement('id', 'com.renpho.health:id/et_vg_email')
       return el
    @allure.step('忘记密码时输入邮箱')
    def input_email(self,email):
        self.el_email_input_box().click()
        self.el_email_input_box().clear()
        self.el_email_input_box().send_keys("email")

    @allure.step('点击提交按钮')
    def click_submit(self):
        self.driver.fendElement('id', 'com.renpho.health:id/sb_vp_submit').click()

    #---------------------------设置密码页----------------------------------
    def get_set_pwd_title(self):
        return self.driver.fendElement('id', 'com.renpho.health:id/tv_include_title').text

    def el_password_input_box(self):
        el = self.driver.fendElement('id','com.renpho.health:id/et_fragment_password')
        return el
    @allure.step('设置密码时输入新密码')
    def input_password(self, pwd):
        self.el_password_input_box().click()
        self.el_password_input_box().clear()
        self.el_password_input_box().send_keys("pwd")

    @allure.step('点击确定')
    def click_confirm(self):
        self.driver.fendElement('xpath','//android.widget.TextView[@text="Confirm"]').click()




