from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Membuka Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Fungsi membuka halaman utama
def buka_halaman_utama():
    driver.get("https://ultimateqa.com/automation/")
    time.sleep(2)

print("=== MULAI PENGUJIAN SELENIUM WEBDRIVER ===")

# 1. Big Page
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Big page with many elements").click()
time.sleep(2)
print("1. Big page berhasil dibuka")

# 2. Services
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Services").click()
time.sleep(2)
print("2. Services berhasil dibuka")

# 3. Blog
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Blog").click()
time.sleep(2)
print("3. Blog berhasil dibuka")

# 4. Free Courses
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Free Courses").click()
time.sleep(2)
print("4. Free Courses berhasil dibuka")

# 5. Selenium Java
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Selenium Java").click()
time.sleep(2)
print("5. Selenium Java berhasil dibuka")

# 6. Selenium C#
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Selenium C#").click()
time.sleep(2)
print("6. Selenium C# berhasil dibuka")

# 7. Selenium Resources
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Selenium Resources").click()
time.sleep(2)
print("7. Selenium Resources berhasil dibuka")

# 8. Automation Exercises
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Automation Exercises").click()
time.sleep(2)
print("8. Automation Exercises berhasil dibuka")

# 9. Newsletter
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Newsletter").click()
time.sleep(2)
print("9. Newsletter berhasil dibuka")

# 10. Projects
buka_halaman_utama()
driver.find_element(By.LINK_TEXT, "Projects").click()
time.sleep(2)
print("10. Projects berhasil dibuka")

# 11. Mouse over Case Studies
buka_halaman_utama()
case_studies = driver.find_element(By.LINK_TEXT, "Case Studies")
ActionChains(driver).move_to_element(case_studies).perform()
time.sleep(2)
print("11. Mouse over Case Studies berhasil dilakukan")

print("=== PENGUJIAN SELESAI ===")

input("Tekan Enter untuk menutup browser...")

driver.quit()