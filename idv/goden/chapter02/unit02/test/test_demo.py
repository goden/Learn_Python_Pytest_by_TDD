from idv.goden.chapter02.unit02.crud.demo import add_two_number, Calculator


def test_add_two_number():
    num1 = 5
    num2 = 6

    result = add_two_number(num1, num2)
    assert 11 == result


class TestCalculator:
    def test_add(self):
        num1 = 3
        num2 = 5
        calc = Calculator()
        result = calc.add(num1, num2)
        assert 8 == result

    def test_substract(self):
        num1 = 4
        num2 = 11

        calc = Calculator()
        result = calc.substract(num1, num2)

        assert 7 == result

    def test_multiply(self):
        num1 = 3
        num2 = 5
        calc = Calculator()
        result = calc.multiply(num1, num2)
        assert 15 == result

    def test_divide(self):
        num1 = 3
        num2 = 6
        calc = Calculator()
        result = calc.divide(num2, num1)

        assert 2 == result

