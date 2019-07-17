from selenium import webdriver
from Login import LoginPage
from Logout import LogoutPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path="/Users/Shared/WebDrivers/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
signIn = LoginPage(driver, "Admin", "admin123")
signIn.execute()

ac = ActionChains(driver)
adminElement = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"menu_admin_viewAdminModule")))
ac.move_to_element(adminElement)
ac.perform()

userMgmtElement = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"menu_admin_UserManagement")))
ac.move_to_element(userMgmtElement)
ac.perform()

userElement = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"menu_admin_viewSystemUsers")))
ac.move_to_element(userElement)
ac.click().perform()


#signOut = LogoutPage(driver)
#signOut.execute()
