#Завдання1
people = {
    "Олексій" : "18-24",
    "Вікторія" : "40-50"
}
name = input("Ввести ім'я: ")

try:
    age_group = people[name]
    print(f'Вікова група людини {name}: {age_group}')

except KeyError:
    print("ERROR: людину не знайдено.")

#Завдання 2
try:
    number = input("Введіть число: ")
    number = int(number)
    print(f'Ви ввели число: {number}')

except ValueError:
    print("Помилка")


#Завдання 3
path = input("Введіть шлях до файлу: ")

try:
    with open(path, "r", encoding="utf-8") as file: #скористалась ШІ
        print(file.read())
except FileNotFoundError:
    print("Файл не існує")

#Завдання 4
try:
    import math
    print(math.square(5))
except AttributeError:
    print("Функцію не знайдено в модулі")  #не дуже зрозуміла виконання завдання


