from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("🚀 جاري تشغيل المتصفح...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print("✅ تم فتح جوجل بنجاح!")
driver.quit()