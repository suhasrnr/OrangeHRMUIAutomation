from selenium import webdriver
from Login import LoginPage
driver = webdriver.Firefox(executable_path="/Users/Shared/WebDrivers/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
signIn = LoginPage(driver, "Admin", "admin123")
signIn.execute()