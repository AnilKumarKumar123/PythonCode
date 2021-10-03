from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registration_Page:
    user_name = "//input[@id='input-1']"
    password = "//input[@id='input-2']"
    login_button = "//span[text()='Login']"
    login_text = "//button[text() = 'Continue Anyway']"
    new_record_submission_button = "//span[text()='New Employee Submission']/following::i[1]"
    first_name_text_box = "//span[text() = 'First Name']/following::input[1]"
    save_button = "//span[text()='Save']"
    time_spend_save_button = "//button[@class='btn btn-primary']"
    submission_error_message = "//span[text()='Last Name']/following::div[@class='error-messages'][1]"
    last_name_text_box = "//span[text() = 'Last Name']/following::input[1]"
    city_text_box = "//span[text() = 'City']/following::input[1]"
    new_employee_submission_button = "//span[text()='New Employee Submission']"
    street_address_text_box = "//span[text() = 'Street Address']/following::textarea[1]"
    state_text_box = "//span[text() = 'State']/following::input[1]"
    telephone_text_box = "//span[text() = 'Telephone']/following::input[1]"
    zip_text_box = "//span[text() = 'Zip']/following::input[1]"
    email_text_box = "//span[text() = 'Email']/following::input[1]"
    text_text_box = "//span[text() = 'Text']/following::input[1]"
    employee_id_text_box = "//span[text() = 'Employee ID']/following::input[1]"
    text_text_box = "//span[text() = 'Text']/following::input[1]"
    hiring_information_label = "//div[text() = 'Hiring Information']"
    status_radio_button = "//input[@type='radio']"

    URL = 'https://qa-practical.qa.swimlane.io/'

    def __init__(self, browser):
        self.browser = browser

    def verify_page_title(self, applicationurltext):
        """ Check if the test passed or failed """
        gettitle = self.browser.title
        assert gettitle == applicationurltext

    def verify_error_message(self, firstname):
        """ verify login success"""
        WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.new_record_submission_button)))
        self.browser.find_element_by_xpath(self.new_record_submission_button).click()
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name_text_box)))
        self.browser.find_element_by_xpath(self.first_name_text_box).send_keys(firstname)
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.save_button)))
        self.browser.find_element_by_xpath(self.save_button).click()
        WebDriverWait(self.browser, 12).until(EC.visibility_of_element_located((By.XPATH, self.time_spend_save_button)))
        self.browser.find_element_by_xpath(self.time_spend_save_button).click()
        submission_errormessage = self.browser.find_element_by_xpath(self.submission_error_message).text
        assert submission_errormessage == "Error: Value must be populated before submitting"

    def verify_login_success(self):
        """ verify login success"""

        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.new_employee_submission_button)))
        homepageText = self.browser.find_element_by_xpath(self.new_employee_submission_button).text
        assert homepageText == "New Employee Submission"

    def create_new_employee(self, firstname, lastname, city, streetaddress, statename, phonenumber, zipcode, email):
        """ create new  record"""
        WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.new_record_submission_button)))
        self.browser.find_element_by_xpath(self.new_record_submission_button).click()
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name_text_box)))
        self.browser.find_element_by_xpath(self.first_name_text_box).send_keys(firstname)
        self.browser.find_element_by_xpath(self.last_name_text_box).send_keys(lastname)
        self.browser.find_element_by_xpath(self.city_text_box).send_keys(city)
        self.browser.find_element_by_xpath(self.email_text_box).send_keys(email)
        self.browser.find_element_by_xpath(self.zip_text_box).send_keys(zipcode)
        self.browser.find_element_by_xpath(self.street_address_text_box).send_keys(streetaddress)
        self.browser.find_element_by_xpath(self.state_text_box).send_keys(statename)
        self.browser.find_element_by_xpath(self.telephone_text_box).send_keys(phonenumber)
        radio_button = self.browser.find_elements_by_xpath(self.status_radio_button)
        radio_button[0].click()
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.save_button)))
        self.browser.find_element_by_xpath(self.save_button).click()
        WebDriverWait(self.browser, 12).until(EC.visibility_of_element_located((By.XPATH, self.time_spend_save_button)))
        self.browser.find_element_by_xpath(self.time_spend_save_button).click()
