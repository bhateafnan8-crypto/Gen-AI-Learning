# CSV Data Analyzer — Requirement Review and Correct Execution Plan

## Requirement asked by the user/project

The project should implement a CSV analyzer script with the following functions and ideas:

- `load_csv(file_path)` should read CSV files using `csv.DictReader`.
- `analyze(column_name, rows)` should compute statistics like sum, average, maximum, and minimum for a chosen numeric column.
- `filter_data(condition, rows)` should filter rows using a list comprehension or loop-based filtering.
- `save_json(output_file, data)` should save the result into a JSON file.
- `process_file(file_path, output_file, column_name, condition)` should coordinate the full file flow: load rows, analyze, filter, and save JSON.
- `main()` should accept user input, accept multiple CSV files, and process the files using threads.
- Topics covered should include: CSV reading, JSON writing, generator-style row loading, list comprehensions, threading, file existence checks with `os.path.exists`, and error handling.

## What I did wrong earlier

These were the wrong patterns I tried:

1. I kept multiple inconsistent files such as:
   - `analyze.py`
   - `analyzer.py`
   - `analyzecsv.py`
   - `analayzers.py`
   - `csvanalyze.py`

   They overlapped and confused the project structure.

2. I passed a CSV generator directly into JSON saving.

   Wrong idea:
   ```python
   csvData = load_csv(file_path)
   save_json(output_file, csvData)
   ```

   Problem: `load_csv()` should produce a list of row dictionaries, not a generator object that is not directly serializable.

3. I made `process_file()` return before the `stats` object was returned.

   Wrong flow:
   ```python
   csvData = load_csv(file_path)
   stats = analyze(column_name, file_path)
   save_json(output_file, csvData)
   return filter_data(condition, file_path)
   return stats
   ```

   Problem: `return` is executed before `stats` can be returned. Also `analyze()` was written to accept file path instead of rows.

4. I used `eval()` with a namespace that hid `float`.

   Wrong:
   ```python
   condition = eval(condition_text, {"__builtins__": {}}, {})
   ```

   This gave:
   ```python
   NameError: name 'float' is not defined
   ```

5. I used a lambda that referenced `sales` while the file header did not contain that key.

   Wrong input:
   ```text
   lambda row: float(row['sales']) > 200
   ```

   Problem: sample files such as `sales.csv` use headers like `product,category,amount,quantity` and `messy_data.csv` uses `item,category,price,stock`.

6. I attempted to use one lambda condition across many files that have different headers.

   This created `KeyError: 'sales'` when rows from other files lacked the `sales` column.

7. I left the file `csvanalyze.py` empty, and then tried to stitch the solution into multiple different draft scripts.

## Correct execution plan

The right plan is:

1. Use one final clear file, `csvanalyze.py`.
2. Implement `load_csv()` to return a list of row dictionaries safely.
3. Implement `analyze(column_name, rows)` to calculate:
   - `sum`
   - `average`
   - `maximum`
   - `minimum`
4. Implement `filter_data(condition, rows)` so it can safely evaluate a lambda condition over each row and catch `KeyError` / `TypeError` / `ValueError`.
5. Implement `save_json(output_file, data)` to dump the final result dictionary into a JSON file.
6. Implement `process_file(file_path, output_file, column_name, condition)` such that it loads rows once, analyzes the rows, filters the rows, and saves one JSON result.
7. Implement `main()` to accept multiple file names separated by commas and to run one thread per file.
8. Use a safe evaluation environment for the lambda:

   ```python
   condition = eval(condition_text, {"__builtins__": {}, "float": float}, {})
   ```

   and preferably allow only safe functions such as `float` and `int`.

## What happens after the correct execution

If the code is implemented correctly:

- It reads a CSV file into memory rows.
- It calculates numeric stats for the requested column.
- It filters rows using a callable condition.
- It saves all results in JSON.
- It can process multiple CSV files through threads.

## Correct test input example

Use a file with headers that really contain the numeric column selected for stats and filter:

```text
sales.csv
lambda row: float(row.get('amount', 0)) > 200
results.json
amount
```

Or test multiple compatible files by using a column that exists in both files, such as `amount` and `price` only if you adjust the lambda accordingly.

## Final correction summary

The final script should be built as one consistent project file with:

- safe CSV parsing,
- numeric stats computation,
- safe row filtering,
- JSON writing,
- thread-based multi-file processing,
- and user-friendly error handling for missing files, invalid CSV, missing columns, non-numeric values, and JSON write errors.
