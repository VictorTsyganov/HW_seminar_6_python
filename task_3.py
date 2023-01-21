# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]

# sum_odd_elements = 0

# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum_odd_elements += my_list[i]

# print(sum_odd_elements)

data = '2, 3, 5, 9, 3'

new_list = list(map(int, data.split(', ')))

my_list = [new_list[i] for i in range(len(new_list)) if i % 2 != 0]

print(sum(my_list))