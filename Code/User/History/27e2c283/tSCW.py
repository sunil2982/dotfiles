a,b=0,1
n= 3

for i in range(n+1):
    if a+b<=n+1:
        print(b," ",end="")
        a,b = b,a+b 


def factorial(a1):
    a=1
    for i in range(1,a1+1):
        a = a*i
    return a
        