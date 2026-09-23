def largestNum(n):
    digit= []
    for num in str(n):
        digit.append(int(num))
    print(digit)
    lowest = 0
    sorted_list = []
    n=len(digit)
    for i in range(n):
        for j in range(0,n-i-1):
            if digit[j] > digit[j+1]:
                digit[j],digit[j+1] = digit[j+1],digit[j]
                
    print(digit)


largestNum(123)
largestNum(762)