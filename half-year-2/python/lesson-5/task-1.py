while True:
    print('-----------------------------------------------')
    try:
        num = int(input('Пожалуйста, введите целое число: '))
        print('-----------------------------------------------')
        break
    except ValueError:
        continue

res = ''

if num == 0:
    res += 'нулевое'
else:
    res += 'отрицательное ' if num < 0 else 'положительное '
    res += 'четное' if num % 2 == 0 else 'нечетное'

print(f'{res} число')
print('-----------------------------------------------')