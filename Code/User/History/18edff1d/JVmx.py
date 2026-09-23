n=int(input("enter numbers"))
num_list=[]

for i in range(n):
    nums= input("enter numbes")
    num_list.append(nums)
for nums in num_list:
    x=nums.split(" ")
    print(x)

print(num_list)