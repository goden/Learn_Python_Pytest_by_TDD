import pytest

from idv.goden.chapter03.unit01.demo.Calculator import add, divide

def test_add():
    # verify the correct result
    num1 = 10
    num2 = 20

    result = add(num1, num2)

    assert result == 30

def test_divide():

    num1 = 10
    num2 = 20

    result = divide(num1, num2)

    assert result == 0.5

    with pytest.raises(ZeroDivisionError) as exec:
        num1 = 10
        num2 = 0

        print(exec.value)
        assert isinstance(exec.value, ZeroDivisionError)

