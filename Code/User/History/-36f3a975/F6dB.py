def largest_divisible_by_three(n_str):
    # Convert string to a list of characters so we can modify it
    digits = list(n_str)    
    n = len(digits)
    print(digits)
    # Calculate the initial sum of digits
    current_sum = sum(int(d) for d in digits)
    print(current_sum)
    
    # Step 1: Try to increase a digit from left to right to make it larger
    for i in range(n):
        original_digit = int(digits[i])
        
        # Try replacing the current digit with the largest possible digit (9 down to original+1)
        for target in range(9, original_digit, -1):
            # Check if changing to this target digit makes the total sum divisible by 3
            if (current_sum - original_digit + target) % 3 == 0:
                digits[i] = str(target)
                return "".join(digits)
                
    # Step 2: If we couldn't increase any digit (e.g., "999"), we MUST still change exactly 
    # one digit. To keep the number as large as possible, we modify the rightmost digit.
    print(n)
    for i in range(n - 1, -1, -1):
        print(i)
        original_digit = int(digits[i])
        
        # Try reducing the current digit (from original-1 down to 0)
        for target in range(original_digit - 1, -1, -1):
            if (current_sum - original_digit + target) % 3 == 0:
                digits[i] = str(target)
                return "".join(digits)

# Test with your example
input_num = "123"
output_num = largest_divisible_by_three(input_num)
print(f"Input: {input_num}")
print(f"Output: {output_num}")

input_num = "999"
output_num = largest_divisible_by_three(input_num)
print(f"Input: {input_num}")
print(f"Output: {output_num}")