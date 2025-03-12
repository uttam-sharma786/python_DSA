def insert_sort(arr):
    # Start from the second position (index 1)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1 # reference to the previous element
        
        # Shift elements greater than the current element to the right
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -=1
        
        # Insert the current element at its correct position
        # faliure condition: j = -1
        arr[j + 1] = current
    
    print(f"[{', '.join(map(str, arr))}]")

# Example usage
arr = [1,6,7,4,9,2]
insert_sort(arr)
