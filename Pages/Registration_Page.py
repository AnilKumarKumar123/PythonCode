from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registration_Page:
    user_name = "//input[@id='input-1]"
    password = (By.XPATH, "//input[@id='input-2']")
    login_button = (By.XPATH, "//span[text()='Login']")
    login_text = "//button[text() = 'Continue Anyway']"

    URL = 'https://qa-practical.qa.swimlane.io/'

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        delay = 10  # seconds
        self.browser.maximize_window()
        self.browser.get(url)
        WebDriverWait(self.browser, delay).until(EC.invisibility_of_element((By.XPATH, "//button[text() = 'Continue "
                                                                                       "Anyway']")))

        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, "//button[text() = "
                                                                                           "'Continue Anyway']")))
        self.browser.find_element_by_xpath("//button[text() = 'Continue Anyway']").click()
        WebDriverWait(self.browser, delay).until(EC.invisibility_of_element((By.XPATH, "//button[text() = 'Continue "
                                                                                       "Anyway']")))

    def verify_page_title(self, applicationurltext):
        """ Check if the test passed or failed """
        gettitle = self.browser.title
        assert gettitle == applicationurltext

    def enter_username_password(self, username, password):
        """ Enter username and password """
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-1']")))
        self.browser.find_element_by_xpath("//input[@id='input-1']").send_keys(username)
        self.browser.find_element_by_xpath("//input[@id='input-2']").send_keys(password)
        self.browser.find_element_by_xpath("//span[text()='Login']").click()

    def verify_login_success(self):
        """ verify login success"""

        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='New Employee Submission']")))
        homepageText = self.browser.find_element_by_xpath("//span[text()='New Employee Submission']").text
        assert homepageText == "New Employee Submission"

    def verify_error_message(self, firstname):
        """ verify login success"""
        WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='New Employee Submission']/following::i[1]")))
        self.browser.find_element_by_xpath("//span[text()='New Employee Submission']/following::i[1]").click()
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text() = 'First Name']/following::input[1]")))
        self.browser.find_element_by_xpath("//span[text() = 'First Name']/following::input[1]").send_keys(firstname)
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Save']")))
        self.browser.find_element_by_xpath("//span[text()='Save']").click()
        WebDriverWait(self.browser, 12).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn "
                                                                                          "btn-primary']")))
        self.browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        errormessage = self.browser.find_element_by_xpath(
            "//span[text()='Last Name']/following::div[@class='error-messages'][1]").text
        assert errormessage == "Error: Value must be populated before submitting"

    def create_new_employee(self, firstname, lastname, city):
        """ create new  record"""
        WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='New Employee Submission']/following::i[1]")))
        self.browser.find_element_by_xpath("//span[text()='New Employee Submission']/following::i[1]").click()
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text() = 'First Name']/following::input[1]")))
        self.browser.find_element_by_xpath("//span[text() = 'First Name']/following::input[1]").send_keys(firstname)

        self.browser.find_element_by_xpath("//span[text() = 'Last Name']/following::input[1]").send_keys(lastname)

        self.browser.find_element_by_xpath("//span[text() = 'City']/following::input[1]").send_keys(city)
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Save']")))
        self.browser.find_element_by_xpath("//span[text()='Save']").click()
        WebDriverWait(self.browser, 12).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn "
                                                                                          "btn-primary']")))
        self.browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()


