ALLOWED_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWEL_LETTERS = 'aeiou' # NOTE: В задаче про букву "y" не написано, но может её тоже стоит добавить.

def is_allowed_letters(word):
    res = True
    for let in word:
        if not (let in ALLOWED_LETTERS):
            res = False
            break
    return res

def get_consonant_letters_count(word):
    res = 0
    for let in word:
        if not (let in VOWEL_LETTERS):
            res += 1
    return res

while True:
    print('-----------------------------------------------')
    word = input('Пожалуйста, введите слово (маленькими латинскими буквами и только одно): ')
    if is_allowed_letters(word):
        break

vowel_letters = dict.fromkeys(list(VOWEL_LETTERS), 0)

# Определяем кол-во каждой гласной и записываем в словарь.
for key in vowel_letters.keys():
    vowel_letters[key] = word.count(key)

# Определяем общее кол-во гласных.
vowel_letters_count = sum(vowel_letters.values())

# Определяем общее кол-во согласных.
consonant_letters_count = get_consonant_letters_count(word)

print('-----------------------------------------------')
print('Выполнен подсчёт букв в введённом слове.')
print(f'Согласных: {consonant_letters_count}')
print(f'Гласных: {vowel_letters_count}')
for key in vowel_letters.keys():
    print(f'Буква "{key}": {False if vowel_letters[key] == 0 else vowel_letters[key]}')
print('-----------------------------------------------')
