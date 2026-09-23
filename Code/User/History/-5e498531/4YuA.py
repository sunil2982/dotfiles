def apples(a1):
    # Write code here
    extra_apple=0
    while True:
        if a1%4==0:
            print(0)
            break
        a1 =a1 +1    
    return extra_apple   

n= int(input("enter number"))

apples(n)