CONS_DIV = '-----------------------------------------------'
LEN_MAX = 1_000

while True:
    print(CONS_DIV)
    ans = input(f'Пожалуйста, введите строку (длина не более {LEN_MAX}): ')
    if len(ans) <= LEN_MAX:
        print(CONS_DIV)
        break

res = list()
for word in ans.split(' '):
    if word != '':
        res.append(word)

print(*res, end=f'\n{CONS_DIV}')
