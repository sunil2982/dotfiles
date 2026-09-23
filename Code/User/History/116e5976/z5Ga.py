def selectionSort(arr):
    # Write code here
    n= len(arr)

    for i in range(n-1):
        imax= i
        for j in range(i+1,n):
            
            if arr[j]>arr[imax]:
                imax = j
        arr[i],arr[imax] = arr[imax],arr[i]
    print(arr)
    return arr


selectionSort([5, 7, 2, 9, 1])
selectionSort([3, 1, 2])
selectionSort([64, 25, 12, 22, 11])