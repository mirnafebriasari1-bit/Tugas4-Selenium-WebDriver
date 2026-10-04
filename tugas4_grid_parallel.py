from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import threading
import time


GRID_URL = "http://127.0.0.1:4444"


def jalankan_test(nama_test, aksi):
    options = Options()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    try:
        mulai = time.time()

        driver.get("https://ultimateqa.com/automation/")
        time.sleep(2)

        aksi(driver)

        selesai = time.time()

        print(
            f"[PASS] {nama_test} | "
            f"Durasi: {selesai - mulai:.2f} detik"
        )

    except Exception as e:
        print(f"[FAIL] {nama_test} | {e}")

    finally:
        driver.quit()


def big_page(driver):
    driver.find_element(
        By.LINK_TEXT,
        "Big page with many elements"
    ).click()


def services(driver):
    driver.find_element(
        By.LINK_TEXT,
        "Services"
    ).click()


def blog(driver):
    driver.find_element(
        By.LINK_TEXT,
        "Blog"
    ).click()


print("========================================")
print(" SELENIUM GRID - PARALLEL EXECUTION")
print("========================================")

tests = [
    ("Big Page", big_page),
    ("Services", services),
    ("Blog", blog)
]

threads = []

for nama, aksi in tests:
    thread = threading.Thread(
        target=jalankan_test,
        args=(nama, aksi)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("========================================")
print("Semua pengujian Grid selesai.")
print("========================================")