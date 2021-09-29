from selenium import webdriver

driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')
Url = "https://www.google.com/"
driver.get(Url)
