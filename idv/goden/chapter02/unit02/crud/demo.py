def add_two_number(num1: int, num2: int):
    return num1 + num2

class Calculator:

    def add(self, num1: int, num2: int) :
        return num1 + num2

    def substract(self, num1: int, num2: int) :
        if num1 < num2 :
            return num2 - num1
        else:
            return num1 - num2

    def multiply(self, num1: int, num2: int) :
        return num1 * num2

    def divide(self, num1: int, num2: int) :
        if num1 == 0 or num2 == 0 :
            raise ZeroDivisionError

        return num1 / num2