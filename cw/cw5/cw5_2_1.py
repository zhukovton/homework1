import json
import csv
import pathlib
import os
# Записать json в csv

with open("cw5_2.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(data)

list1 = []
for k, v in data.items():
    list1.append({"file_name": k, "size": v["size"], "suffix": v["suffix"]})


with open("../practika/jsonToCsv.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["file_name", "size", "suffix"])
    writer.writeheader()  # запишет названия полей
    # writer.writerow({"name": "vlad", "age": 22, "grade": "middle"})
    writer.writerows(list1)
