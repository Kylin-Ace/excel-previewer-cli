# Excel Previewer CLI

Inspect an Excel workbook from the terminal. See its dimensions and preview rows without opening a spreadsheet editor.

## Try it

```bash
git clone https://github.com/Kylin-Ace/excel-previewer-cli.git
cd excel-previewer-cli
python -m venv .venv
```

Activate with `source .venv/bin/activate` on macOS or Linux, or `.venv\Scripts\Activate.ps1` in Windows PowerShell. Then run:

```bash
python -m pip install pandas openpyxl
python excel_parser.py sample.xlsx --rows 3
```

```text
========================================
First Sheet Data (4 rows, 3 columns)
========================================
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
```

## Options

| Option | Behavior |
| --- | --- |
| `--rows N` | Preview up to `N` rows per sheet. Defaults to 5. |
| `--all` | Print the name, dimensions, and preview of every sheet. Defaults to the first sheet. |

```bash
python excel_parser.py sample.xlsx --all --rows 2
python excel_parser.py --help
```

The tool uses `argparse` for command-line options and pandas with openpyxl to read `.xlsx` files. Missing files and workbook read errors are reported in the terminal.
