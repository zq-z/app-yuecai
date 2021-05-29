import time

import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait



#log=GetLogger().get_log("ll")

class Base:
    def __init__(self,driver):
        #log.info("初始化driver{}".format(driver))
        self.driver=driver




    # 查找元素
    def base_find_element(self, loc, timeout=30, poll_frequency=1):
        #log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))

    # 点击方法

    def base_click(self, loc):
       # log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):

        el = self.base_find_element(loc)
        el.clear()
       # # log.info("正在全选：{}".format(loc))
       #  el.send_keys(Keys.CONTROL + "a")
       #  #3log.info("正在删除：{}".format(loc))
       #  el.send_keys(Keys.DELETE)
       # # log.info("正在输入：{}".format(loc,value))
        el.send_keys(value)

    # 获取文本的方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 获取截图的方法
    def base_get_image(self):
        path = "../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
        self.driver.get_screenshot_as_file(path)

        allure.attach.file(path,attachment_type=allure.attachment_type.PNG)

    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except:
            print('A')
            print('U')

            return False



