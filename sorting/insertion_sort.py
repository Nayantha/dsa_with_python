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
array = [20, 10, 5, 35, 45, 6, 12, 15, 25, 50, 7]
unsorted_array = array
for index, number in enumerate(array):
    ...
unsorted_array.sort()
