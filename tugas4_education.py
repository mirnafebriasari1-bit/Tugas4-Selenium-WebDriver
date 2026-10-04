from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Membuka Firefox
driver = webdriver.Firefox()

# Membuka website
driver.get("https://ultimateqa.com/automation/")
driver.maximize_window()

time.sleep(2)

# Klik submenu Free Courses pada bagian Education
driver.find_element(By.LINK_TEXT, "Free Courses").click()
time.sleep(2)

print("Menu Education - Free Courses berhasil dibuka!")

input("Tekan Enter untuk menutup browser...")

driver.quit()