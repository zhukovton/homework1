a = input()
# пытаемся что-то делать
try:
    a = int(a)
# исправляем ошибку
except ValueError:
    a = 0
except TypeError:
    a = -1

# редко используется
    # продолжает в случае успешного try
else:
    a /=10
    # отрабатывает во вез случаях
finally:
    a += 10


print(a)
