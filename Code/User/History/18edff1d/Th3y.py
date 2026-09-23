n=int(input("enter numbers"))
num_list=[]

for i in range(n):
    nums= input("enter numbes")
    num_list.append(nums)
for nums in num_list:
    x=nums.split(" ")
    for new_str in x:
        new_str2= new_str[1::] + new_str[0]
        if new_str2 ==new_str[1]:
            print(f"pattern match")
        else:
            print("pattern do not match")

print(num_list)