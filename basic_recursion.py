"""Module contains function with algorithm basic recursion."""


def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))


def sum_list(array: list) -> int:
    array_sum = 0
    for item in array:
        if isinstance(item, list):
            array_sum += sum_list(item)
        else:
            array_sum += item
    return array_sum


print(sum_list([1, 2, 3, [4, 5, [6, 7, [8, 9]]]]))
