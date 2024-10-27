# Напишите программу для управления списком задач (To-Do List). Программа должна уметь:
# Добавлять новую задачу.
# Удалять задачу по номеру.
# Отмечать задачу как выполненную.
# Выводить список всех задач с указанием их статуса (выполнена/не выполнена)

def show_tasks(filename) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read().split("\n")
    return data


def add_task(filename, task):
    num = len(show_tasks(filename)) + 1
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"\n{num} | {task} | Не выполнено")

def remove_task(filename, d_task):
    data = show_tasks(filename)
    count = 1
    new_data = []
    for i in data:
        if i == "":
            continue
        num, task, status = i.split(" | ")
        if int(num) == d_task:
            continue
        new_data.append(f"{count} | {task} | {status}\n")
        count += 1
    with open(filename, "w", encoding="utf-8") as file:
        for i in new_data:
            file.write(i)

if __name__ == "__main__":
    filename = "todolist.txt"
    print(show_tasks(filename))
    d_task = 3
    remove_task(filename, d_task)
    # add_task(filename, "Создать задачу")
