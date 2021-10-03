import random as r
import time

import names
from selenium import webdriver

from Pages.Login_Page import Login_Page
from Pages.Registration_Page import Registration_Page

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


def generate_random_phone_number():
    ph_no = [r.randint(6, 9)]
    # the first number should be in the range of 6 to 9
    for i in range(1, 10):
        ph_no.append(r.randint(0, 9))

    return ph_no


def test_login_url():
    driver = webdriver.Chrome(
        executable_path=path)
    # Set up test case data

    # Search for the phrase
    login_page = Login_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    print("Done TC#1")
    driver.quit()


def test_login_page():
    driver = webdriver.Chrome(executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_username_password("anil.kumar", "JobPassword123!@#")
    registration_page.verify_login_success()
    print("Done TC#2")
    driver.quit()


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
    driver.quit()


def test_create_new_record():
    driver = webdriver.Chrome(
        executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_username_password("anil.kumar", "JobPassword123!@#")
    registration_page.verify_login_success()
    registration_page.create_new_employee(names.get_first_name(gender=None), names.get_last_name(), "USA",
                                          "TestStreet", "California", "6473333145", "587654",
                                          "test@gmail.com")
    print("Done TC#4")


def test_invalid_login():
    driver = webdriver.Chrome(
        executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_user_name("testSample")
    login_page.enter_password("testSample")
    login_page.click_submit_button()
    login_page.validate_error_message()
    print("Done TC#5")
    driver.quit()


def test_valid_user_name_invalid_password():
    driver = webdriver.Chrome(
        executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_user_name("anil.kumar")
    login_page.enter_password("anil.kumar")
    login_page.click_submit_button()
    login_page.validate_error_message()
    print("Done TC#6")


def test_invalid_user_name_valid_password():
    driver = webdriver.Chrome(
        executable_path=path)
    login_page = Login_Page(driver)
    registration_page = Registration_Page(driver)
    login_page.load(url)
    login_page.verify_page_title("Swimlane")
    login_page.enter_user_name("testusername")
    login_page.enter_password("JobPassword123!@#")
    login_page.click_submit_button()
    login_page.validate_error_message()
    print("Done TC#7")


test_create_new_record()
test_login_url()
test_login_page()
test_registration_error_message()
test_invalid_login()
test_invalid_user_name_valid_password()
test_valid_user_name_invalid_password()
