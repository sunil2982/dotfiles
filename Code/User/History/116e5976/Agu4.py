def selectionSort(arr):
    # Write code here
    n= len(arr)

    for i in range(n-1):
        imax= i
        for j in range(i+1,n):
            imax =j
            if arr[j]>arr[imax]:
                imax = j
        arr[i],arr[imax] = arr[imax],arr[i]

    return arr


