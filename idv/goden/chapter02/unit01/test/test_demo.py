from idv.goden.chapter02.unit01.demo.demo import add_two_number
from idv.goden.chapter02.unit01.demo.demo import Calculator


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
