class LoginPage:
	def __init__(self, driver, username,password):
		self.driver = driver
		self.username = username
		self.password = password
	def execute(self):
		self.driver.find_element_by_id("txtUsername").send_keys(self.username)
		self.driver.find_element_by_id("txtPassword").send_keys(self.password)
		self.driver.find_element_by_id("btnLogin").click()
