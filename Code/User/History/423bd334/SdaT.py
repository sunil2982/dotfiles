arr = [8,10,12,26,2,6,44,89,56,123,]
"""
n = len(arr)

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            min=j
            arr[i],arr[min]= arr[min],arr[i]

print(arr)
"""

def selection_one_sort(arr):
    n= len(arr)
    min =arr[0]
    temp = 0
    for i in range(n):
        if arr[min] > arr[i]:
            min =i
            arr[min],arr[i] =arr[i], arr[min]
    print(arr)