from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time
import os


URL = "https://ultimateqa.com/automation/"
SCREENSHOT_DIR = "screenshots"


os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def buat_driver():
    options = Options()
    return webdriver.Firefox(options=options)


def jalankan_test(nama_test, aksi):
    driver = buat_driver()
    mulai = time.time()

    try:
        driver.get(URL)
        time.sleep(2)

        aksi(driver)

        durasi = time.time() - mulai

        print(
            f"[PASS] {nama_test} | "
            f"Duration: {durasi:.2f} seconds"
        )

        return True

    except Exception as e:
        durasi = time.time() - mulai

        nama_file = (
            nama_test
            .replace(" ", "_")
            .replace("/", "_")
            + ".png"
        )

        screenshot = os.path.join(
            SCREENSHOT_DIR,
            nama_file
        )

        driver.save_screenshot(screenshot)

        print(
            f"[FAIL] {nama_test} | "
            f"Duration: {durasi:.2f} seconds"
        )

        print(f"       Error: {e}")
        print(f"       Screenshot: {screenshot}")

        return False

    finally:
        driver.quit()


def services(driver):
    driver.find_element(
        By.LINK_TEXT, "Services"
    ).click()


def projects(driver):
    driver.find_element(
        By.LINK_TEXT, "Projects"
    ).click()


def case_studies(driver):
    element = driver.find_element(
        By.LINK_TEXT, "Case Studies"
    )
    ActionChains(driver).move_to_element(
        element
    ).perform()


def blog(driver):
    driver.find_element(
        By.LINK_TEXT, "Blog"
    ).click()


def newsletter(driver):
    driver.find_element(
        By.LINK_TEXT, "Newsletter"
    ).click()


def free_courses(driver):
    driver.find_element(
        By.LINK_TEXT, "Free Courses"
    ).click()


def selenium_java(driver):
    driver.find_element(
        By.LINK_TEXT, "Selenium Java"
    ).click()


def selenium_csharp(driver):
    driver.find_element(
        By.LINK_TEXT, "Selenium C#"
    ).click()


def selenium_resources(driver):
    driver.find_element(
        By.LINK_TEXT, "Selenium Resources"
    ).click()


def automation_exercises(driver):
    driver.find_element(
        By.LINK_TEXT, "Automation Exercises"
    ).click()


def big_page(driver):
    driver.find_element(
        By.LINK_TEXT,
        "Big page with many elements"
    ).click()


def about(driver):
    driver.find_element(
        By.LINK_TEXT, "About"
    ).click()


tests = [
    ("Services", services),
    ("Projects", projects),
    ("Case Studies - Mouse Over", case_studies),
    ("Blog", blog),
    ("Newsletter", newsletter),
    ("Free Courses", free_courses),
    ("Selenium Java", selenium_java),
    ("Selenium C#", selenium_csharp),
    ("Selenium Resources", selenium_resources),
    ("Automation Exercises", automation_exercises),
    ("Big Page with many elements", big_page),
    ("About", about)
]


print("========================================")
print("   SELENIUM WEBDRIVER TEST REPORT")
print("             TUGAS 4")
print("========================================")

waktu_mulai = time.time()

hasil = []

for nama, aksi in tests:
    berhasil = jalankan_test(nama, aksi)
    hasil.append(berhasil)


total_waktu = time.time() - waktu_mulai

total_test = len(hasil)
total_pass = sum(hasil)
total_fail = total_test - total_pass


print()
print("========================================")
print("           TEST SUMMARY")
print("========================================")
print(f"Total Test : {total_test}")
print(f"PASS       : {total_pass}")
print(f"FAIL       : {total_fail}")
print(f"Total Time : {total_waktu:.2f} seconds")
print("========================================")