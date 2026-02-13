from selenium import webdriver
from pages.login_page import LoginPage
import pytest


def test_facebook_login():
    # إعداد المتصفح
    driver = webdriver.Chrome()
    driver.maximize_window()

    # استخدام الـ Page Object
    login_pg = LoginPage(driver)
    login_pg.load()
    login_pg.login("your_test_email@example.com", "your_secure_password")

    # التأكد من النتيجة (Assertion)
    assert "facebook" in driver.current_url.lower()

    print("Test Passed Successfully!")
    driver.quit()


if __name__ == "__main__":
    test_facebook_login()