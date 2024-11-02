# Класс «Прямоугольник» наследуется от класса «Геометрическая фигура». Класс должен содержать конструктор по параметрам «ширина», 
# «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета. 
# Класс должен переопределять метод, вычисляющий площадь фигуры.


# Класс для работы с цветом фигуры
class Color:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

# Базовый класс "Геометрическая фигура"
class GeometricShape:
    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочерних классах")

# Класс "Прямоугольник", наследующийся от "Геометрической фигуры"
class Rectangle(GeometricShape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)  # Создаем объект класса "Цвет фигуры"
    
    # Переопределение метода для вычисления площади
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник {self.color} шириной {self.width} и высотой {self.height}, площадь: {self.area()}"

# Пример использования
rect = Rectangle(5, 10, "красный")
print(rect)