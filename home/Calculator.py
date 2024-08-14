class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Calculator(self.value / other.value)
        else:
            raise ValueError("Division by zero is not possible!")

    def __str__(self):
        return f"{self.value}"


a = Calculator(1)
b = Calculator(2)
result_add = a + b
result_sub = a - b
result_mul = a * b
result_div = a / b

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)
