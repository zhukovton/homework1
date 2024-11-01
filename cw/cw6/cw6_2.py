def modify_list(func: callable, _lst):
    new_lst = []
    for i in _lst:
        new_lst.append(func(i))
    return new_lst

# def int_func(_lst):
#     int(_lst)

_lst = ["danila", "vlad", "lucy"]

print(modify_list(str.capitalize, _lst))
