"""
=== CSV Data Analyzer ===
"""

import os
import csv
import json
import threading


def load_csv(file_path):
    rows = []

    try:
        if not os.path.exists(file_path):
            print(f"Error: File not found {file_path}")
            return rows

        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print(f"Error: File is empty {file_path}")
                return rows

            rows = list(reader)
            return rows

    except PermissionError:
        print(f"Error: Permission denied -> {file_path}")
    except csv.Error as e:
        print(f"Error: Invalid CSV data in {file_path} -> {e}")
    except UnicodeDecodeError:
        print(f"Error: Encoding issue in {file_path} (not valid utf-8)")
    except Exception as e:
        print(f"Unexpected error while reading {file_path} -> {e}")

    return rows


def analyze(column_name, rows):
    if not rows:
        return None

    values = []

    for row in rows:
        value = row.get(column_name)

        if value is None or str(value).strip() == "":
            continue

        try:
            values.append(float(value))
        except (TypeError, ValueError):
            continue

    if not values:
        return None

    return {
        "sum": sum(values),
        "average": sum(values) / len(values),
        "maximum": max(values),
        "minimum": min(values)
    }


def filter_data(condition, rows):
    if not callable(condition):
        raise TypeError("condition must be a callable function")

    return [row for row in rows if condition(row)]


def save_json(output_file, data):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def process_file(file_path, output_file, column_name, condition):
    rows = load_csv(file_path)

    stats = analyze(column_name, rows)
    filtered_rows = filter_data(condition, rows)

    result = {
        "stats": stats,
        "filtered_rows": filtered_rows
    }

    save_json(output_file, result)

    return result


def main():
    file_paths = input("Enter CSV files separated by comma: ").strip().split(",")

    # remove blank file entries
    file_paths = [path.strip() for path in file_paths if path.strip()]

    condition_text = input("Enter filter condition as a lambda expression, e.g. lambda row: row['sales'] > 100: ").strip()

    # Convert text condition safely only if using eval
    # Example:
    # condition = eval(condition_text, {"__builtins__": {}}, {})
    # But safe approach: ask for a callable from code. For demo, use eval.
    condition = eval(condition_text, {"__builtins__": {}}, {})

    json_file = input("Enter JSON output file name: ").strip()
    column_name = input("Enter column name for stats: ").strip()

    threads = []

    for file_path in file_paths:
        t = threading.Thread(
            target=process_file,
            args=(file_path, json_file, column_name, condition)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()