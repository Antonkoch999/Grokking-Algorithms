"""Module contains function with algorithm quick sort."""
import random


def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    else:
        random_element = random.choice(array)
        less = [el for el in array if el < random_element]
        greater = [el for el in array if el > random_element]
        middle = [random_element] * array.count(random_element)
        return quick_sort(less) + middle + quick_sort(greater)


print(quick_sort([5, 3, 6, 6, 2, 10]))
