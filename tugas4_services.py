from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Membuka Firefox
driver = webdriver.Firefox()

# Membuka website
driver.get("https://ultimateqa.com/automation/")
driver.maximize_window()

time.sleep(2)

# Membuka Big Page
driver.find_element(By.LINK_TEXT, "Big page with many elements").click()
time.sleep(2)

print("Big page with many elements berhasil dibuka!")

# Kembali ke halaman Automation Practice
driver.back()
time.sleep(2)

# Klik Services
driver.find_element(By.LINK_TEXT, "Services").click()
time.sleep(2)

print("Menu Services berhasil dibuka!")

# Kembali
driver.back()
time.sleep(2)

print("Pengujian selesai!")

input("Tekan Enter untuk menutup browser...")

driver.quit()