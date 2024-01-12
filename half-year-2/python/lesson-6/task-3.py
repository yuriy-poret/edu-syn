CONS_DIV = '-----------------------------------------------'

while True:
    print(CONS_DIV, 'Пожалуйста, введите числа A и B.', sep='\n')
    print('- Только целые и A <= B.')
    try:
        print(CONS_DIV)
        a = int(input('Число A: '))
        b = int(input('Число B: '))
        if a <= b:
            print(CONS_DIV)
            break
    except ValueError:
        continue

res = list()
for num in range(a, b + 1):
    if num % 2 == 0:
        res.append(num)

print('Чётные числа на заданном отрезке:', *res, end=f'\n{CONS_DIV}')
