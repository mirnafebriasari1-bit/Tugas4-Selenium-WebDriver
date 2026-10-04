from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.browser_version = "stable"

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444",
    options=options
)

driver.get("https://ultimateqa.com/automation/")

print("========================================")
print("SELENIUM GRID BERHASIL TERHUBUNG")
print("Judul:", driver.title)
print("URL:", driver.current_url)
print("========================================")

driver.quit()