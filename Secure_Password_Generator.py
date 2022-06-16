import random

chars = []
# проверка числа
pwd_quantity = input('Сколько паролей вам нужно сгенерировать? ')
while pwd_quantity.isdigit() == False:
    pwd_quantity = input('Пожалуйста, введите корректное целое число ')
pwd_quantity = int(pwd_quantity)
# проверка числа
pwd_len = input('Какой длины должен быть пароль? ')
while pwd_len.isdigit() == False:
    pwd_len = input('Пожалуйста, введите корректное целое число ')
pwd_len = int(pwd_len)
# y/n
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
if pwd_digits.lower() in ['lf', 'l', 'да', 'д']:
    chars.append("23456789")

# y/n
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
if pwd_uppercase.lower() in ['lf', 'l', 'да', 'д']:
    chars.append("ABCDEFGHIJKMNPQRSTUVWXYZ")

# y/n
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
if pwd_lowercase.lower() in ['lf', 'l', 'да', 'д']:
    chars.append("abcdefghjkmnpqrstuvwxyz")
# y/n
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
if pwd_punctuation.lower() in ['lf', 'l', 'да', 'д']:
    chars.append("!#$%&*+-=?@^_")
# y/n
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')
if pwd_exceptions.lower() in ['n', 'no', 'н', 'нет']:
    chars.append('il1Lo0O')


def generate_password(d_psw, lens, chars):
    for _ in range(d_psw):
        if len(chars) == 0:
            print('Вы не выбрали никаких сомволов')
            break
        else:
            password = []
            for _ in range(lens//len(chars)+1):
                for i in range(len(chars)):
                    if len(password) != lens:
                        password.append(random.choice(chars[i]))
            random.shuffle(password)
            print(*password, sep='')


generate_password(pwd_quantity, pwd_len, chars)
