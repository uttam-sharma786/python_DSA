def selection(arr):
    n = len(arr)
    
    for i in range(n-1): 
        minIndex = i
        
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        if minIndex != i:  # This should be inside the loop
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    return arr

selectionArray = [65, 34, 89, 33, 22]
print(selection(selectionArray))