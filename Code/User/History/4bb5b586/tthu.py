n= int(input("enter number"))

number_list=[]

for num in range(n-1):
    number= input("enter winter numbers")
    number_list.append(number)
new_number_list = number_list.split(" ")

print(number_list)
for num_1 in new_number_list:
    if num_1 ==num_1[::-1]:
        print("palindromes")