from Page.page_address import PageAddress
from Page.page_login import PageLogin
from Page.page_search import PageSearch


class PageIn():
    # 获取地址
    def page_get_address(self):
        return PageAddress(driver)
    # 获取登录
    def page_get_login(self):
        return PageLogin(driver)
    # 获取搜索
    def page_get_search(self):
        return PageSearch(driver)