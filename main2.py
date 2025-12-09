#Завдання 1: Створіть клас BankAccount з атрибутами account_number (номер рахунку) і balance (баланс рахунку), а також методами deposit, який додає певну суму до балансу, і withdraw, який знімає певну суму з балансу. Метод withdraw повинен перевіряти, чи є на рахунку достатньо коштів перед зняттям.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Додано {amount}. Новий баланс: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостатньо коштів на рахунку!"
        self.balance -= amount
        return f"Знято {amount}. Новий баланс: {self.balance}"

    def get_info(self):
        return f"Рахунок: {self.account_number}, Баланс: {self.balance}"

#Завдання 2: Створіть клас Car з атрибутами make (марка автомобіля), model (модель автомобіля) і year (рік випуску автомобіля), а також методом get_info, який повертає рядок з інформацією про автомобіль у форматі "[рік] [марка] [модель]".
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"[{self.year}] {self.make} {self.model}"

car1 = Car("Toyota", "Camry", 2020)
print(car1.get_info())

#Завдання 3: Створіть клас Employee з атрибутами name (ім'я працівника), position (посада працівника) і salary (заробітна плата працівника), а також методом get_salary_info, який повертає рядок з інформацією про заробітну плату у форматі "Заробітна плата [ім'я]: [заробітна плата]".
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"
emp1 = Employee("Ольга", "Менеджер", 50000)
print(emp1.get_salary_info())

#Завдання 4: Створіть клас Rectangle з атрибутами width (ширина прямокутника) і height (висота прямокутника), а також методами calculate_area, який обчислює площу прямокутника, і calculate_perimeter, який обчислює периметр прямокутника.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 20)
print("Площа:", rect.calculate_area())
print("Периметр:", rect.calculate_perimeter())

#Завдання 5: Створіть клас Product з атрибутами name (назва товару), price (ціна товару) і quantity (кількість одиниць товару), а також методами calculate_total_price, який обчислює загальну вартість товарів (ціна * кількість), і display_info, який виводить інформацію про товар.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        return f"Товар: {self.name}, Ціна: {self.price}, Кількість: {self.quantity}"
product1 = Product("Телефон", 55000, 3)

print(product1.display_info())
print("Загальна вартість:", product1.calculate_total_price())
