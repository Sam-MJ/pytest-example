from anotherfunc import func4


def func1(text):
    return text * 3


def func2(number):
    return f"{number} bananas"


def func3():
    return func4()


if __name__ == "__main__":
    print(func3())
