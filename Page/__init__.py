from selenium.webdriver.common.by import By
# 点击搜索按钮
search_btn=By.ID,"com.android.settings:id/search"
# 搜索输入框
search_box=By.ID,"android:id/search_src_text"
# 返回按钮
back_btn=By.CLASS_NAME,"android.widget.ImageButton"
# 移动网络
mobile_network=By.XPATH,"//*[@text=移动网络]"