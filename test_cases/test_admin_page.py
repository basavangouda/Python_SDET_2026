
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

#When we get Captcha check box we can handle using this below package
# pip3 install seleniumbase
from seleniumbase import Driver

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger=Log_Maker.log_gen()

    @pytest.mark.smoke
    def test_title_verification(self,setup1):
        self.logger.info("*************************************************************Test1_01_Admin_Login ************")
        self.logger.info("****************************Verification of admin login page title  ******************************************")
        self.driver=setup1
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        actual_title=self.driver.title
        print(actual_title)
        expected_title="nopCommerce demo store. Login"
        if actual_title==expected_title:
            self.logger.info("**************test_title_verification matched ******************************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("**************test_title_verification not matched ******************************")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_valid_admin_login(self,setup1):
        #self.driver = webdriver.Chrome()
        #the below Driver using to handle security captcha
        #self.driver=Driver(uc=True,headless=False)
        self.logger.info("**************test_valid_admin_login started ******************************")
        self.driver=setup1
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        # attempt to click the CAPTCHA checkbox if present
        self.driver.uc_gui_click_captcha()
        act_dashboard_text=self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashboard_text=="Dashboard":
            self.logger.info("**************test_Dashboard text found ******************************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("**************test_Dashboard text not found ******************************")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_invalid_admin_login(self,setup1):
        self.logger.info("**************test_invalid_admin_login started ******************************* ******************************")
        self.driver = setup1
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.implicitly_wait(10)
        error_message=self.driver.find_element(By.XPATH,"//li").text
        if error_message=="No customer account found":
            self.logger.info("**************test_No customer account found text matched ******************************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("**************test_No customer account found text not matched ******************************")
            self.driver.close()
            assert False



