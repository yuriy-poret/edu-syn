MINIMUM_INVESTMENT_AMOUNT = 1000

print('-----------------------------------------------')
print('Пожалуйста, введите для каждого инвестора кол-во долларов (целое число).')
mike_dollars_count = int(input('Майкл: '))
ivan_dollars_count = int(input('Иван: '))

res = ''

if mike_dollars_count >= MINIMUM_INVESTMENT_AMOUNT:
    res = 'Mike'

if ivan_dollars_count >= MINIMUM_INVESTMENT_AMOUNT:
    if res == '':
        res = 'Ivan'
    else:
        res = '2'

if res == '':
    if (mike_dollars_count + ivan_dollars_count) >= MINIMUM_INVESTMENT_AMOUNT:
        res = '1'
    else:
        res = '0'

print(res)
print('-----------------------------------------------')