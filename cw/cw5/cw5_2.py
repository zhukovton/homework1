import json
import pathlib
import os
# Напишите функцию, сохраняющую информацию о текущей директории  в виде json

path = os.getcwd()
p = pathlib.Path(path)


print(list(p.iterdir()))

dic1 = {}
for i in p.iterdir():
    dic1[i.name] = {"size": i.stat().st_size, "suffix": i.suffix}

print(dic1)

with open("cw5_2.json", "w", encoding="utf-8") as file:
    json.dump(dic1, file, indent=4)

