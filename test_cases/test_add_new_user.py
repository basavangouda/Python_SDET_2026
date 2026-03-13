import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Add_Customer_Page import Add_Customer_Page

#When we get Captcha check box we can handle using this below package
# pip3 install seleniumbase
from seleniumbase import Driver

class Test_03_Add_New_Customer:
    admin_page_url = Read_Config.get_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger=Log_Maker.log_gen()

    @pytest.mark.smoke
    def test_add_new_user(self,setup1):
        self.logger.info("*************************Test_03_Add_new_user **********************")
        self.driver=setup1
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*****************************Login is completed*************")
        self.logger.info("****************************Starting Add new customer Test***************")
        self.add_customer=Add_Customer_Page(self.driver)
        time.sleep(5)
        self.add_customer.click_customers()
        time.sleep(5)
        self.add_customer.click_customers_from_the_menu_options()
        self.add_customer.click_addnew_button()
        self.logger.info("****************************Providing customer Info started***************")
        email=generate_random_email()
        self.add_customer.enter_email_id(email)
        self.add_customer.enter_password_id("Test@123")
        self.add_customer.enter_first_name("BG")
        self.add_customer.enter_last_name("Ashvik")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_companyname("QACircle")
        #self.add_customer.enter_department("Testing")
        self.add_customer.select_checkbox_tax_exempt()
        self.add_customer.select_customers_roles("Guests")
        self.add_customer.select_manager_vendor("Vendor 1")
        self.add_customer.select_active_checkbox()
        self.add_customer.select_customer_must_change_password()
        self.add_customer.enter_admin_comments("Test Admin Comments")
        self.add_customer.click_save_button()
        time.sleep(5)
        #test case validation on success message in body text
        customer_add_success_text="The new customer has been added successfully."
        success_text=self.driver.find_element(By.XPATH,"//span[normalize-space()='The new customer has been added successfully.']").text

        if customer_add_success_text==success_text:
            assert True
            self.logger.info("****************************Test_03_Add_New_Customer is Passed **************")
            self.driver.close()

        else:
            assert False
            self.logger.info("****************************Test_03_Add_New_Customer is Failed **************")
            self.driver.close()


import random
import string


def generate_random_email():
    # Create a random username of 8 characters
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    # Pick a random domain
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    domain = random.choice(domains)

    # Combine into an email
    email = f"{username}@{domain}"
    return email
