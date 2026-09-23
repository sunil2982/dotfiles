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
    print(count)
    return count

def find_max_divisors():
    start,end = map(int,input().split())
    max_divisor= -1
    best_number = -1

    for num in range(start,end+1):
        current_divisors =  divisor(num)
        if current_divisors>max_divisor:
            max_divisor =current_divisors
            best_number = num
    print(f"{num} {max_divisor}")