import pytest

from idv.goden.chapter03.unit01.demo.Calculator import add, divide

def test_add():
    # verify the correct result
    num1 = 10
    num2 = 20

    result = add(num1, num2)

    assert result == 30

# Basic Usage
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

def test_value_error():
    with pytest.raises(ValueError) as exec_info:

        int("abc")

    print(exec_info.value)
    assert "invalid literal" in str(exec_info.value)


class MyError(Exception):
    pass

def fail():
    raise MyError("Oops!")


def test_my_error():
    with pytest.raises(MyError) as exec_info:
        fail()
    assert "Oops!" in str(exec_info.value)

