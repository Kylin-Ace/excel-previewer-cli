# Excel Previewer CLI

A lightweight **Python command-line tool** for quickly previewing Excel workbooks from the terminal.

Instead of opening a spreadsheet application just to inspect a workbook, the tool lets you preview rows, inspect sheets, and control how much data is displayed.

## Features

- Preview the first rows of an `.xlsx` workbook
- Inspect all sheets in a workbook
- Choose the number of preview rows
- Clean terminal output
- Useful for quick data inspection and automation workflows

## Tech Stack

- **Python**
- **pandas**
- **openpyxl**

## Usage

Preview the first sheet:

```bash
python excel_parser.py sample.xlsx
```

Preview a specific number of rows:

```bash
python excel_parser.py sample.xlsx --rows 10
```

Show all sheets:

```bash
python excel_parser.py panda1.xlsx --all
```

## Installation

Install the dependencies with:

```bash
pip install pandas openpyxl
```

## Why I Built It

This project was a practical exercise in Python scripting, command-line interfaces, file handling, and working with structured spreadsheet data.

## Repository

https://github.com/Kylin-Ace/excel-previewer-cli
