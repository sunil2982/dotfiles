def selectionSort(arr):
    # Write code here
    n = len(arr)
    for i in range(n-1):
        imin = i
        for j in range(i+1,n):
            if abs(arr[j]) < abs(arr[imin]):
                imin=j
        
            elif abs(arr[j]) == abs(arr[imin]) and arr[j] <arr[imin]:
                imin =j
                

        arr[i],arr[imin] = arr[imin],arr[i]

    print(arr)
    return arr

selectionSort([-3,1,-2,4])