# Дриопитек (Dryopithecus)
# Рамапитек (Ramapithecus)
# Австралопитек (Australopithecus)
# Человек прямоходящий (Homo Erectus)
# Хомо Сапиенс Неандерталец (Homo Sapiens Neanderthalensis)
# Хомо Сапиенс Сапиенс (Homo Sapiens Sapiens)
# Хомо Сапиенс (Homo Sapiens) # NOTE: По заданию, этот этап не включать.

stages_count = 6
result = ''

print(f'Пожалуйста, укажите {stages_count} этапов развития человека (по порядку, от самого раннего).')
# print('Подсказка: Этап 1 будет равен Homo Sapiens Sapiens или Хомо Сапиенс Сапиенс.')
while stages_count > 0:
    result += input(f'Этап {stages_count}: ') + ' => '
    stages_count -= 1

print(result.strip(' =>'))
