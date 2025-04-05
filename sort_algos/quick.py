def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            #swap
            arr[i], arr[j] = arr[j], arr[i]
    # find swap of pivot & its value
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

nums = [9, 3, 7, 2, 8, 5]
print(quicksort(nums))  # Output: [2, 3, 5, 7, 8, 9]
