n=int(input("enter numbers"))
num_list=[]
num_1 = "123"
num_2 ="123"

for i in range(n):
    nums= input("enter numbes")
    num_list.append(nums)
print(num_list)
for nums in num_list:
    x=nums.split(" ")
    for new_str in x:
        new_str2= new_str[1::] + new_str[0]
        print(new_str2)
        if new_str2 ==new_str[1]:
            print(f"pattern match")
        else:
            print("pattern do not match")

print(num_list)
print(num_1==num_2)