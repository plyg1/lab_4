import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from Point_7 import Point_7
import math


# Основна функція
def main():
    # пустий масив точок
    points = []
    # Введення координат точок
    # та створення екземплярів класу Point_7
    print("Введіть координати X, Y для 3 точок:")
    for i in range(3):
        try:
            tmp_x = float(input("X{}: ".format(i + 1)))
            tmp_y = float(input("Y{}: ".format(i + 1)))
        except ValueError:
            print("Неправильні значення для точок!")
            exit()
        else:
            tmp_point = Point_7(tmp_x, tmp_y)
            print("Кількість точок: ", Point_7.get_count())
            points.append(tmp_point)
    # Відображення точок до змін
    show_points(points)
    # Обробка точок за варіантом
    task1(points)
    # Відображення точок після змін
    show_points(points)
    # Збереження координат точок у файлі
    save_points(points)


# Функція для обробки точок за варіантом
def task1(list_of3_points):
    """Створити список з трьох точок, порахувати відстань між першою і
    другою, пересунути третю на 25 вправо."""
    point_1 = list_of3_points[0]
    point_2 = list_of3_points[1]
    point_3 = list_of3_points[2]

    # Обчислення відстані
    length = math.sqrt(math.pow(point_2.get_x() - point_1.get_x(), 2) + math.pow(point_2.get_y() - point_1.get_y(), 2))

    # Переміщення третьої точки
    point_3.shift(25.0, 0.0)

    print("Відстань між першою та другою точками = {}".format(length))


# Відображення графічних об'єктів
def show_points(list_of_points):
    # Робота з графіком
    x = [point.get_x() for point in list_of_points]
    y = [point.get_y() for point in list_of_points]
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.show()


# Збереження координат у файл
def save_points(list_of_points):
    with open("output.txt", "w") as f:
        for num, point in enumerate(list_of_points):
            f.write(f"{num + 1} : {point.get_x()};{point.get_y()}\n")
    print("Координати точок збережено у файл output.txt")


if __name__ == '__main__':
    main()
