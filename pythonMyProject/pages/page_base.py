import os
import time
from project_utils.utilfile import returnAppEnvFromInitFile
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from appium import webdriver

from project_utils.logger import Logger
"""
连接手机并启动一个应用

param:
    platformName:手机操作系统
    platformVersion：系统版本
    automationName: 驱动，安卓uiautomator2
    deviceName：设备编号
    appPackage:包名
    appActivity: Activity名称
     # 这两个属性设置支持中文输入
    unicodeKeyboard: True,
    resetKeyboard: True,
    noReset：是否清除缓存，True清除，False不清除
    language='en',
    locale='US'
    appium_server_url 
"""

appium_server_url = 'http://localhost:4723/wd/hub'
capabilities = {}

capabilities['platformName'] = 'Android'
# 设备名称，adb devices
# capabilities['deviceName'] = 'RXD0221326001256'
capabilities['deviceName'] = 'emulator-5554'
# 手机安卓系统的版本
# capabilities['platformVersion'] = 10
capabilities['automationName'] = 'UIAutomator2'
capabilities['appPackage'] = 'com.renpho.health'
capabilities['appActivity'] = 'com.renpho.login.LoginMainActivity'
# 这两个属性设置支持中文输入
# capabilities['unicodeKeyboard'] = True
# capabilities['resetKeyboard'] = True
# True不会清除缓存数据
capabilities['noReset'] = True
capabilities['session'] = True



class PageBase():

    def __init__(self):
        self.log = Logger('testLog.log', level='debug')
        try:
            self.driver = BeseUtil(appium_server_url, capabilities)
            self.log.logger.info("App启动成功")
        # print("App启动成功")
        except Exception as e:
            self.log.logger.info("App启动失败")
            raise e

class BeseUtil():

    def __init__(self, appium_server_url, capabilities):
        self.log = Logger('testLog.log', level='debug')
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.driver.implicitly_wait(8)
        self.wait = WebDriverWait(self.driver, 10, 0.5)
    def waitElement(self, el, *args):
        """
        等待元素的方法，没人等待时间30秒
        :param el: 元素
        :param args: 可变长参数，用于设置等待时间，当其只有一个时才有效
        :return:
        """
        global waitElementResult
        waitTime = 30
        try:
            if len(args) == 1:
                for i in args:
                    waitTime = int(i)
            else:
                waitTime = 30
        except Exception:
            raise Exception

        try:
            WebDriverWait(self.driver, waitTime, 0.5).until(EC.visibility_of(el))
            waitElementResult = 'T'
        except Exception:
            waitElementResult = "F"
            print(waitElementResult)

        if waitElementResult == "F":
            for i in range(4):
                try:
                    if i <= 2:
                        self.swipToDown()
                        WebDriverWait(self.driver, 8, 0.5).until(EC.visibility_of(el))
                        waitElementResult = 'T'
                        break
                    else:
                        self.swipToUp()
                        WebDriverWait(self.driver, 8, 0.5).until(EC.visibility_of(el))
                        waitElementResult = 'T'
                        break
                except Exception:
                    continue
        try:
            if waitElementResult == "F":
                assert 1 == 2
        except Exception as e:
            self.get_screenshot("等待元素超时")
            self.log.logger.error("等待元素超时")
            # e.with_traceback()
            # assert False

    def fendElement(self, by, value, *args):
        """
        :param By: xpath/XPATH/Xpath, id/ID/resource-id, class/CLASS/classname/ClassName/class_name/CLASSNAME/CLASS_NAME
        :param value:
        :param *args: 用于设置等待时间
        :return: an element
        """
        waiTime = 30
        try:
            if len(args) == 1:
                for i in args:
                    waiTime = int(i)
            else:
                waiTime = 30
        except Exception:
            raise Exception

        try:
            if by == "xpath" or by == "XPATH" or by == "Xpath":
                el = self.driver.find_element(by=By.XPATH, value=value)
                self.waitElement(el, waiTime)
                return el
            elif by == "id" or by == "resource-id" or by == "ID":
                el = self.driver.find_element(by=By.ID, value=value)
                self.waitElement(el, waiTime)
                return el
            elif by == 'CLASS' or by == 'class' or by == 'classname' or by == 'ClassName' or by == 'class_name' or by == 'CLASSNAME' or by == 'CLASS_NAME':
                el = self.driver.find_element(by=By.CLASS_NAME, value=value)
                self.waitElement(el, waiTime)
                return el
            else:
                self.log.logger.warning(
                    "请输入正确的定位方式：定位方式by等于xpath/XPATH/Xpath，id/ID/resource-id, class/CLASS/classname/ClassName/class_name/CLASSNAME/CLASS_NAME\n")
                # assert False
        except Exception:
            # self.get_screenshot("fendElement未找到目标元素,属性" + by + ",属性值" + value)
            self.log.logger.warning("fendElement未找到目标元素:属性by：%s 属性值value：%s", by, value)
            # assert False
            raise Exception

    def get_screenshot(self, *args):
        """
        Get the current window screenshot.

        :param args: 备注，会作为名称的一部分拼接到截图名称中
        Usage:
        driver.get_screenshot()
        """
        descr = ''
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))

        if  returnAppEnvFromInitFile() == 'test':
            pic_path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\result\\screenshot\\" + current_date
        else:
            pic_path = os.path.abspath(
                os.path.dirname(os.getcwd())) + "\\result_release\\screenshot\\" + current_date

        try:
            if len(args) < 1:
                pic_name = current_time + '--' + '.png'
            else:
                for i in args:
                    descr = descr + str(i)
                pic_name = current_time + '--' + descr + '.png'
        except Exception:
            self.log.logger.warning("请检查截图函数的输入参数")
            raise Exception

        if os.path.exists(pic_path):
            pass
        else:
            # 创建多层级的文件夹
            os.makedirs(pic_path)
        self.driver.get_screenshot_as_file(pic_path + '\\' + pic_name)
        return pic_path + '\\' + pic_name



if __name__ == '__main__':
    PageBase()
