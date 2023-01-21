# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# number = int(input('Введите целое число: '))

# number_list = []

# for i in range(1, number + 1):
#     number_list.append(round(float((1 + 1/i) ** i), 2))

# print(number_list)
# print(f'Сумма {sum(number_list)}')

number = int(input('Введите целое число: '))

number_list = [round(float((1 + 1/i) ** i), 2) for i in range(1, number + 1)]

print(number_list)
print(f'Сумма {sum(number_list)}')