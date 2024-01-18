import time

import allure
from utils.utilDB import UtilDB
from pages.page_login import PageLogin
from utils.random_util import *

# _________________________用户许可页面____________________________

class PageRegister(PageLogin):

    def el_title(self):
        el = self.driver.fendElement(by="ID", value="com.renpho.health:id/tv_title")
        return el

    def get_title(self):
        text = self.el_title().text
        return text

    def el_agree_privacy_box(self):
        """
        我已阅读并同意使用条款和隐私政策框
        :return:
        """
        el = self.driver.fendElement(by="ID", value="com.renpho.health:id/policy")
        return el

    def click_agree_privacy_button(self):
        self.el_agree_privacy_box().click()

    def el_get_push_box(self):
        """
        向我发送有关Renpho Health产品，新闻和促销的最新消息框
        :return:
        """
        el = self.driver.fendElement(by="ID", value="com.renpho.health:id/push")
        return el

    def click_get_push_button(self):
        """
        点击向我发送推送
        :return:
        """
        self.el_get_push_box().click()

    def el_Iagree_button(self):
        """
        我同意按钮
        :return:
        """
        el = self.driver.fendElement(by="ID", value="com.renpho.health:id/next_btn")
        return el

    def click_Iagree_button(self):
        self.el_Iagree_button().click()

    def is_in_user_license_page(self):
        title = self.get_title()
        assert title == "User Permission"

    # ____________________________注册页_________________________________

    def el_title_sign_up(self):
        """
        注册页标题
        :return:
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/tv_include_title")
        except Exception:
            el = self.driver.fendElement(by="xpath", value="//*[@text='注册']")
        return el

    def get_title_sign_up(self):
        """
        获取注册页标题
        :return:
        """
        text = self.el_title_sign_up().text
        return text

    def is_in_email_page(self):
        assert self.get_title_sign_up() == "sign up"

    def el_email_input_box(self):
        """
        邮箱输入框
        :return:
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/input_email")
        except Exception:
            el = self.driver.fendElement(by="xpath", value="//*[@text='邮箱']")
        return el

    def el_password_input_box(self):
        """
        密码输入框
        :return:
        """
        el = self.driver.fendElement(by="id", value="com.renpho.health:id/input_pas")
        return el

    def el_confirm_button(self):
        """
        确定登录按钮
        :return:
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/register_btn")
        except Exception:
            el = self.driver.fendElement(by="xpath", value="//*[@text='密码']")

        return el



    def el_email_already_registered_prompt(self):
        """
        该元素用于展示邮箱已经注册的提示
        :return: el
        """
        try:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/tvContent")
        except Exception:
            el = self.driver.fendElement(by="xpath", value="//*[@text='Email has been registered！']")
        return el
    def get_email_already_registered_prompt(self):
        """
        获取邮箱已经注册的提示语
        :return: text
        """
        text = self.el_email_already_registered_prompt().text
        return text

    def get_email_format_error_prompt(self):

        """
        获取邮箱格式错误的提示语
        :return:
        """
        text = self.driver.fendElement("id", "com.renpho.health:id/email_error").text
        return text


    @allure.step("注册步骤：输入邮箱")
    def input_email(self, email):
        self.el_email_input_box().click()
        self.el_email_input_box().clear()
        self.el_email_input_box().send_keys(email)

    @allure.step("注册步骤：输入密码")
    def input_password(self, password):
        self.el_password_input_box().click()
        self.el_password_input_box().clear()
        self.el_password_input_box().send_keys(password)

    @allure.step("注册步骤：点击确定")
    def click_confirm_button(self):
        self.el_confirm_button().click()

    # ___________________邮箱验证页_________________
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
        text = self.driver.fendElement("id", "com.renpho.health:id/tv_vg_error").text
        return text

    def get_email_verify_code_limit(self):
        text = self.driver.fendElement(by="ID", value="com.renpho.health:id/tv_vg_error").text
        return text



    # ___________完善信息页_________________
    def el_perfect_personal_information_page_title(self):
        """
        该元素展示完善信息页的标题名称
        :return: el
        """

        el = self.driver.fendElement(by="xpath", value="//*[@text='Get started']")
        return el

    def get_perfect_personal_information_page_title(self):
        """
        获取完善信息页的标题名称
        :return: text
        """
        text = self.el_perfect_personal_information_page_title().text
        return text

    def perfect_personal_information(self):
        """
        完善个人信息 (录入默认信息)
        :return:
        """
        # 选择性别为男性
        self.driver.fendElement(by="id", value="com.renpho.health:id/rb_header_male").click()

        # 选择生日
        self.driver.fendElement(by="id", value="com.renpho.health:id/tv_item_des").click()
        self.driver.fendElement(by="id", value="android:id/button1").click()

        # 选择身高
        self.driver.fendElement(by="id", value="com.renpho.health:id/tv_item_des").click()
        self.driver.fendElement(by="id", value="com.renpho.health:id/tv_dialog_confirm").click()

        # 选择体重
        self.driver.fendElement(by="id", value="com.renpho.health:id/tv_item_des").click()
        self.driver.fendElement(by="id", value="com.renpho.health:id/ok").click()

        # 运动模式，不是必要

        # 保存
        self.driver.fendElement(by="id", value="com.renpho.health:id/btn_footer_save").click()




    def click_skip(self):
        self.driver.fendElement("id","com.renpho.health:id/tv_jump_over").click()


    # _____________邮箱页的其他操作______________

    @allure.step("步骤：获取正确的邮箱验证码")
    def get_email_VCode(self, email):
        """
        获取正确邮箱验证码
        :return:
        """
        # sql = "SELECT code FROM verify_code_password vcp WHERE email in ('xbtest001@qq.com')"
        sql_testenv = "SELECT code FROM test2.verify_code_password vcp WHERE email in ('" + email + "')"
        from utils.utilfile import returnAppEnvFromInitFile
        env = returnAppEnvFromInitFile()
        pwd = '123456'
        time.sleep(3)
        if env == 'test':
            db = UtilDB(url='192.168.9.253', port=3306, dbName='', userName='root', passWord=pwd)
            value = db.get_data(sql_testenv)
            code = value[0][0]
            print(code)
            print(type(code))
            return code
        else:
            pass

    def common_register(self):
        """
        注册流程的公共方法
        :return:
        """
        self.click_register_button()
        self.log.logger.info("点击了首页的注册按钮")
        self.click_agree_privacy_button()
        self.log.logger.info("点击同意使用条款")
        self.click_get_push_button()
        self.log.logger.info("点击了向我发送推送")
        self.click_Iagree_button()
        self.log.logger.info("点击了我同意按钮")
        # 获取随机邮箱
        email = get_random_email()
        self.input_email(email)
        self.log.logger.info('输入了邮箱')
        # 获取随机密码
        password = get_random_pwd()
        self.input_password(password)
        self.log.logger.info('输入了密码')
        self.click_confirm_button()
        # 获取验证码
        code = self.get_email_VCode(email)
        self.input_verify_code(code)
        # 完善个人信息并点击保存
        self.perfect_personal_information()
        # 点击跳过进入首页
        self.click_skip()



