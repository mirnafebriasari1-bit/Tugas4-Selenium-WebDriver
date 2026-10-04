from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Membuka Firefox
driver = webdriver.Firefox()

# Membuka website
driver.get("https://ultimateqa.com/automation/")
driver.maximize_window()

time.sleep(2)

# Klik submenu Selenium Resources
driver.find_element(By.LINK_TEXT, "Selenium Resources").click()
time.sleep(2)

print("Menu Education - Selenium Resources berhasil dibuka!")

input("Tekan Enter untuk menutup browser...")

driver.quit()