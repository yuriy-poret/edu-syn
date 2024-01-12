import math


CONS_DIV = '-----------------------------------------------'
NUM_MAX = 2_000_000_000

while True:
    print(CONS_DIV)
    ans = input(f'Пожалуйста, введите натуральное число (должно быть <= {NUM_MAX}): ')
    if ans.isdigit():
        num = int(ans)
        if num <= NUM_MAX:
            break

res = 0
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        res += 1
        if i != num // i: # NOTE: Чтобы избежать дублирования.
            res += 1

print(CONS_DIV)
print(f'Кол-во делителей указанного числа: {res}')
print(CONS_DIV)
