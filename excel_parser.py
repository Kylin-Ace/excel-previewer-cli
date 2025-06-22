import pandas as pd
import argparse

def excel_parser(file_path, show_all=False, preview_rows=5):
    """
    Reads an Excel file and displays its contents.
    Args:
        file_path (str): Path to the Excel file.
        show_all (bool): If True, show all sheets. Otherwise, show only the first sheet.
        preview_rows (int): Number of rows to preview from each sheet.
    """
    try:
        if show_all:
            sheets = pd.read_excel(file_path, sheet_name=None)
            for sheet_name, data in sheets.items():
                print(f"\n{'='*40}\nSheet: {sheet_name} "
                      f"({data.shape[0]} rows, {data.shape[1]} columns)\n{'='*40}")
                print(data.head(preview_rows))
        else:
            data = pd.read_excel(file_path)
            print(f"\n{'='*40}\nFirst Sheet Data "
                  f"({data.shape[0]} rows, {data.shape[1]} columns)\n{'='*40}")
            print(data.head(preview_rows))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Excel file previewer")
    parser.add_argument("file", help="Path to the Excel file")
    parser.add_argument("--all", action="store_true", help="Show all sheets")
    parser.add_argument("--rows", type=int, default=5, help="Number of rows to preview (default: 5)")
    args = parser.parse_args()

    excel_parser(args.file, show_all=args.all, preview_rows=args.rows)

if __name__ == "__main__":
    main()