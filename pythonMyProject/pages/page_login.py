import allure
from pages.page_base import PageBase


class PageLogin(PageBase):

    """
    登录页
    """
    def el_title(self):
        """
        标题元素
        :return:
        """
        el = self.driver.fendElement(by="ID", value="com.renpho.health:id/textView132")
        return el

    def get_title(self):
        text = self.el_title().text
        return text

    def el_home_title(self):
        try:
            el = self.driver.fendElement(by='ID', value='com.renpho.health:id/navigation_bar_item_large_label_view')
        except Exception:
            el = self.driver.fendElement(by="XPATH", value="//*[@text='首页']")
        return el

    def get_home_title(self):
        text = self.el_home_title().text
        return text

    def el_email_input_box(self):
        """
        邮箱输入框
        :return:
        """
        try:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/input_email")
        except Exception:
            el = self.driver.fendElement(by='xpath', value="//*[@text='邮箱']")
        return el

    def el_password_input_box(self):
        """
        密码输入框
        :return:
        """
        try:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/input_pas")
        except Exception:
            el = self.driver.fendElement(by='xpath', value="//*[@text='密码']")
        return el
    def el_show_password_button(self):

        """
        展示密码按钮
        :return:
        """
        try:
            return self.driver.fendElement(by="id", value="com.renpho.health:id/look_pass")
        except Exception:
            self.log.logger.error("在登录页没有定位到密码【显示/隐藏】按钮")
            # assert False

    def el_remember_password(self):
        try:
            return self.driver.fendElement(by="XPATH", value="//*[@text='记住密码']")
        except Exception:
            self.log.logger.error("在登录页没有定位到【记住密码】选项")
            # assert False
    def el_login_button(self):
        """
        登录按钮
        :return:
        """

        try:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/progressButton")
        except Exception:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/text")
        return el
    def el_register_button(self):
        """
        注册按钮
        :return:
        """
        try:
            el = self.driver.fendElement(by="id", value="com.renpho.health:id/register_accont")
        except Exception:
            el = self.driver.fendElement(by="xpath", value="//*[@text='注册']")
        return el


    def el_forget_password_button(self):
        try:
            return self.driver.fendElement(by="id", value="com.renpho.health:id/forget_pass")
        except Exception:
            self.log.logger.error("在登录页没有定位到【	忘记密码?】")


    @allure.step("步骤：输入邮箱")
    def input_email(self,email):
        self.el_email_input_box().click()
        self.el_email_input_box().clear()
        self.el_email_input_box().send_keys(email)

    @allure.step("步骤：输入密码")
    def input_password(self,pwd):
        self.el_password_input_box().click()
        self.el_password_input_box().clear()
        self.el_password_input_box().send_keys(pwd)

    @allure.step("步骤：点击登录按钮")
    def click_login_button(self):
        self.el_login_button().click()


    @allure.step("步骤：点击注册按钮")
    def click_register_button(self):
        self.el_register_button().click()

    @allure.step("步骤：执行公共登录操作，进入系统首页")
    def common_login(self,email,pwd):
        """
        登录的公共方法
        :param email:
        :param pwd:
        :return:
        """
        self.log.logger.info("开始执行登录用例")
        self.input_email(email)
        self.log.logger.info("输入了邮箱")
        self.input_password(pwd)
        self.log.logger.info("输入了密码")
        self.click_login_button()
        self.log.logger.info("点击了登录按钮")


    @allure.step("步骤：选择提示框内的否定选项")
    def choose_prompt_refuse(self):
        """
        弹出的提示框内点击否定选项
        :return:
        """
        try:
            # 在获取地址权限的弹窗中选择“拒绝”  安卓9以下有
            el = self.driver.fendElement("id", "com.android.packageinstaller:id/permission_deny_button", "5")
            el.click()
        except Exception:
            self.log.logger.info("没有出现获取地址权限的弹窗")
        try:
            # 在允许查找附近设备的弹窗中选择“拒绝”，安卓12
            el = self.driver.fendElement("id", "com.android.permissioncontroller:id/permission_deny_button", "5")
            el.click()
        except Exception:
            self.log.logger.info("没有出现允许查找附近设备的弹窗")
        try:
            # 在位置信息声明中选择暂不开启 安卓9以下有
            el = self.driver.fendElement("ID", "com.renpho.health:id/location_permission_open_try_tv", "5")
            el.click()
        except Exception:
            self.log.logger.info("没有出现'位置信息声明'")

    # @allure.step("步骤：断言是否进入了首页")
    # def assert_isinhomepage(self):
    #

    def prompt_account_password_error(self):
        """

        :return:登录账号或密码错误时的提示语
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/login_other_error")
            print(el.text)
            return el.text
        except Exception:
            self.log.logger.error("在登录页未定位到提示语：'您输入的账户或密码有误，请重新输入'")


    def prompt_emailbox_isEmpty(self):
        """

        :return:邮箱为空时的提示语
        """
        try:
            el = self.driver.fendElement(by="ID", value="com.renpho.health:id/email_error")
            print(el.text)
            return el.text
        except Exception:
            self.log.logger.error("在登录页邮箱输入为空时，未定位到提示语：'请输入有效的电子邮箱地址'")


    def prompt_email_no_register(self):
        try:
            el = self.driver.fendElement(by="id",value="com.renpho.health:id/tvContent")
            print(el.text)
            return el.text
        except Exception:
            self.log.logger.error("在登录页未定位到提示语：该邮箱未注册")

    @allure.step("步骤：判断是否登录进首页")
    def assert_IsInHomePage(self, isInHomePage):
        if isInHomePage in ("True", "T", "t", "true", "YES", "Yes", "yes", "Y", "y"):
            try:
                self.choose_prompt_refuse()
                els = self.driver.fendElements(by="XPATH", value="//*[@text='Home']")
                assert len(els) >= 1
                # self.driver.fendElement(by="XPATH", value="//*[@text='首页']")
                assert True
            except:
                self.log.logger.error("执行登录正向用例失败")
                self.driver.get_screenshot("执行登录正向用例失败")
                assert False

        elif isInHomePage in ("False", "FALSE", "F", "f", "NO", "No", "no", "N", "n"):
            try:
                # els = self.loginPage.driver.fendElements(by="XPATH", value="//*[@text='登录']")
                # assert len(els) == 1
                self.driver.fendElement(by="XPATH", value="//*[@text='Log In']")
                assert True
            except:
                self.log.logger.error("执行登录反向用例失败")
                self.driver.get_screenshot()
                assert False