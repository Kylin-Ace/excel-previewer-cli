# 🧰 Excel Previewer CLI Tool (Python)

A simple Python-based command-line tool to preview Excel files directly in the terminal. Great for analyzing Excel sheets quickly without opening Excel, and perfect for automating Excel inspection workflows.

---

## 🚀 Features

- Preview the first few rows of any `.xlsx` Excel file
- Optionally show all sheets in a workbook
- Supports custom number of preview rows
- Clean, readable output for terminal use
- Great for automation and data wrangling tasks

---

## 📁 Files Included

| File Name             | Description |
|-----------------------|-------------|
| `excel_parser.py`     | 🧠 Main CLI tool – preview Excel content via terminal |
| `generate_dummy_data.py` | 🏭 Generates `dummy_data.xlsx` and `dummy_data.csv` (realistic random data) |
| `generate_sample_data.py` | ✨ Generates `panda1.xlsx` and `sample.xlsx` (simple, clean data) |
| `dummy_data.xlsx`     | 📊 Excel file with realistic fake employee data (Name, Email, Salary, etc.) |
| `dummy_data.csv`      | CSV version of the same data |
| `sample.xlsx`         | 🌈 Simple dataset with 4 rows — Name, Age, City |
| `panda1.xlsx`         | 🐼 Another fake business-style file for testing single-sheet mode |

---

## 💻 How to Use
python excel_parser.py panda1.xlsx --all
python excel_parser.py sample.xlsx --rows 10

---
### ▶️ Basic Preview (first sheet only):
python excel_parser.py sample.xlsx
========================================
First Sheet Data (4 rows, 3 columns)
========================================
     Name  Age      City
0   Alice   25  New York
1     Bob   30    London
2 Charlie   35     Paris
3   Diana   40     Tokyo
```bash
python excel_parser.py dummy_data.xlsx
## 🛠 Requirements

Make sure you have the following installed:

- Python 3.7 or higher
- `pandas` (for data handling)
- `openpyxl` (for working with Excel `.xlsx` files)

### 📦 Install the dependencies:

```bash
pip install pandas openpyxl

