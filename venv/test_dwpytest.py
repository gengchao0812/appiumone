import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction


sys.path.append("..")

class TestDw():
    def setup(self):
        print("调起setup")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        print("初始化完毕")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        print("开始等待")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        print("开始等待5秒")
        time.sleep(5)

        action = TouchAction(self.driver)
        #release 释放掉  perform 执行它 wait单位是毫秒
        # action.press(x=731,y=2083).wait(200).move_to(x=731,y=484).release().perform()
        #获取屏幕尺寸
        windows_rect = self.driver.get_window_rect()['width']
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x1 = int (width/2)
        y_start = int(height * 4/5)
        y_end = int (height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
    
    @pytest.mark.skip
    def test_two(self):
        """
        1. 打开 雪球app
        2. 定位首頁的搜索框
        3. 判断搜索框的是否可用，并查看搜索框的name属性值
        4. 打印搜索框这个元素的左上角坐标和他的宽高
        5. 向搜索框输入alibaba
        6. 判断【阿里巴巴】是否可见
        7. 如果可见，打印“搜索成功”， 如果不可见，打印“搜索失败”
        :return:
        """
        time.sleep(2)
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(el2.text)
        print(f"宽和高是 {el2.size}")
        print(f"元素坐标是 {el2.location}")
        if el2.is_enabled() == True:
            el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        #判断可见
        elemengt_display = el4.get_attribute("displayed")
        if elemengt_display == 'true':
            print("搜索成功")
        else:
            print("搜索失败")


    @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1. 打开 雪球app
        2. 点击搜索输入框
        3. 向搜索输入框里输入“阿里巴巴”
        4. 在搜索结果里面选择“阿里巴巴”，然后进行点击
        5. 获取这只上香港 阿里巴巴的股价， 并判断 这只股价的价格>200
        """
        time.sleep(2)
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(1)
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        el4.click()
        el5 = float(self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]").text)
        el5 = float(self.driver.find_element_by_class_name(""))
        assert  el5>200



if __name__ == '__main__':
    pytest.main()