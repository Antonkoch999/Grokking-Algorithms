"""Module contains function with algorithm usage strategy divide and rule."""


def divide_into_squares(lenght: int, width: int) -> int:
    greatest_number = lenght if lenght > width else width
    smallest_number = lenght if lenght < width else width
    if greatest_number % smallest_number == 0:
        return smallest_number
    else:
        lenght = smallest_number
        width = greatest_number % smallest_number
        return divide_into_squares(lenght, width)


print(divide_into_squares(1680, 640))
