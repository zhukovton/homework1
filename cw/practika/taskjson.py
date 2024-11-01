import json

slovar = {
    "sdf": "sdff",
    "sdg": {
        "asd": "asdas"
    }
}

# with open(("test.json"), "w", encoding="utf-8") as otp:
#     json.dump(slovar, otp, indent=4)  #записывает json в файл
# json.dumps()    # преобразует в строку

# with open(("test.json"), "r", encoding="utf-8") as data:
#     slovarr = json.load(data)  #возвращает
# print(slovarr)

deserialized: dict = json.loads('{"234":1, "v":[1,2,3]}')
print(deserialized["234"])   




