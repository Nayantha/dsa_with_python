def partition(arr: list[int], low: int, high: int):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(array: list[int], first_index, last_index: int):
    if first_index > last_index:
        return
    partition_index = partition(array, first_index, last_index)
    quick_sort(array, first_index=first_index, last_index=partition_index - 1)
    quick_sort(array, last_index=last_index, first_index=partition_index + 1)
