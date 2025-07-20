class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and a perimeter of {self.perimeter}')


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")  # Fixed typo: __init__, not _init_
        self.side = side  # Fixed assignment
        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        self.area = self.side ** 2  # Fixed assignment operator

    def compute_perimeter(self):
        self.perimeter = 4 * self.side  # Fixed assignment operator and syntax
