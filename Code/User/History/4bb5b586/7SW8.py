n= int(input("enter number"))
palindrome ='NO'
winter_number = 'NO'
number_list=[]

for num in range(n-1):
    number= input("enter winter numbers")

    number_list.append(number)
for num in number_list:
    new_number_list = num.split(" ")

print(new_number_list)

for num_1 in new_number_list:
    if num_1 ==num_1[::-1]:
        print(num_1)
        temp_list=[]
        for i in num_1:
            temp_list.append(i)
            if int(i) ==0:
                continue
            elif int(num_1) % int(i) ==0:
                print("YES")
            else:
                print("NO")



