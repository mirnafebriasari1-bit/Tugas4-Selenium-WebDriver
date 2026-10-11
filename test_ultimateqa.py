import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://ultimateqa.com/automation/"

# Menu yang berpindah ke halaman lain
LINK_MENU = [
    "Services",
    "Projects",
    "Blog",
    "Newsletter",
    "Free Courses",
    "Selenium Java",
    "Selenium C#",
    "Selenium Resources",
    "Big page with many elements",
    "About",
]


@pytest.mark.parametrize(
    "teks",
    LINK_MENU,
    ids=lambda t: t.replace(" ", "_").replace("#", "sharp"),
)
def test_menu_klik(driver, teks):
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, teks)))
    jumlah_tab = len(driver.window_handles)
    link.click()

    # Tunggu: URL pindah di tab yang sama ATAU terbuka tab baru
    wait.until(
        lambda d: len(d.window_handles) > jumlah_tab
        or d.current_url.rstrip("/") != URL.rstrip("/")
    )

    # Kalau terbuka tab baru, pindah ke tab itu
    if len(driver.window_handles) > jumlah_tab:
        driver.switch_to.window(driver.window_handles[-1])

    # Tunggu sampai halaman tujuan punya judul
    wait.until(lambda d: d.title.strip() != "")

    # Assertion 1: URL berbeda dari halaman awal
    assert driver.current_url.rstrip("/") != URL.rstrip("/")
    # Assertion 2: halaman tujuan punya judul
    assert driver.title.strip() != ""


def test_automation_exercises(driver):
    """Link ini mengarah ke halaman Automation Practice itu sendiri."""
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Automation Exercises"))
    )
    link.click()

    wait.until(lambda d: d.title.strip() != "")

    # Assertion 1: tetap di halaman Automation Practice
    assert driver.current_url.rstrip("/") == URL.rstrip("/")
    # Assertion 2: judul halaman sesuai
    assert "Automation Practice" in driver.title


def test_case_studies_hover(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    elemen = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Case Studies"))
    )
    ActionChains(driver).move_to_element(elemen).perform()

    assert elemen.is_displayed()