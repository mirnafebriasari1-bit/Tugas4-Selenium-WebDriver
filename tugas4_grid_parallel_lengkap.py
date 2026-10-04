from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time


GRID_URL = "http://127.0.0.1:4444"
URL = "https://ultimateqa.com/automation/"


def buat_driver():
    options = Options()

    return webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )


def jalankan_test(nama_test, aksi):
    driver = buat_driver()
    mulai = time.time()

    try:
        driver.get(URL)
        time.sleep(1)

        aksi(driver)

        durasi = time.time() - mulai
        print(f"[PASS] {nama_test} | Durasi: {durasi:.2f} detik")

    except Exception as e:
        durasi = time.time() - mulai
        print(f"[FAIL] {nama_test} | Durasi: {durasi:.2f} detik | Error: {e}")

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
        By.LINK_TEXT,
        "Big page with many elements"
    ).click()


def about(driver):
    driver.find_element(By.LINK_TEXT, "About").click()


print("========================================")
print(" SELENIUM GRID - PARALLEL EXECUTION")
print("          TUGAS 4 LENGKAP")
print("========================================")

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

threads = []

waktu_mulai = time.time()

for nama, aksi in tests:
    thread = threading.Thread(
        target=jalankan_test,
        args=(nama, aksi)
    )
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


total_waktu = time.time() - waktu_mulai

print("========================================")
print(" SEMUA PENGUJIAN GRID SELESAI")
print(f" Total waktu: {total_waktu:.2f} detik")
print("========================================")