CONS_DIV = '-----------------------------------------------'

print(CONS_DIV)
n = int(input('Пожалуйста, укажите сколько чисел вы собираетесь ввести (целое число): '))
print(CONS_DIV)

counter = 0
print(f'Теперь введите {n} чисел (каждое число отбивайте клавишей Enter).')
for i in range(1, n + 1):
    number = int(input(f'Число №{i}: '))
    if number == 0:
        counter += 1

print(CONS_DIV)
print(f'Кол-во чисел равных нулю: {counter}')
print(CONS_DIV)
