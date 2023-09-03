from sorting.insertion_sort import insertion_sort


def test_sorting_algorithm(sorting_algorithm):
    array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
    unsorted_array = array
    sorting_algorithm(array)
    unsorted_array.sort()
    assert array == unsorted_array


def test_insertion_sort():
    test_sorting_algorithm(insertion_sort)
