while True:
    print('-----------------------------------------------')
    num = input('Пожалуйста, введите пятизначное целое число: ')
    if (len(num) == 5) and (num.isdigit()):
        break

print(f'Результат: {((int(num[3]) ** int(num[4])) * int(num[2])) / (int(num[0]) - int(num[1]))}')
