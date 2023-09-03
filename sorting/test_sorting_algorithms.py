from sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
    unsorted_array = array
    insertion_sort(array)
    unsorted_array.sort()
    assert array == unsorted_array
