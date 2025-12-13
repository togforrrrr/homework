#Завдання 1: Створіть програму для керування завданнями. Створіть клас Task з атрибутами, такими як назва, опис, дедлайн і стан (виконано/не виконано). Створіть також клас TaskManager, який буде зберігати список завдань і надавати методи для додавання, видалення, відмічення як виконане і виведення списку завдань.
class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"{self.title} | {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def show_tasks(self):
        for task in self.tasks:
            print(task)



manager = TaskManager()
manager.add_task(Task("Домашнє завдання", "Зробити ООП", "27.12.2025"))
manager.add_task(Task("Проєкт", "Здати проєкт", "17.12.2025"))
manager.mark_task_completed("Домашнє завдання")
manager.show_tasks()

#Завдання 2: Реалізуйте систему для онлайн-магазину. Створіть клас Product з властивостями, такими як назва, ціна, наявність тощо. Створіть клас Cart для управління кошиком покупця з методами для додавання товарів, видалення, підрахунку загальної вартості тощо.
class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.available:
            self.items.append(product)
        else:
            print("Товар недоступний")

    def remove_product(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_cart(self):
        for item in self.items:
            print(f"{item.name} - {item.price} грн")
        print("Загальна сума:", self.total_price(), "грн")


cart = Cart()
cart.add_product(Product("Ноутбук", 45000))
cart.add_product(Product("Мишка", 500))
cart.show_cart()

#Завдання 3: Напишіть програму для керування банківськими рахунками. Створіть клас BankAccount з атрибутами, такими як ім'я власника, номер рахунку та баланс. Створіть клас Bank для здійснення операцій з рахунками, таких як поповнення, зняття коштів, перекази між рахунками.
class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
            else:
                print("Недостатньо коштів для переказу")



bank = Bank()
acc1 = BankAccount("Олег", "123", 1000)
acc2 = BankAccount("Оля", "456", 500)

bank.add_account(acc1)
bank.add_account(acc2)
bank.transfer("123", "456", 300)

print(acc1.balance)
print(acc2.balance)

#Завдання 4: Розробіть систему для керування персоналом компанії. Створіть клас Employee з властивостями, такими як ім'я, посада, заробітна плата тощо. Створіть клас Department, який буде містити список співробітників і методи для додавання, видалення співробітників і підрахунку загальної заробітної плати відділу.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def show_employees(self):
        for emp in self.employees:
            print(f"{emp.name} - {emp.position} - {emp.salary} грн")



dept = Department("IT")
dept.add_employee(Employee("Степан", "Програміст", 30000))
dept.add_employee(Employee("Олена", "Тестувальник", 25000))

dept.show_employees()
print("Загальна зарплата:", dept.total_salary(), "грн")


