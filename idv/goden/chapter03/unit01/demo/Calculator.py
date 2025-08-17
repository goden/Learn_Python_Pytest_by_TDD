def add(num1: int, num2: int) :
    return num1 + num2

def substract(num1: int, num2: int) :
    if num1 < num2 :
        return num2 - num1
    else:
        return num1 - num2

def multiply(num1: int, num2: int) :
    return num1 * num2

def divide(num1: int, num2: int) :
    if num1 == 0 or num2 == 0 :
        raise ZeroDivisionError
    return num1 / num2