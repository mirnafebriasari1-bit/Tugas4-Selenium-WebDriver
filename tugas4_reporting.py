from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Membuat folder screenshot
os.makedirs("screenshots", exist_ok=True)

# Membuka Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Menyimpan hasil pengujian
hasil_test = []


def jalankan_test(nama_test, fungsi_test):
    mulai = time.time()

    try:
        fungsi_test()

        durasi = time.time() - mulai

        hasil_test.append({
            "test": nama_test,
            "status": "PASS",
            "durasi": durasi,
            "error": "-"
        })

        print(f"[PASS] {nama_test} | Duration: {durasi:.2f} seconds")

    except Exception as e:
        durasi = time.time() - mulai

        # Membuat nama screenshot
        nama_file = nama_test.replace(" ", "_") + ".png"
        screenshot = os.path.join("screenshots", nama_file)

        # Mengambil screenshot
        driver.save_screenshot(screenshot)

        hasil_test.append({
            "test": nama_test,
            "status": "FAIL",
            "durasi": durasi,
            "error": str(e),
            "screenshot": screenshot
        })

        print(f"[FAIL] {nama_test} | Duration: {durasi:.2f} seconds")
        print(f"       Error: {e}")
        print(f"       Screenshot: {screenshot}")


def buka_halaman_utama():
    driver.get("https://ultimateqa.com/automation/")
    time.sleep(2)


# =========================
# TEST 1
# =========================
def test_big_page():
    buka_halaman_utama()
    driver.find_element(
        By.LINK_TEXT,
        "Big page with many elements"
    ).click()
    time.sleep(2)


# =========================
# TEST 2
# =========================
def test_services():
    buka_halaman_utama()
    driver.find_element(
        By.LINK_TEXT,
        "Services"
    ).click()
    time.sleep(2)


# =========================
# TEST 3
# =========================
def test_blog():
    buka_halaman_utama()
    driver.find_element(
        By.LINK_TEXT,
        "Blog"
    ).click()
    time.sleep(2)


# =========================
# TEST 4
# =========================
def test_free_courses():
    buka_halaman_utama()
    driver.find_element(
        By.LINK_TEXT,
        "Free Courses"
    ).click()
    time.sleep(2)


# =========================
# TEST 5
# =========================
def test_selenium_java():
    buka_halaman_utama()
    driver.find_element(
        By.LINK_TEXT,
        "Selenium Java"
    ).click()
    time.sleep(2)


# =========================
# MENJALANKAN TEST
# =========================

print("========================================")
print("   SELENIUM WEBDRIVER TEST REPORT")
print("========================================")

jalankan_test("Big Page", test_big_page)
jalankan_test("Services", test_services)
jalankan_test("Blog", test_blog)
jalankan_test("Free Courses", test_free_courses)
jalankan_test("Selenium Java", test_selenium_java)


# =========================
# RINGKASAN
# =========================

print()
print("========================================")
print("           TEST SUMMARY")
print("========================================")

total = len(hasil_test)
passed = sum(1 for hasil in hasil_test if hasil["status"] == "PASS")
failed = total - passed

print(f"Total Test : {total}")
print(f"PASS       : {passed}")
print(f"FAIL       : {failed}")

print()
print("Detail Test:")

for hasil in hasil_test:
    print("----------------------------------------")
    print(f"Test       : {hasil['test']}")
    print(f"Status     : {hasil['status']}")
    print(f"Duration   : {hasil['durasi']:.2f} seconds")
    print(f"Error      : {hasil['error']}")

    if hasil["status"] == "FAIL":
        print(f"Screenshot : {hasil['screenshot']}")

print("========================================")

input("Tekan Enter untuk menutup browser...")

driver.quit()