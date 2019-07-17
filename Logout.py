from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class LogoutPage:
	def __init__(self, driver):
		self.driver = driver
	def execute(self):
		welcomeElement = self.driver.find_element_by_id("welcome")
		time.sleep(5)
		ac = ActionChains(self.driver)
		ac.move_to_element(welcomeElement)
		ac.click().perform()
		tenSecWait = WebDriverWait(self.driver,10)
		logoutElement = tenSecWait.until(EC.presence_of_element_located((By.LINK_TEXT,"Logout")))
		logoutElement.click()
