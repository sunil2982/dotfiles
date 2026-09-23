def countOccurrences(arr, k):
    # Write code here
    min_val = min(arr)
    max_val = max(arr)

    count_arr = [0] * k
    print(len(count_arr))
    for num in arr:
        count_arr[num-min_val] =count_arr[num-min_val] +1
    arr = count_arr
    print(arr)
    return arr

countOccurrences([2,2,1],3)
countOccurrences([5],6)