
arr = [4,2,2,8,3,3,1,99,77,33,21]
min_val = min(arr)
print(f"min value: ",min_val)
max_val = max(f"Max value: ",arr)
elements_range = max_val-min_val +1

count_arr = [0] * elements_range

opt_arr = [0] * len(arr)

print(count_arr)
print(opt_arr)

for num in arr:
    count_arr[num-min_val] += 1
    print(f"Count arr: ",count_arr)

for i in range(1,len(count_arr)):
    count_arr[i] = count_arr[i] + count_arr[i-1]

for num in reversed(arr):
    out_arr[count_arr[num-min_val] -1 ] = num