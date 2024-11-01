_lst = [{"name": "Vlad", "age": 25, "adress": "Гагарина"},
        {"name": "Alex", "age": 60, "adress": "Ленина"},
        {"name": "Danila", "age": 40, "adress": "Бекетова"}]


def my_filer(func: callable, _lst):
    new_list = []
    for i in _lst:
        if func(i):  # == True:
            new_list.append(i)
    return new_list


def check_age(x):
    return x.get("age") >= 30


def check_name(y):
    name = y.get("name")
    return (len(name)) >= 5


print(my_filer(check_age, _lst))
print(my_filer(check_name, _lst))
