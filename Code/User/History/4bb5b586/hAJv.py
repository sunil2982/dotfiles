def is_winter_number(num_str):
    # Condition 1: Check if it's a palindrome
    if num_str == num_str[::-1]:
        return "YES"
    
    # Condition 2: Check if it's divisible by all of its digits
    # Non-palindromes containing '0' cannot be winter numbers
    if '0' in num_str:
        return "NO"
        
    num_int = int(num_str)
    
    # Check divisibility for every digit
    for digit_char in num_str:
        digit = int(digit_char)
        if num_int % digit != 0:
            return "NO" 
            
    return "YES"

def main():
    # Read the number of rows N
    N = int(input())
    
    # Process N lines of input
    for _ in range(N):
        # Read the whole line, split it by spaces to get individual numbers
        line_numbers = input().split()
        
        # Check and print the result for each number found in this line
        for num in line_numbers:
            print(is_winter_number(num))

# Run the program
if __name__ == "__main__":
    main()
