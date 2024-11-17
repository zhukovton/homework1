# функция, которая запрашивает ввод, пока не введет валидное

def get_valid_number():
    while True:
        number = input()
        try:
            number = int(number)
        except ValueError:
            print("Введи число")
        else:
            return number


print(get_valid_number())
