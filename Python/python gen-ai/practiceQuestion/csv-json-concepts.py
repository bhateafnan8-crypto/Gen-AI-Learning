# CSV — comma separated data
import csv

# Write
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Afnan", 22])

# Read
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON — key-value structured data
import json

# Write
data = {"name": "Afnan", "age": 22}
with open("data.json", "w") as f:
    json.dump(data, f)

# Read
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

    