n= int(input("enter number"))

number_list=[]

for num in range(n-1):
    number= input("enter winter numbers")
    number_list.append(number)

for num_1 in number_list:
    if num_1 ==num_1[::-1]:
        print("palindromes")