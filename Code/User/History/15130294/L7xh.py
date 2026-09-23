def countOccurrences(arr):
    # Write code here
    min_val = min(arr)
    max_val = max(arr)

    count_arr = [0] * (max_val +1)
    output_arr= []
    print(len(count_arr))
    for num in arr:
        count_arr[num]= count_arr[num] +1
    arr = count_arr
    print(arr)

    for num in count_arr:
        output_arr[num]=count_arr[] 
        
    return output_arr
    
countOccurrences([2,2,1])
countOccurrences([5])