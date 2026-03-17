# Python Selenium POM Framework 🚀

هذا المشروع عبارة عن هيكل أتمتة (Automation Framework) متكامل تم بناؤه باستخدام **Python** و **Selenium**، مع تطبيق نمط التصميم **Page Object Model (POM)** لضمان سهولة الصيانة وقابلية التوسع.

## 💡 المميزات (Features)
* **Page Object Model:** فصل منطق الاختبار عن عناصر واجهة المستخدم.
* **Scalability:** تصميم يسهل إضافة اختبارات جديدة بسرعة.
* **Readable Code:** استخدام ممارسات البرمجة النظيفة لتسهيل فهم الكود.
* **Dynamic Waiting:** التعامل مع عناصر الويب بمرونة لتجنب فشل الاختبارات (Flaky Tests).

## 🛠 التكنولوجيا المستخدمة (Tech Stack)
* **Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Design Pattern:** Page Object Model (POM)

## 📁 هيكلية المشروع (Project Structure)
* **pages/:** تحتوي على معرفات العناصر (Locators) والعمليات الخاصة بكل صفحة.
* **tests/:** تحتوي على سيناريوهات الاختبار الفعلية.
* **utils/:** الأدوات المساعدة والإعدادات العامة.
* **requirements.txt:** المكتبات اللازمة لتشغيل المشروع.

## 🚀 كيفية التشغيل (Setup & Execution)
1. قم بعمل Clone للمشروع:
   ```bash
   git clone [https://github.com/dawoudmohesen0/Python-Selenium-POM-Framework.git](https://github.com/dawoudmohesen0/Python-Selenium-POM-Framework.git)

   pip install -r requirements.txt
