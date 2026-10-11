# Tugas 4 - Selenium WebDriver (Python)

Pengujian otomatis website https://ultimateqa.com/automation/ menggunakan
Selenium WebDriver, pytest, Selenium Grid, dan GitHub Actions.

## Teknologi

- Python 3.12
- Selenium 4.49.0
- pytest, pytest-html, pytest-xdist
- Mozilla Firefox

## Menu yang Diuji

Services, Projects, Case Studies (mouse over), Blog, Newsletter,
Free Courses, Selenium Java, Selenium C#, Selenium Resources,
Automation Exercises, Big page with many elements, About.

## Struktur Proyek

- `test_ultimateqa.py` : kumpulan test (12 test)
- `conftest.py` : fixture driver (Firefox lokal atau Selenium Grid) dan screenshot otomatis
- `requirements.txt` : daftar dependensi
- `.github/workflows/selenium.yml` : workflow CI/CD

## Instalasi

```bash
pip install -r requirements.txt
```

## Menjalankan Test (Lokal)

```bash
python -m pytest -v --html=report.html --self-contained-html
```

Hasil: `report.html` dan folder `screenshots/`.

## Menjalankan di Selenium Grid (Paralel)

1. Unduh `selenium-server-4.49.0.jar` dari https://www.selenium.dev/downloads/
2. Jalankan hub:

```bash
java -jar selenium-server-4.49.0.jar hub
```

3. Jalankan node di terminal lain:

```bash
java -jar selenium-server-4.49.0.jar node --detect-drivers true --max-sessions 4
```

4. Jalankan test lewat Grid (PowerShell):

```powershell
$env:GRID_URL="http://127.0.0.1:4444"
python -m pytest -n 4 -v --html=report_grid.html --self-contained-html
Remove-Item Env:GRID_URL
```

Status Grid dapat dilihat di http://localhost:4444

## CI/CD

Workflow GitHub Actions (`.github/workflows/selenium.yml`) menjalankan test
dengan Firefox headless pada setiap push dan pull request ke branch `main`.
Laporan HTML dan screenshot disimpan sebagai artifact `laporan-pengujian`.

## Laporan Pengujian

Laporan HTML berisi status PASS/FAIL, durasi, dan screenshot setiap test.