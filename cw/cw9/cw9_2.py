class MyStr:
    def __init__(self, value):
        self.value = value

    def __add__(self, other: "MyStr"):
        return MyStr(self.value + other.value)

    # Возвращаем объект
    def __repr__(self):
        return f"MyStr({self.value})"



mystr = MyStr("1")
mystr2 = MyStr("2")
print(mystr + mystr2)
