"""Module contains function with algorithm binary search."""
from typing import Optional


def binary_search(array_search: list, value_search: int) -> Optional[int]:
    left = 0
    right = len(array_search) - 1
    while left <= right:
        middle = (left + right) // 2
        value = array_search[middle]
        if value == value_search:
            return middle
        elif value > value_search:
            right = middle - 1
        else:
            left = middle + 1
    return None


array = [1, 3, 5, 7, 9]
binary_search(array, 7)
