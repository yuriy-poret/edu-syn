CONS_DIV = '-----------------------------------------------'

def is_palindrome(word):
    lst = [ch.lower() for ch in word]
    return lst == lst[::-1]

while True:
    print(CONS_DIV)
    ans = input('Пожалуйста, введите строку (только одну и без пробелов): ')
    # NOTE: Если нужна проверка только на пробелы: if ' ' not in ans:
    if ans.isalpha():
        print(CONS_DIV)
        break

print('yes' if is_palindrome(ans) else 'no', end=f'\n{CONS_DIV}')
