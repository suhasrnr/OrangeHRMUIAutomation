from selenium import webdriver
from Login import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox(executable_path="/Users/Shared/WebDrivers/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
signIn = LoginPage(driver, "Admin", "admin123")
signIn.execute()
time.sleep(5)
welcomeElement = driver.find_element_by_id("welcome")
ac = ActionChains(driver)
ac.move_to_element(welcomeElement)
ac.click().perform()
tenSecWait = WebDriverWait(driver,10)
logoutElement = tenSecWait.until(EC.presence_of_element_located((By.LINK_TEXT,"Logout")))
logoutElement.click()