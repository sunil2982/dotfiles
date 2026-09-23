a,b=0,1
n= 6

for i in range(n+1):
    if a+b<=n:
        print(b," ",end="")
        a,b = b,a+b 
