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
    print(f"this is x",x)

    for new_str in x:
        new_str2= new_str[1::] + new_str[0]
        print(f"thi is new str 2",new_str2)
        print(f"this is new str")

        if new_str2 ==x[1]:
            print(f"pattern match")
        else:
            print("pattern do not match")

print(num_list)
print(num_1==num_2)