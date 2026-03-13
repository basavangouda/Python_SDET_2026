import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Search_Customer_Page import Search_Customer_Page

class Test_04_Search_Customer:
    admin_page_url = Read_Config.get_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger=Log_Maker.log_gen()

    @pytest.mark.smoke
    def test_search_customer_by_email(self,setup1):
        self.logger.info("***********************Test_04_001_search_customer_with_email_address Started*****")
        self.driver = setup1
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****Login Completed****")
        self.logger.info("**************Navigating to customer_search_Page*************")
        self.add_customer=Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        time.sleep(5)
        self.add_customer.click_customers_from_the_menu_options()
        self.logger.info("**************Started search_customer_by email*************")
        self.search_customer=Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_email("james_pan@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(5)
        is_email_present = self.search_customer.search_customer_by_email("james_pan@nopCommerce.com")

        if is_email_present== True:

            assert True
            self.logger.info("*************Test_04_001_search_customer_with_email_address Passed*************")
            self.driver.close()
        else:
            self.logger.info("*************Test_04_001_search_customer_with_email_address Failed*************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self,setup1):
        self.logger.info("***********************Test_04_002_search_customer_with_name Started*****")
        self.driver = setup1
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****Login Completed****")
        self.logger.info("**************Navigating to customer_search_Page*************")
        self.add_customer=Add_Customer_Page(self.driver)
        self.driver.refresh()
        time.sleep(5)
        self.add_customer.click_customers()
        time.sleep(5)
        self.add_customer.click_customers_from_the_menu_options()
        self.driver.refresh()
        self.logger.info("**************Started search_customer_by name*************")
        self.search_customer=Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_firstname("Brenda")
        self.search_customer.enter_customer_lastname("Lindgren")
        self.search_customer.click_search_button()
        time.sleep(5)
        is_name_present = self.search_customer.search_customer_by_name("Brenda Lindgren")
        if is_name_present == True:
            assert True
            self.logger.info("*************Test_04_002_search_customer_with_name Passed*************")
            self.driver.close()
        else:
            self.logger.info("*************Test_04_001_search_customer_with_name Failed*************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_name.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_search_customer_by_companyname(self, setup1):
        self.logger.info("***********************Test_04_003_search_customer_with_companyname Started*****")
        self.driver = setup1
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****Login Completed****")
        self.logger.info("**************Navigating to customer_search_Page*************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        time.sleep(5)
        self.add_customer.click_customers_from_the_menu_options()
        self.driver.refresh()
        self.logger.info("**************Started search_customer_by companyname*************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_companyname("3455")
        self.search_customer.click_search_button()
        time.sleep(5)
        is_companyname_present = self.search_customer.search_customer_by_company("3455")
        if is_companyname_present == True:
            assert True
            self.logger.info("*************Test_04_003_search_customer_with_companyname Passed*************")
            self.driver.close()
        else:
            self.logger.info("*************Test_04_003_search_customer_with_companynamename Failed*************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_companyname.png")
            self.driver.close()
            assert False


