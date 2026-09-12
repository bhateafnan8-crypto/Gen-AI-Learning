"""
=== CSV Data Analyzer ===
"""

import os
import csv
import json
import threading


def load_csv(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Error: File not found -> {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print(f"Error: File is empty -> {file_path}")
                return []

            return list(reader)

    except PermissionError:
        print(f"Error: Permission denied -> {file_path}")
    except csv.Error as e:
        print(f"Error: Invalid CSV data in {file_path} -> {e}")
    except UnicodeDecodeError:
        print(f"Error: Encoding issue in {file_path} (not valid utf-8)")
    except Exception as e:
        print(f"Unexpected error while reading {file_path} -> {e}")

    return []


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

    filtered_rows = []

    for row in rows:
        try:
            if condition(row):
                filtered_rows.append(row)
        except KeyError:
            continue
        except (TypeError, ValueError):
            continue

    return filtered_rows


def save_json(output_file, data):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: could not save JSON -> {e}")


def process_file(file_path, output_file, column_name, condition):
    rows = load_csv(file_path)

    if not rows:
        return {
            "stats": None,
            "filtered_rows": []
        }

    stats = analyze(column_name, rows)
    filtered_rows = filter_data(condition, rows)

    result = {
        "stats": stats,
        "filtered_rows": filtered_rows
    }

    save_json(output_file, result)
    return result


def main():
    file_paths_input = input("Enter CSV files separated by comma: ").strip()
    file_paths = [path.strip() for path in file_paths_input.split(",") if path.strip()]

    condition_text = input(
        "Enter filter condition as a lambda expression, e.g. lambda row: float(row.get('amount', 0)) > 200: "
    ).strip()

    # eval with safe namespace
    condition = eval(
        condition_text,
        {"__builtins__": {}, "float": float, "int": int, "str": str},
        {}
    )

    json_file = input("Enter JSON output file name: ").strip()
    column_name = input("Enter column name for stats: ").strip()

    threads = []

    for file_path in file_paths:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = f"{base_name}_{json_file}"

        t = threading.Thread(
            target=process_file,
            args=(file_path, output_file, column_name, condition)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()