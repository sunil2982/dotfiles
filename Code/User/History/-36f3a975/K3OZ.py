def largestNum(n):
    digit= []
    for num in str(n):
        digit.append(int(num))
    print(digit)
    lowest = 0
    sorted_list = []
    for i in digit:
        if i>lowest:
            lowest= i
            sorted_list.append(i)
    print(sorted_list)


largestNum(123)
largestNum(762)