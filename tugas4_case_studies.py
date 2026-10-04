from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Membuka Firefox
driver = webdriver.Firefox()

# Membuka website
driver.get("https://ultimateqa.com/automation/")
driver.maximize_window()

time.sleep(2)

# Mencari menu Case Studies
case_studies = driver.find_element(By.LINK_TEXT, "Case Studies")

# Mengarahkan mouse ke Case Studies
ActionChains(driver).move_to_element(case_studies).perform()

time.sleep(2)

print("Mouse over pada Case Studies berhasil dilakukan!")

input("Tekan Enter untuk menutup browser...")

driver.quit()