class Point_7:
    """
    Клас для представлення точки на площині з обмеженнями координат.
    """

    __x: float = 0.0
    __y: float = 0.0
    __point_count: int = 0

    def __init__(self, x: float, y: float):
        """Конструктор для ініціалізації координат точки."""
        self.set_x(x)
        self.set_y(y)
        Point_7.__point_count += 1

    def __del__(self):
        """Деструктор, який виводить повідомлення про видалення точки."""
        print(f"Point ({self.__x}, {self.__y}) has been deleted.")
        Point_7.__point_count -= 1

    def get_x(self):
        """Метод-геттер для координати X."""
        return self.__x

    def set_x(self, value: float):
        """Метод-сеттер для координати X з перевіркою діапазону."""
        if -100 <= value <= 100:
            self.__x = value
        else:
            self.__x = 0.0

    def get_y(self):
        """Метод-геттер для координати Y."""
        return self.__y

    def set_y(self, value: float):
        """Метод-сеттер для координати Y з перевіркою діапазону."""
        if -100 <= value <= 100:
            self.__y = value
        else:
            self.__y = 0.0

    def shift(self, x_shift: float, y_shift: float):
        """Метод для зміщення точки на вказану величину по осях X та Y."""
        self.set_x(self.get_x() + x_shift)
        self.set_y(self.get_y() + y_shift)

    @staticmethod
    def get_count():
        """Метод класу для отримання кількості створених екземплярів."""
        return Point_7.__point_count
