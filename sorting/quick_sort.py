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
    arr[pivot_element_index], arr[left_pointer] = arr[left_pointer],arr[pivot_element_index]
    return left_pointer

def quick_sort(array: list[int]):
    ...
