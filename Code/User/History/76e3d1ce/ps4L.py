def LargestNum(n:int):
    int_to_str_digit=str(n)
    str_digit_list = list(int_to_str_digit)
    print(str_digit_list)
    digit_sum=0
    for i in str_digit_list:
        digit_sum= digit_sum+int(i)
    print(digit_sum)

if __name__ == "__main__":
    LargestNum(123)