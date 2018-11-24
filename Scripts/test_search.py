import os,sys

import pytest

sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page_search import PageSearch

class TestSearch():
    # 初始化方法
    def setup_class(self):
        # 实例化对象
        self.search=PageSearch(get_driver())
    # 结束方法
    def teardown_class(self):
        self.search.driver.quit()
    # 测试方法
    @pytest.mark.parametrize("value",['l'])
    def test_seaarch(self,value):
        # 点击搜索
        self.search.page_click_search_btn()
        # 输入搜索信息
        self.search.page_input_search_box(value)
        # 点击返回
        try:
            assert  self.search.page_is_ok()
            print("断言成功")
        except:
            print("断言失败")

        self.search.page_click_back_btn()
