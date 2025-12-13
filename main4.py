#Завдання 1: Створи клас "Тварина", який має властивості, спільні для всіх тварин, і потім створи підкласи, наприклад, "Собака" та "Кіт", які успадковують властивості від "Тварини".
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Тварина видає звук")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} каже: Гав!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} каже: Мяу!")



dog = Dog("Джек")
cat = Cat("Муся")

dog.speak()
cat.speak()

#Завдання 2: Створи клас "Особа", який має властивість "ім'я" і метод "вік", а потім створи підкласи "Водій", який додатково має властивість "номер водійського посвідчення".
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"Вік: {self.age}")


class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number



driver = Driver("Сергій", 30, "AB234356")
driver.show_age()
print("Номер посвідчення:", driver.license_number)

#Завдання 3: Створи клас "ТранспортнийЗасіб", з властивістю "швидкість" і методом "переміщення", а потім створи підкласи для різних видів транспорту, які успадковують властивості та методи від "ТранспортногоЗасобу".
class TransportVehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Рухається зі швидкістю {self.speed} км/год")


class Car(TransportVehicle):
    pass


class Bicycle(TransportVehicle):
    pass


class Plane(TransportVehicle):
    def move(self):
        print(f"Летить зі швидкістю {self.speed} км/год")


car = Car(70)
bike = Bicycle(25)
plane = Plane(1000)

car.move()
bike.move()
plane.move()

#Завдання 4: Створи клас "Пристрій", з методами "увімкнути" і "вимкнути", а потім створи підкласи для різних електронних пристроїв, які успадковують методи від "Пристрою".
class Device:
    def turn_on(self):
        print("Пристрій увімкнено")

    def turn_off(self):
        print("Пристрій вимкнено")


class Phone(Device):
    pass


class Laptop(Device):
    pass


phone = Phone()
laptop = Laptop()

phone.turn_on()
laptop.turn_on()
laptop.turn_off()

#Завдання 5: Створи клас "МоваПрограмування", з властивістю "ім'я" і методом "вивести_привітання", а потім створи підкласи для різних мов програмування, які успадковують властивості та методи від "МовиПрограмування".
class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привіт! Це мова програмування {self.name}")


class PythonLang(ProgrammingLanguage):
    pass


class JavaLang(ProgrammingLanguage):
    pass


class CppLang(ProgrammingLanguage):
    pass


python = PythonLang("Python")
java = JavaLang("Java")
cpp = CppLang("C++")

python.say_hello()
java.say_hello()
cpp.say_hello()
