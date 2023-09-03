def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        current_min_value = arr[i]
        for j in range(i + 1, len(arr)):
            if current_min_value > arr[j]:
                current_min_value = arr[j]
                arr[j], arr[i] = arr[i], arr[j]
