def LargestNum(n:int):

    # converting integer number in to string
    int_to_str_digit=str(n)
    str_digit_list = list(int_to_str_digit)
    
    print(str_digit_list)

    # sum of all digits
    digit_sum= sum([ int(i) for i in str_digit_list])

    #for i in str_digit_list:
       # digit_sum= digit_sum+int(i)
    print(digit_sum)



if __name__ == "__main__":
    LargestNum(123)