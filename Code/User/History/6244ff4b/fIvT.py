import math

def count_divisors(num):
    """Calculates the total number of divisors for a given number."""
    if num <= 0:
        return 0
    if num == 1:
        return 1
        
    count = 0
    sqrt_num = int(math.isqrt(num))
    
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            # If divisors are equal (e.g., 4*4 = 16), count it once
            if i * i == num:
                count += 1
            else:
                # Otherwise, count both pairs (e.g., 2 and 8 for 16)
                count += 2
    return count

def find_max_divisors():
    # Read the start and end values from input
    start, end = map(int, input().split())
    
    max_divisors = -1
    best_number = -1
    
    # Iterate through the range (inclusive)
    for num in range(start, end + 1):
        current_divisors = count_divisors(num)
        
        # Using strict '>' ensures that if there's a tie, 
        # the smaller (first seen) number is kept.
        if current_divisors > max_divisors:
            max_divisors = current_divisors
            best_number = num
            
    # Output: the number with most divisors, followed by the count of divisors
    print(f"{best_number} {max_divisors}")

if __name__ == "__main__":
    find_max_divisors()


"""
import math
def divisor(num):
    if num==0:
        return 0
    if num == 1:
        return 1
    count= 0
    sqrt_num=int(math.isqrt(num))
    #print(math.isqrt(num))

    for i in range(1,sqrt_num+1):
        if  num % i ==0:
            if  i * i == num:
                count= count +1
            else:
                count = count +2
    #print(count)
    return count

def find_max_divisors():
    start,end = map(int,input().split())
    max_divisor= -1
    best_number = -1

    for num in range(start,end+1):
        current_divisors =  divisor(num)
        if current_divisors > max_divisor:
            max_divisor =current_divisors
            best_number = num
    print(f"{num} {max_divisor}")

if __name__=="__main__":
    find_max_divisors()

"""