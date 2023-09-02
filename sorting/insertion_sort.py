# int arr[] = {20,10,5,35,45,6,12,15,25,50,7};
#     int n = sizeof(arr)/ sizeof(arr[0]), key;
#     for (int i = 1; i < n; ++i) {
#         key = arr[i];
#         int j = i - 1;
#         for (; j >= 0 && key < arr[j]; --j) {
#             arr[j+1] = arr[j];
#         }
#         arr[j+1] = key;
#     }
def insertion_sort(array_to_be_sorted: list[int]):
    for index in range(1, len(array_to_be_sorted)):
        number = array_to_be_sorted[index]
        search_index = index - 1
        while search_index >= 0 and number < array_to_be_sorted[search_index]:
            search_index -= 1
        array_to_be_sorted[index] = array_to_be_sorted[search_index + 1]
        array_to_be_sorted[search_index + 1] = number


array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
unsorted_array = array
insertion_sort(array)
unsorted_array.sort()
assert array == unsorted_array
