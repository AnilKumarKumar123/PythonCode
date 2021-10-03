from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:
    user_name = "//input[@id='input-1']"
    password = "//input[@id='input-2']"
    login_button = "//span[text()='Login']"
    login_text = "//button[text() = 'Continue Anyway']"
    login_error_message = " // div[text() = 'Login failed.']"

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        delay = 10  # seconds
        self.browser.maximize_window()
        self.browser.get(url)
        WebDriverWait(self.browser, delay).until(EC.invisibility_of_element((By.XPATH, self.login_text)))
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, self.login_text)))
        self.browser.find_element_by_xpath(self.login_text).click()
        WebDriverWait(self.browser, delay).until(EC.invisibility_of_element((By.XPATH, self.login_text)))

    def verify_page_title(self, applicationurltext):
        """ Check if the test passed or failed """
        gettitle = self.browser.title
        assert gettitle == applicationurltext

    def enter_username_password(self, username, password):
        """ Enter username and password """
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
        self.browser.find_element_by_xpath(self.user_name).send_keys(username)
        self.browser.find_element_by_xpath(self.password).send_keys(password)
        self.browser.find_element_by_xpath(self.login_button).click()

    def verify_invalid_login(self, username):
        """ Enter username and password """
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
        self.browser.find_element_by_xpath(self.user_name).send_keys(username)
        self.browser.find_element_by_xpath(self.login_button).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.login_error_message)))
        login_error_text = self.browser.find_element_by_xpath(self.login_error_message).text
        assert login_error_text == "Login failed."

    def enter_user_name(self, username):
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
        self.browser.find_element_by_xpath(self.user_name).send_keys(username)

    def enter_password(self,password):
        WebDriverWait(self.browser, 8).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
        self.browser.find_element_by_xpath(self.password).send_keys(password)

    def click_submit_button(self):
        self.browser.find_element_by_xpath(self.login_button).click()

    def validate_error_message(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.login_error_message)))
        login_error_text = self.browser.find_element_by_xpath(self.login_error_message).text
        assert login_error_text == "Login failed."



