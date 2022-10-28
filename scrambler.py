direction = input('Введите ш - шифровать или д - дешифровать: ')
while direction.lower() != 'ш' and direction.lower() != 'д':
    direction = input('Необходимо ввести "ш" или "д": ')

language = input('Введите язык текста р - русский, а - английский: ')
while language.lower() != 'р' and language.lower() != 'а':
    language = input('Введите "р" или "а": ')

if language.lower() == 'р':
    max_step = 32
else:
    max_step = 25

step = input('Введите шаг сдвига: ')
while not step.isdigit() or int(step) < 1 or int(step) > max_step:
    step = input(f'Необходимо ввести число от 1 до {max_step}: ')

def get_min_max_index(char):
    if 65 <= ord(char) <= 90:
        min_digit = 65
        max_digit = 90
    elif 97 <= ord(char) <= 122:
        min_digit = 97
        max_digit = 122
    elif 1040 <= ord(char) <= 1071:
        min_digit = 1040
        max_digit = 1071
    elif 1072 <= ord(char) <= 1103:
        min_digit = 1072
        max_digit = 1103
    return min_digit, max_digit

def encryption(text, step):
    new_text = ''
    for i in text:
        if i.isalpha():
            min_digit, max_digit = get_min_max_index(i)
            if ord(i) + step <= max_digit:
                new_text += chr(ord(i) + step)
            else:
                new_text += chr(min_digit + ord(i) + step - max_digit - 1)
        else:
            new_text += i
    return new_text

def decryption(text, step):
    new_text = ''
    for i in text:
        if i.isalpha():
            min_digit, max_digit = get_min_max_index(i)
            if ord(i) - step >= min_digit:
                new_text += chr(ord(i) - step)
            else:
                new_text += chr(max_digit + 1 - (min_digit - ord(i) + step))
        else:
            new_text += i
    return new_text

if direction.lower() == 'ш':
    print(encryption(input('Введите текст для шифрования: '), int(step)))
else:
    print(decryption(input('Введите текст для дешифрования: '), int(step)))