def partition(arr: list[int], left_pointer: int, right_pointer: int):
    pivot_element = arr[right_pointer]
    pivot_element_index = right_pointer
    while True:
        while pivot_element >= arr[left_pointer] and left_pointer < right_pointer:
            left_pointer += 1
        if left_pointer >= right_pointer:
            break
        while pivot_element < arr[right_pointer] and left_pointer < right_pointer:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
    arr[pivot_element_index], arr[left_pointer] = arr[left_pointer], arr[pivot_element_index]
    return left_pointer

def quick_sort(array: list[int], first_index, last_index: int):
    if first_index > last_index:
        return
    partition_index = partition(array, first_index, last_index)
    quick_sort(array, first_index=first_index, last_index=partition_index - 1)
    quick_sort(array, last_index=last_index, first_index=partition_index + 1)
