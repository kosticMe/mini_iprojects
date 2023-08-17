# generator of passwords
from random import choice


# генерация пароля
def generator_of_passwords(amount, length):
    for _ in range(amount):
        for _ in range(length):
            print(choice(chars), end='')
        print()  # перевод строки


# проверка корректности вводимых данных
def valid_num(label):
    num = input(label)
    while not num.isdigit():
        num = input('Нужно ввести целое число ')
    return int(num)


def valid_answer(label):
    valid_answers = ['да', 'нет']
    answer = input(label + ' ')
    while answer not in valid_answers:
        answer = input('Нужно написать одно слово: да или нет ')
    return answer


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
AMBIGUOUS = ' il1Lo0O'  # неоднозначные символы

chars = ''  # доступные символы

# считывание пользовательских данных
amount = valid_num('Количество паролей для генерации: ')
length = valid_num('Длина одного пароля: ')
on_digits = valid_answer('Включать ли цифры? (ответьте да или нет): ')
on_uppercase = valid_answer('Включать ли прописные буквы? (ответьте да или нет): ')
on_lowercase = valid_answer('Включать ли строчные буквы? (ответьте да или нет):  ')
on_symbol = valid_answer('Включать ли специальные символы? (ответьте да или нет): ')
off_ambiguous = valid_answer('Исключить ли неоднозначные символы? (ответьте да или нет): ')

# формироование chars
if on_digits == 'да':
    chars += DIGITS
if on_uppercase == 'да':
    chars += UPPERCASE_LETTERS
if on_lowercase == 'да':
    chars += LOWERCASE_LETTERS
if on_symbol == 'да':
    chars += PUNCTUATION
if off_ambiguous == 'да':
    for c in chars:
        if c in AMBIGUOUS:
            chars.replace(c, '')  # удаление неоднозначных элементов

# генерация
generator_of_passwords(amount, length)