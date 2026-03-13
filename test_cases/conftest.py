
import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


# def pytest_addoption(parser):
#    parser.addoption("--browser", action="store", default="Chrome",
#                     help="Specify the browser : chrome or firefox or edge")

@pytest.fixture()
def browser(request):
   return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
   global driver
   if browser == "chrome":
       driver=webdriver.Chrome()
   elif browser == "firefox":
       driver=webdriver.Firefox()
   elif browser == "edge":
       driver=webdriver.Edge()
   else :
       raise ValueError("Unsupported browser")
   return driver


#this one writing just to handle security issue in live website not necessary to write below code

#When we get Captcha check box we can handle using this below package
# pip3 install seleniumbase
from seleniumbase import Driver
@pytest.fixture()
def setup1(browser):
    global driver
    driver = Driver(uc=True,headless=False)
    return driver

###########for pytest html reports ###########
#hook for adding environment info in html report
def pytest_configure(config):

   config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
   config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
   config.stash[metadata_key]['Tester Name'] = 'Basavana Gouda'




