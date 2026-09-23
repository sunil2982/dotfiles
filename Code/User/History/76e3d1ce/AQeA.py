def LargestNum(n:int):

    """ a  number is divisible by 3 if its digit sum is divisible by 3"""

    # converting integer number in to string
    int_to_str_digit=str(n)
    str_digit_list = list(int_to_str_digit)

    # numbers of digit 
    num_length= len(str_digit_list)
    print(str_digit_list)

    # sum of all digits
    digit_sum= sum([ int(i) for i in str_digit_list])

    #for i in str_digit_list:
       # digit_sum= digit_sum+int(i)
    print(digit_sum)

    # from left to right change digit to maximum number
    for i in range(num_length):
        original_digit = int(str_digit_list[i])
        print(original_digit)

        for target in range(9,original_digit,-1):
            if (digit_sum - original_digit + target) %3 == 0:
                str_digit_list[i] = str(target)
                print(str_digit_list[i])
                print("".join(str_digit_list))
                return
    #  if we could not increase it from left like 999 or 988
    # changing digit  from right

    for i in range(n-1,-1,-1):
        original_digit = str_digit_list[i]
        
        


if __name__ == "__main__":
    LargestNum(123)