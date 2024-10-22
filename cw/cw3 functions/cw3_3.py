# Функция принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def premia_to_float(_str: str):
    return float(_str.replace("%", ""))


def calculate_salary(names: list[str], stavka: [int], premia: [str]) -> dict[str, float]:
    result = {}
    #  zip() - из переданных список, сделает новый кортеж
    data = list(zip(names, stavka, premia))

    for n, s, p in data:
        result[n] = premia_to_float(p) * (s / 100)

    return result


print(calculate_salary(["Ivan", "Tony", "Lucy"], [123, 500000, 100000], ["10%", "500.5%", "1000%"]))
