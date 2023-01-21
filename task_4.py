# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# point_a = []
# for i in range(2):
#     point_a.append(int(input('Для точки А введите значения Х, Y (после ввода'
#                             ' каждого значения нажимаем enter): ')))

# point_b = []
# for i in range(2):
#     point_b.append(int(input('Для точки B введите значения Х, Y (после ввода'
#                             ' каждого значения нажимаем enter): ')))

# distance = (((point_b[0] - point_a[0]) ** 2
#              + (point_b[1] - point_a[1]) ** 2) ** (0.5))

# print(f'Расстояние между точками составляет{distance: .3f}')

point_a = []
for i in range(2):
    point_a.append(int(input('Для точки А введите значения Х, Y (после ввода'
                            ' каждого значения нажимаем enter): ')))

point_b = []
for i in range(2):
    point_b.append(int(input('Для точки B введите значения Х, Y (после ввода'
                            ' каждого значения нажимаем enter): ')))

def find_distance(diff, x_1, x_2, y_1, y_2):
    distance = ((diff(x_1, y_1) ** 2 + diff(x_2, y_2) ** 2) ** (0.5))

    print(f'Расстояние между точками составляет{distance: .3f}')

find_distance(lambda x, y: y - x, point_a[0], point_a[1], point_b[0], point_b[1])