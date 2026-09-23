arr = [8,10,12,26,2,6,44,89,56,123,]

n = len(arr)

for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            min=j
            arr[i],arr[min]= arr[min],arr[i]

print(arr)
