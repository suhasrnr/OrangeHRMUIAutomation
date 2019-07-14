from selenium import webdriver
from Login import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox(executable_path="/Users/Shared/WebDrivers/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
signIn = LoginPage(driver, "Admin", "admin123")
signIn.execute()
welcomeElement = driver.find_element_by_id("welcome")
ac = ActionChains(driver)
ac.move_to_element(welcomeElement)
ac.click().perform()
time.sleep(5)
logoutElement = driver.find_element_by_link_text("Logout")
logoutElement.click()