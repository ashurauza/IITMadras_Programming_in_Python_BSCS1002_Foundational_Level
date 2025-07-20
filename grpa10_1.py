class Calculator:
    def __init__(self, a, b):  # Corrected constructor method
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b  # Fixed operator

    def multiply(self):
        return self.a * self.b  # Fixed operator

    def subtract(self):
        return self.a - self.b  # Fixed operator

    def quotient(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a // self.b  # Integer division

    def remainder(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a % self.b
