from src import myfunctions


def test_func1():
    assert myfunctions.func1(3) == 9
    assert myfunctions.func1(2) == 6
    assert not myfunctions.func1(5) == 10


def test_func3():
    assert myfunctions.func3() == "aaaaa"
