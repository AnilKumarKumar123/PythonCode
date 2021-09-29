from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:
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