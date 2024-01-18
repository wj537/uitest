import allure
from pages.page_base import PageBase
from pages.page_login import PageLogin

class PageHome(PageLogin):
    def el_title(self):
        """
        首页的首页tab
        :return:
        """
        try:
            el = self.driver.fendElement(by='ID', value='com.renpho.health:id/navigation_bar_item_large_label_view')
        except Exception:
            el = self.driver.fendElement(by="XPATH", value="//*[@text='首页']")
        return el

    def get_title(self):
        text = self.el_title().text
        return text
