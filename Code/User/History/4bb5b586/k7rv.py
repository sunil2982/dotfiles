def is_winter_number(num_str):
    # Condition 1: Check if it's a palindrome
    if num_str == num_str[::-1]:
        return "YES"
    
    # Condition 2: Check if it's divisible by all of its digits
    # First, handle numbers containing '0' (can't divide by zero)
    if '0' in num_str:
        return "NO"
        
    num_int = int(num_str)
    
    # Check divisibility for every digit
    for digit_char in num_str:
        digit = int(digit_char)
        if num_int % digit != 0:
            return print("NO",end="") # Found a digit that doesn't divide it
            
    return print("YES",end="")

def main():
    # Read the number of total rows N
    N = int(input())
    
    # Read and process N rows of inputs
    for _ in range(N):
        # Using strip() to clean up any accidental trailing spaces
        current_num = input().strip()
        
        # Check and print the result immediately for each number
        print(is_winter_number(current_num))

# Run the program
if __name__ == "__main__":
    main()
