def apples(a1):
    # Write code here
    extra_apple=0
    while True:
        if a1%4==0:
            return 0
        a1 =a1 +1
        extra_apple= extra_apple +1    
    return extra_apple   

n= int(input("enter number"))

apples(n)