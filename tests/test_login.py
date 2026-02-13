from selenium import webdriver
from pages.login_page import LoginPage
import time


def test_login_process():
    # إعداد المتصفح
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # إنشاء كائن من الصفحة
        login_pg = LoginPage(driver)

        # 1. فتح الموقع
        login_pg.load()
        print("Page loaded successfully.")

        # 2. تنفيذ تسجيل الدخول
        # حط بياناتك هون للتجربة
        login_pg.login("dawoud@example.com", "12345678")

        # 3. انتظر قليلاً لتظهر النتيجة
        time.sleep(3)

        # 4. تصوير الشاشة (الخطوة اللي طلبتها)
        # سيتم حفظ الصورة باسم 'login_result.png' في مجلد المشروع
        login_pg.take_screenshot("login_result")

        print("Test finished and screenshot taken!")

    except Exception as e:
        print(f"An error occurred: {e}")
        # إذا صار خطأ، يصور الشاشة عشان تعرف وين المشكلة
        driver.save_screenshot("error_report.png")

    finally:
        # إغلاق المتصفح
        driver.quit()


if __name__ == "__main__":
    test_login_process()
