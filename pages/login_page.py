from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com"  # أو أي موقع بدك تفحصه

        # المعرفات (Locators)
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        # كتابة البيانات
        wait.until(EC.presence_of_element_located(self.email_field)).send_keys(username)
        wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)

        # الضغط على زر الدخول
        wait.until(EC.element_to_be_clickable(self.login_button)).click()

    # دالة تصوير الشاشة
    def take_screenshot(self, name):
        self.driver.save_screenshot(f"{name}.png")
        print(f"📸 Screenshot saved as: {name}.png")
