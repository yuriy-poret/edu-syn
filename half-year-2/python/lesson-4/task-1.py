def format(value):
    result = float(value)
    if result % 1 == 0:
        return int(value)
    else:
        return result

while True:
    print('-----------------------------------------------')
    print('Пожалуйста, укажите стороны прямоугольника.')
    print('- Только целые или вещественные числа.')
    try:
        a = format(input('Сторона A: ').replace(',', '.'))
        b = format(input('Сторона B: ').replace(',', '.'))
        print('-----------------------------------------------')
        break
    except ValueError:
        continue

S = a * b
P = 2 * (a + b)

print(f'Площадь: {format(S)}')
print(f'Периметр: {format(P)}')
print('-----------------------------------------------')
