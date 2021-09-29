from selenium import webdriver

from Pages.Registration_Page import Registration_Page
from Pages.Login_Page import Login_Page
import names
import time

path = "C://Users//kumar//PycharmProjects//TestSample\\Drivers\\chromedriver.exe"
url = "https://qa-practical.qa.swimlane.io/"


def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_login_url():
    driver = webdriver.Chrome(
        executable_path=path)
    # Set up test case data

    # Search for the phrase
    login_page = Login_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    print("Done TC#1")


def test_login_page():
    driver = webdriver.Chrome(executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    registration_page.verify_login_success()
    print("Done TC#2")


def test_registration_error_message():
    driver = webdriver.Chrome(executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_username_password("anil.kumar", "JobPassword123!@#")
    registration_page.verify_login_success()
    registration_page.verify_error_message(names.get_first_name(gender=None))
    print("Done TC#3")


def test_create_new_record():
    driver = webdriver.Chrome(
        executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_username_password("anil.kumar", "JobPassword123!@#")
    registration_page.verify_login_success()
    registration_page.create_new_employee(names.get_first_name(gender=None), names.get_last_name(), "USA")
    print("Done TC#4")


test_create_new_record()
test_login_url()
test_login_page()
test_registration_error_message()
