from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com/"
        # تحديد العناصر باستخدام Locators
        self.email_input = (By.ID, "email")
        self.pass_input = (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        # استخدام Explicit Wait بدلاً من time.sleep
        wait = WebDriverWait(self.driver, 10)

        email_field = wait.until(EC.presence_of_element_located(self.email_input))
        email_field.send_keys(username)

        self.driver.find_element(*self.pass_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()