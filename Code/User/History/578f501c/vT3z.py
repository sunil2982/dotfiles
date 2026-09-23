def digit(a):
 def digit(a1):
       
    k = 1
    current_length = 0
    while True:
        block_str = "".join(str(i) for i in range(1, k + 1))
        if current_length + len(block_str) >= a1:
            rem = a1 - current_length - 1
            return int(block_str[rem])
        current_length += len(block_str)
        k += 1