from time import sleep

import allure
import pytest


from base.base_driver import Base_driver
from page.login_page import login_page
from tool.read_json import read_json

def get_login():
    datas = read_json("login.json")
    airs = []
    for data in datas.values():
        airs.append((data.get("username"),
                     data.get("password"),
                     data.get("result_except"),
                     #data.get("success")
                     )
                    )
    return airs

class TestLogin:
    def setup(self):
       self.driver=Base_driver.__init__(self)

       self.login=login_page(self.driver)

    @allure.feature("登录模块")
    @pytest.mark.parametrize(("username","password","result_except"),get_login())
    @allure.story("登录")
    def test_login(self,username,password,result_except):

         self.login.input_phone(username)


         self.login.input_password(password)

         self.login.click_checkbox()

         self.login.click_login_button()
         try:
            assert result_except=="手机号不正确"

         except AssertionError as e:
            sleep(2)
            self.login.get_screen()
if __name__ == '__main__':
    pytest.main(["test_login.py"])








