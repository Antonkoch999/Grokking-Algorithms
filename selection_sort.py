"""Module contains function with algorithm selection sort"""


def find_smallest(array: list) -> int:
    smallest = array[0]
    smallest_index = 0
    for index, element in enumerate(array):
        if array[index] < smallest:
            smallest = array[index]
            smallest_index = index
    return smallest_index


def selection_sort(array: list) -> list:
    sort_array = []
    while array:
        smallest = find_smallest(array)
        sort_array.append(array.pop(smallest))
    return sort_array


lst = [5, 3, 6, 2, 10]
selection_sort(lst)
