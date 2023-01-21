# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум 
# использование библиотеки Random для и получения случайного int.
# from random import randint

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(number_list)):
#     random_index = randint(0, len(number_list) - 1)
#     temp = number_list[i]
#     number_list[i] = number_list[random_index]
#     number_list[random_index] = temp

# print(number_list)

from random import randint

number_list = '1, 2, 3, 4, 5, 6, 7, 8, 9'

def list_shuffle(num_list):
    for i in range(len(num_list)):
        random_index = randint(0, len(num_list) - 1)
        temp = num_list[i]
        num_list[i] = num_list[random_index]
        num_list[random_index] = temp
    return num_list

data = list(map(int, number_list.split(', ')))
print(list_shuffle(data))
