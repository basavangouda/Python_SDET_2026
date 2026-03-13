#https://admin-demo.nopcommerce.com/
from selenium.webdriver.common.by import By

class Login_Admin_Page:
    #Finding attributes in admin login page
    text_box_username_id='Email'
    text_box_password_id="Password"
    btn_login_xpath="//button[@type='submit']"
    link_text_logout="Logout"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.text_box_username_id).clear()
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.text_box_password_id).clear()
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_text_logout).click()