from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort


def sorting_algorithm_test(sorting_algorithm):
    array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
    unsorted_array = array
    sorting_algorithm(array)
    unsorted_array.sort()
    assert array == unsorted_array


def test_insertion_sort():
    sorting_algorithm_test(insertion_sort)


def test_selection_sort():
    sorting_algorithm_test(selection_sort)

def test_quick_sort():
    array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
    unsorted_array = array
    quick_sort(array)
    unsorted_array.sort()
    assert array == unsorted_array
