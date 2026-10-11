import os
import re

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"  # tidak menunggu semua gambar selesai dimuat

    if os.getenv("HEADLESS") == "1":
        options.add_argument("-headless")

    grid_url = os.getenv("GRID_URL")  # kalau diisi -> pakai Selenium Grid
    if grid_url:
        d = webdriver.Remote(command_executor=grid_url, options=options)
    else:
        d = webdriver.Firefox(options=options)

    d.set_window_size(1366, 900)
    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            nama = re.sub(r"[^A-Za-z0-9_-]", "_", item.name)
            driver.save_screenshot(f"screenshots/{report.outcome}_{nama}.png")
            report.extras = getattr(report, "extras", []) + [
                extras.png(driver.get_screenshot_as_base64())
            ]