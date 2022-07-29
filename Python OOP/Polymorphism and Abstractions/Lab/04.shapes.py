from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * self.__height + 2 * self.__width


circle = Circle(5)
print(circle.calculate_area())  # 78.53981633974483
print(circle.calculate_perimeter())  # 31.41592653589793
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())  # 200
print(rectangle.calculate_perimeter())  # 60
