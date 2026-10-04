from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Membuka Firefox
driver = webdriver.Firefox()

# Membuka halaman Automation Practice
driver.get("https://ultimateqa.com/automation/")

# Memaksimalkan browser
driver.maximize_window()

# Menunggu halaman tampil
time.sleep(2)

# Menampilkan judul halaman
print("Judul halaman:", driver.title)

# Mencari dan klik "Big page with many elements"
driver.find_element(By.LINK_TEXT, "Big page with many elements").click()

# Menunggu halaman terbuka
time.sleep(2)

print("Big page with many elements berhasil dibuka!")

# Menunggu sebelum browser ditutup
input("Tekan Enter untuk menutup browser...")

driver.quit()