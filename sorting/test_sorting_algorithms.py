from sorting.insertion_sort import insertion_sort


def sorting_algorithm_test(sorting_algorithm):
    array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
    unsorted_array = array
    sorting_algorithm(array)
    unsorted_array.sort()
    assert array == unsorted_array


def test_insertion_sort():
    sorting_algorithm_test(insertion_sort)
