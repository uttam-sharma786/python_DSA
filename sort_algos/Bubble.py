def bubble_sort(arr):
    is_swap = True  # To ensure the loop runs at least once
    while is_swap:
        is_swap = False  # Assume no swaps will happen
        for i in range(len(arr) - 1):  # Loop until second last element
            if arr[i] > arr[i + 1]:
                # Swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swap = True  # Swap occurred, so we need another pass
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))
