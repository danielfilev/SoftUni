from abc import ABC, abstractmethod

# This is a test exercise of the Open/Closed Principle


class Shape(ABC):

    @abstractmethod
    def calc_area(self):
        pass


class Triangle(Shape):

    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calc_area(self):
        return self.height * self.base / 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
# Answer was: "The total area is: 12"

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
# Answer should be: "The total area is: 9.0"
