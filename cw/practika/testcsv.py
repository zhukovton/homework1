import csv

# with open("test.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     data = list(reader)
#
# print(data)

# with open("test.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for i in reader.reader:
#         print(i)

data = [
    {"name": "vlad", "age": 22, "grade": "middle"},
    {"name": "vlad", "age": 22, "grade": "middle"}
]

with open("new_test.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
    writer.writeheader()  # запишет названия полей
    # writer.writerow({"name": "vlad", "age": 22, "grade": "middle"})
    writer.writerows(data)