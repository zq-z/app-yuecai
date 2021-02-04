from time import sleep

import page
from base.base import Base


class login_page(Base):


   def input_phone(self,text):

       self.base_input(page.phone,text)

   def input_password(self,text):
       self.base_input(page.password,text)
   def click_checkbox(self):
       self.base_click(page.click_checkbox)
   def click_login_button(self):
       self.base_click(page.click_login_button)
   def get_screen(self):
       self.base_get_image()
