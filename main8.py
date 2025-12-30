#Завдання1
import sqlite3

connection = sqlite3.connect("AnimalKingdom.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_name TEXT,
    animal_type TEXT
)
""")

animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]

cursor.executemany(
    "INSERT INTO Animals (animal_name, animal_type) VALUES (?, ?)",
    animals
)

cursor.execute(""" UPDATE Animals SET animal_name = 'Сокіл' WHERE animal_name = 'Орел'""")

print("Звірі типу 'Ссавець':")
cursor.execute("""
SELECT * FROM Animals
WHERE animal_type = 'Ссавець'
""")
mammals = cursor.fetchall()
for animal in mammals:
    print(animal)


print("\nУсі записи в таблиці Animals:")
cursor.execute("SELECT * FROM Animals")
all_animals = cursor.fetchall()
for animal in all_animals:
    print(animal)


connection.commit()
connection.close()


#Завдання2
import sqlite3

connection = sqlite3.connect("FruitBasket.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Fruits (ID INTEGER PRIMARY KEY AUTOINCREMENT,fruit_name TEXT,color TEXT)""")

fruits = [
    ("Яблуко", "Червоне"),
    ("Банан", "Жовтий"),
    ("Апельсин", "Помаранчевий")
]

cursor.executemany(
    "INSERT INTO Fruits (fruit_name, color) VALUES (?, ?)",
    fruits
)

cursor.execute("""
UPDATE Fruits
SET color = 'Зелене'
WHERE fruit_name = 'Яблуко'
""")

print("Фрукти жовтого кольору:")
cursor.execute("""
SELECT * FROM Fruits
WHERE color = 'Жовтий'
""")
yellow_fruits = cursor.fetchall()
for fruit in yellow_fruits:
    print(fruit)

print("\nУсі фрукти в кошику:")
cursor.execute("SELECT * FROM Fruits")
all_fruits = cursor.fetchall()
for fruit in all_fruits:
    print(fruit)

connection.commit()
connection.close()


