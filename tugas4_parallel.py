from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time


def test_big_page():
    driver = webdriver.Firefox()
    driver.maximize_window()

    start = time.time()

    try:
        driver.get("https://ultimateqa.com/automation/")
        time.sleep(2)

        driver.find_element(
            By.LINK_TEXT,
            "Big page with many elements"
        ).click()

        time.sleep(2)

        duration = time.time() - start
        print(f"[PASS] Big Page | Duration: {duration:.2f} seconds")

    except Exception as e:
        print(f"[FAIL] Big Page | Error: {e}")

    finally:
        driver.quit()


def test_services():
    driver = webdriver.Firefox()
    driver.maximize_window()

    start = time.time()

    try:
        driver.get("https://ultimateqa.com/automation/")
        time.sleep(2)

        driver.find_element(
            By.LINK_TEXT,
            "Services"
        ).click()

        time.sleep(2)

        duration = time.time() - start
        print(f"[PASS] Services | Duration: {duration:.2f} seconds")

    except Exception as e:
        print(f"[FAIL] Services | Error: {e}")

    finally:
        driver.quit()


def test_blog():
    driver = webdriver.Firefox()
    driver.maximize_window()

    start = time.time()

    try:
        driver.get("https://ultimateqa.com/automation/")
        time.sleep(2)

        driver.find_element(
            By.LINK_TEXT,
            "Blog"
        ).click()

        time.sleep(2)

        duration = time.time() - start
        print(f"[PASS] Blog | Duration: {duration:.2f} seconds")

    except Exception as e:
        print(f"[FAIL] Blog | Error: {e}")

    finally:
        driver.quit()


print("========================================")
print("   PARALLEL EXECUTION SELENIUM")
print("========================================")

# Membuat thread untuk setiap test
thread1 = threading.Thread(target=test_big_page)
thread2 = threading.Thread(target=test_services)
thread3 = threading.Thread(target=test_blog)

start_all = time.time()

# Menjalankan semua test secara bersamaan
thread1.start()
thread2.start()
thread3.start()

# Menunggu semua test selesai
thread1.join()
thread2.join()
thread3.join()

total_duration = time.time() - start_all

print("========================================")
print("Semua test selesai.")
print(f"Total waktu: {total_duration:.2f} seconds")
print("========================================")

input("Tekan Enter untuk menutup...")