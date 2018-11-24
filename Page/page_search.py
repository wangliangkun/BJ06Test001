from selenium.webdriver.common.by import By
from Base.base import Base
import Page
"""
操作步骤：
		1. 点击搜索按钮 id 		com.android.settings:id/search
		2. 搜索框内输入内容id   android:id/search_src_text
		3. 点击返回按钮 class   android.widget.ImageButton
"""


class PageSearch(Base):
    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_element(Page.search_btn)
    # 搜索框内输入内容
    def page_input_search_box(self,value):
        self.base_input_element(Page.search_box).send_keys(value)
    # 点击返回按钮
    def page_click_back_btn(self):
        self.base_click_element(Page.back_btn)
    # 断言
    def page_is_ok(self,loc):
        self.base_find_element(Page.mobile_network)