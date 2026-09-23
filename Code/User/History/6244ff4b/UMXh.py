import math
def divisor(num):
    if num==0:
        return 0
    if num == 1:
        return 1
    count= 0
    sqrt_num=int(math.isqrt(num))
    print(math.isqrt(num))

    for i in range(1,sqrt_num+1):
        if  num % i ==0:
            if  i * i == num:
                count= count +1
            else:
                count = count +2
    return count

def max_divisors():
    