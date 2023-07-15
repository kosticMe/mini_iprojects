# Числовая угадайка
from random import randint

print("Добро пожаловать в числовую угадайку")  # Приветствие


def is_valid_n(number):  # Проверка на корректность ввода n
    if n.isdigit() and int(n) > 1:
        return True
    else:
        return False


n = input("Введите максимальное число, которое может быть загадано ")  # Правая граница угадываемого промежутка
while not is_valid_n(n):
    n = input("Введите целое число, большее 1: ")
n = int(n)  # Инициализация  валидного значения n

rand_num = randint(1, n)  # Случайное целое число от 1 до 100
attempts = 1  # Счетчик попыток

print(f"Попробуйте отгадать число от 1 до {n}")


def is_valid_num(input_data):
    if input_data.isdigit() and 1 <= int(input_data) <= n:
        return True
    else:
        return False


def compare_num():
    global rand_num, attempts, n
    while True:
        num = input()
        if is_valid_num(num):
            num = int(num)
            if num < rand_num:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                attempts += 1
            elif num > rand_num:
                print("Ваше число больше загаданного, попробуйте еще разок")
                attempts += 1
            else:
                print(f"Поздравляем, Вы угадали число за {attempts} попыток")
                respond = input(
                    "Хотите сыграть еще? (Ответьте да , если хотите и любой другой текст, в противном случае) ").lower()
                if respond == "да":
                    attempts = 1
                    n = input("Введите максимальное число, которое может быть загадано ")  # Правая граница угадываемого промежутка
                    while not is_valid_n(n):
                        n = input("Введите целое число, большее 1 ")
                    n = int(n)
                    rand_num = randint(1, n)
                    print("Продолжаем! Попробуйте угадать число ")
                    continue
                else:
                    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                break
        else:
            print(f"А может быть все-таки введем целое число от 1 до {n}?")


compare_num()
