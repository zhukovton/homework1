# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква,
a = "а значение - код буквы. Напишите преобразование в одну строку."


def uniqod_dict(text: str) -> dict[str, int]:  # после стрелки указывается тип данных который будет на выходе функции
    result = {}
    for i in text:
        result[i] = ord(i)  # код буквы

    return result


print(uniqod_dict(a))




