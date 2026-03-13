import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from utilities.custom_logger import Log_Maker


class Add_Customer_Page:

    # Locators from Add Customer Page
    link_customers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_option_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_add_new_xpath="//a[normalize-space()='Add new']"
    text_email_id='Email'
    text_password_id='Password'
    text_fname_id='FirstName'
    text_lname_id='LastName'
    rdo_gender_male_id='Gender_Male'
    rdo_gender_female_id='Gender_Female'
    text_companyname_id='Company'
    text_department_xpath="//select[@id='customer_attribute_1']"
    chekbox_tax_exempt_id='IsTaxExempt'
    text_box_customer_roles_xpath="//ul[@class='select2-selection__rendered']"
    custrole_guests_xpath="//ul[@role='listbox']/li[4]"           #//li[contains(text(),'Guests')]
    custrole_registered_xpath="//ul[@role='listbox']/li[3]"       #//li[contains(text(),'Registered')]
    custrole_forummoderators_xpath ="//ul[@role='listbox']/li[2]" #//li[contains(text(),'Forum Moderators')]
    custrole_administrators_xpath ="//ul[@role='listbox']/li[1]"  #//li[contains(text(),'Administrators')]
    custrole_vendors_xpath ="//ul[@role='listbox']/li[5]"         #//li[contains(text(),'Vendors')]
    dropdown_manager_vendor_id='VendorId'
    checkbox_active_id ='Active'
    checkbox_customermustchangepassword_id ='MustChangePassword'
    text_admin_comments_id ='AdminComment'
    btn_save_xpath="//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver


    def click_customers(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def click_customers_from_the_menu_options(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()

    def click_addnew_button(self):
        self.driver.find_element(By.XPATH, self.link_add_new_xpath).click()

    def enter_email_id(self,email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_password_id(self,password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_first_name(self,firstname):
        self.driver.find_element(By.ID, self.text_fname_id).send_keys(firstname)

    def enter_last_name(self,lastname):
        self.driver.find_element(By.ID, self.text_lname_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdo_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()

    def enter_companyname(self,companyname):
        self.driver.find_element(By.ID, self.text_companyname_id).send_keys(companyname)

    def enter_department(self,department_name):
        self.driver.find_element(By.XPATH,self.text_department_xpath).send_keys(department_name)

    def select_checkbox_tax_exempt(self):
        self.driver.find_element(By.ID, self.chekbox_tax_exempt_id).click()

    def select_customers_roles(self,role):
        self.driver.find_element(By.XPATH, self.text_box_customer_roles_xpath).click()
        time.sleep(5)
        if role=='Guests':
            #First we click here for the registered dropdown default selected
            self.driver.find_element(By.XPATH, self.custrole_registered_xpath).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.custrole_guests_xpath).click()

        elif role=='Administrator':
            self.driver.find_element(By.XPATH, self.custrole_administrators_xpath).click()

        elif role=='Forum Moderators':
            self.driver.find_element(By.XPATH, self.custrole_forummoderators_xpath).click()

        elif role=='Registered':
            pass

        elif role=='Vendor':
            self.driver.find_element(By.XPATH, self.custrole_vendors_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.custrole_administrators_xpath).click()


    def select_manager_vendor(self,value):
        drop_down=Select(self.driver.find_element(By.ID,self.dropdown_manager_vendor_id))
        drop_down.select_by_visible_text(value)

    def select_active_checkbox(self):
        self.driver.find_element(By.ID, self.checkbox_active_id ).click()

    def select_customer_must_change_password(self):
        self.driver.find_element(By.ID, self.checkbox_customermustchangepassword_id ).click()

    def enter_admin_comments(self,comments):
        self.driver.find_element(By.ID, self.text_admin_comments_id).send_keys(comments)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()


