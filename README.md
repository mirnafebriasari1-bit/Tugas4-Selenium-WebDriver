# Tugas 4 - Selenium WebDriver dengan Python

## Deskripsi

Project ini merupakan implementasi pengujian otomatis menggunakan Selenium WebDriver dengan bahasa pemrograman Python.

Pengujian dilakukan pada website:

https://ultimateqa.com/automation/

Project ini dibuat untuk menerapkan automated testing menggunakan Selenium WebDriver, termasuk pengujian beberapa fitur website, parallel execution, Selenium Grid, test reporting, dan integrasi CI/CD.

## Teknologi yang Digunakan

- Python 3.12.10
- Selenium 4.50.0
- Mozilla Firefox
- Selenium WebDriver
- Selenium Grid
- Python Threading
- GitHub Actions

## Fitur Pengujian

Pengujian yang dilakukan meliputi:

1. Services
2. Projects
3. Case Studies - Mouse Over
4. Blog
5. Newsletter
6. Education - Free Courses
7. Education - Selenium Java
8. Education - Selenium C#
9. Education - Selenium Resources
10. Education - Automation Exercises
11. Big Page with Many Elements
12. About

## Selenium WebDriver

Pengujian dilakukan menggunakan Selenium WebDriver dengan Python sehingga browser dapat dikendalikan secara otomatis melalui kode program.

Pengujian tidak dilakukan secara manual dengan menekan setiap fitur menggunakan mouse, tetapi dijalankan melalui script Python.

## Parallel Execution

Project ini menerapkan parallel execution menggunakan Python threading dan Selenium WebDriver.

Parallel execution memungkinkan beberapa pengujian dijalankan secara bersamaan sehingga proses pengujian dapat dilakukan dengan lebih efisien.

File yang digunakan:

- `tugas4_parallel.py`

## Selenium Grid

Project ini menerapkan Selenium Grid untuk menjalankan pengujian menggunakan Remote WebDriver.

File yang digunakan:

- `tugas4_grid.py`
- `tugas4_grid_parallel.py`
- `tugas4_grid_parallel_lengkap.py`

`Tugas4_grid_parallel_lengkap.py` digunakan untuk menjalankan pengujian 12 fitur secara paralel menggunakan Selenium Grid.

## Test Reporting

Project ini menyediakan test reporting untuk menampilkan hasil pengujian secara lebih lengkap.

Informasi yang ditampilkan meliputi:

- Status PASS/FAIL
- Durasi setiap pengujian
- Pesan error apabila terjadi kegagalan
- Screenshot apabila terjadi kegagalan
- Total jumlah pengujian
- Jumlah pengujian yang PASS
- Jumlah pengujian yang FAIL
- Total waktu pengujian

File yang digunakan:

- `tugas4_reporting.py`
- `tugas4_reporting_lengkap.py`

## CI/CD

Project ini juga menerapkan integrasi CI/CD menggunakan GitHub Actions.

Workflow GitHub Actions digunakan untuk menjalankan pengujian Selenium secara otomatis ketika terdapat perubahan pada repository.

File workflow:

`.github/workflows/selenium.yml`

File pengujian yang digunakan dalam proses CI/CD:

`tugas4_ci.py`

Pengujian CI/CD mencakup 12 fitur utama dan telah berhasil dijalankan.

## File Project

### `tugas4.py`

Program dasar untuk membuka website menggunakan Selenium WebDriver.

### `tugas4_lengkap.py`

Program untuk menjalankan beberapa pengujian Selenium WebDriver secara berurutan.

### `tugas4_reporting.py`

Program untuk menghasilkan laporan pengujian yang berisi status PASS/FAIL, durasi pengujian, error, dan ringkasan hasil.

### `tugas4_reporting_lengkap.py`

Program reporting lengkap untuk 12 fitur pengujian dengan informasi status, durasi, error, screenshot saat pengujian gagal, dan ringkasan hasil.

### `tugas4_parallel.py`

Program untuk menjalankan beberapa pengujian secara paralel menggunakan Python threading dan Selenium WebDriver.

### `tugas4_grid.py`

Program untuk menguji koneksi dan menjalankan Selenium WebDriver melalui Selenium Grid.

### `tugas4_grid_parallel.py`

Program untuk menjalankan beberapa pengujian secara paralel menggunakan Selenium Grid.

### `tugas4_grid_parallel_lengkap.py`

Program untuk menjalankan 12 fitur pengujian secara paralel menggunakan Selenium Grid.

### `tugas4_ci.py`

Program pengujian yang digunakan dalam proses CI/CD GitHub Actions.

## File Pengujian Fitur

File pengujian fitur individual meliputi:

- `tugas4_services.py`
- `tugas4_blog.py`
- `tugas4_education.py`
- `tugas4_selenium_java.py`
- `tugas4_selenium_csharp.py`
- `tugas4_selenium_resources.py`
- `tugas4_automation_exercises.py`
- `tugas4_newsletter.py`
- `tugas4_projects.py`
- `tugas4_case_studies.py`

## Instalasi

Pastikan Python sudah terpasang pada komputer.

Install Selenium menggunakan perintah:

```bash
pip install -r requirements.txt
```
## Menjalankan Pengujian

### Pengujian Dasar

```bash
python tugas4.py
```

### Pengujian Lengkap

```bash
python tugas4_lengkap.py
```

### Test Reporting

```bash
python tugas4_reporting_lengkap.py
```

### Parallel Execution

```bash
python tugas4_parallel.py
```

### Selenium Grid

Pastikan Selenium Grid Server telah dijalankan terlebih dahulu, kemudian jalankan:

```bash
python tugas4_grid.py
```

### Selenium Grid dengan Parallel Execution

```bash
python tugas4_grid_parallel_lengkap.py
```

## Requirements

Dependencies project terdapat pada file:

`requirements.txt`

Isi utama requirements:

```text
selenium==4.50.0
```

## Struktur Project

```text
Tugas4-Selenium-WebDriver/
│
├── .github/
│   └── workflows/
│       └── selenium.yml
│
├── README.md
├── requirements.txt
│
├── tugas4.py
├── tugas4_lengkap.py
├── tugas4_ci.py
│
├── tugas4_reporting.py
├── tugas4_reporting_lengkap.py
│
├── tugas4_parallel.py
│
├── tugas4_grid.py
├── tugas4_grid_parallel.py
├── tugas4_grid_parallel_lengkap.py
│
├── tugas4_services.py
├── tugas4_blog.py
├── tugas4_education.py
├── tugas4_selenium_java.py
├── tugas4_selenium_csharp.py
├── tugas4_selenium_resources.py
├── tugas4_automation_exercises.py
├── tugas4_newsletter.py
├── tugas4_projects.py
└── tugas4_case_studies.py
```

## Repository GitHub

Repository project:

https://github.com/mirnafebriasari1-bit/Tugas4-Selenium-WebDriver

## Hasil Pengujian

Pengujian Selenium WebDriver telah berhasil dilakukan pada fitur-fitur yang telah ditentukan.

Pengujian Selenium Grid dengan parallel execution juga telah berhasil dijalankan.

Test reporting berhasil menampilkan hasil pengujian berupa status PASS/FAIL, durasi pengujian, dan ringkasan hasil.

Integrasi CI/CD menggunakan GitHub Actions juga telah berhasil dijalankan.

## Author

**Mirna Febriasari**

**NIM: H071241078**

**Universitas Hasanuddin**

## About

Tugas 4 - Selenium WebDriver menggunakan Python.
