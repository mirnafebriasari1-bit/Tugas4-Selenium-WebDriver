from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


URL = "https://ultimateqa.com/automation/"


def buat_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def test_fitur(nama, aksi):
    driver = buat_driver()
    try:
        driver.get(URL)
        time.sleep(1)
        aksi(driver)
        time.sleep(1)
        print(f"[PASS] {nama}")
    except Exception as e:
        print(f"[FAIL] {nama}: {e}")
        raise
    finally:
        driver.quit()


def services(driver):
    driver.find_element(By.LINK_TEXT, "Services").click()


def projects(driver):
    driver.find_element(By.LINK_TEXT, "Projects").click()


def case_studies(driver):
    element = driver.find_element(By.LINK_TEXT, "Case Studies")
    ActionChains(driver).move_to_element(element).perform()


def blog(driver):
    driver.find_element(By.LINK_TEXT, "Blog").click()


def newsletter(driver):
    driver.find_element(By.LINK_TEXT, "Newsletter").click()


def free_courses(driver):
    driver.find_element(By.LINK_TEXT, "Free Courses").click()


def selenium_java(driver):
    driver.find_element(By.LINK_TEXT, "Selenium Java").click()


def selenium_csharp(driver):
    driver.find_element(By.LINK_TEXT, "Selenium C#").click()


def selenium_resources(driver):
    driver.find_element(By.LINK_TEXT, "Selenium Resources").click()


def automation_exercises(driver):
    driver.find_element(By.LINK_TEXT, "Automation Exercises").click()


def big_page(driver):
    driver.find_element(
        By.LINK_TEXT, "Big page with many elements"
    ).click()


def about(driver):
    driver.find_element(By.LINK_TEXT, "About").click()


print("========================================")
print("   SELENIUM CI/CD TEST - TUGAS 3")
print("========================================")

test_fitur("Services", services)
test_fitur("Projects", projects)
test_fitur("Case Studies - Mouse Over", case_studies)
test_fitur("Blog", blog)
test_fitur("Newsletter", newsletter)
test_fitur("Free Courses", free_courses)
test_fitur("Selenium Java", selenium_java)
test_fitur("Selenium C#", selenium_csharp)
test_fitur("Selenium Resources", selenium_resources)
test_fitur("Automation Exercises", automation_exercises)
test_fitur("Big Page with many elements", big_page)
test_fitur("About", about)

print("========================================")
print("Semua pengujian CI/CD berhasil.")
print("========================================")