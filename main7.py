#Завдання 1
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="info.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

logging.info("Це інформація і дата")



#Завдання2
import logging

logging.basicConfig(
    level=logging.ERROR,
    filename="errors.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    result = 5 / 0
except Exception as e:
    logging.error("Сталася помилка: {e}")

#Завдання 3
def login(username, password):
    try:
        assert username == "admin" and password == "5234", \
            "неправильне ім'я користувача або пароль"
        print("Успішно")
    except AssertionError as e:
        print(e)

login("admin", "5234")
login("user", "0000")


#Завдання 4
def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Дозволено користування")
    except AssertionError as e:
        print(e)



check_age(25)
check_age(10)



#Завдання 5
def process_list(input_list):
    try:
        assert len(input_list) >= 3, \
            "Список повинен містити принаймні 3 елементи"
        print("Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)

process_list([1, 2, 3, 4])
process_list([3])
