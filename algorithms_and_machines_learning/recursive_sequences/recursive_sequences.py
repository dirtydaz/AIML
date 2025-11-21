# Recursive Sequences

# 1 Start at 5, generate each term by multiplying the previous term by 3 and subtracting 3
def five_x_3_4_first_n(n):
    nums = [5]
    while len(nums) < n:
        prev_num = nums[-1]
        next_num = prev_num*3-4
        nums.append(next_num)
    
    return(nums)

def five_x_3_4_nth(n):
    if n == 1:
        return 5  
    else:
        prev_term = five_x_3_4_nth(n-1)
        return prev_term * 3 - 4
    
# Collatz
def collatz_terms(n):
    nums = [25]
    while len(nums) < n:
        prev_num = nums[-1]
        if prev_num % 2 == 0:
            next_num = int(prev_num / 2)
            nums.append(next_num)
        else:
            next_num = prev_num * 3 + 1
            nums.append(next_num)
    return nums

def collatz_nth(n):
    if n == 1:
        return 25
    else:
        prev_term = collatz_nth(n-1)
        if prev_term % 2 == 0:
            return int(prev_term / 2)
        else:
            return prev_term * 3 + 1


# Fibonacci
def fib_terms(n):
    nums = [0,1]
    while len(nums) < n+2:
        nums.append(nums[-1]+nums[-2])
    return nums
    

def fib_nth(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        prev_term_1 = fib_nth(n-1)
        prev_term_2 = fib_nth(n-2)
        return prev_term_1 + prev_term_2
    
# Fibonacci Product
def fib_prod_terms(n):
    nums = [2,-3]
    while len(nums) < n:
        nums.append(nums[-1]*nums[-2])
    return nums

def fib_prod_nth(n):
    if n == 1:
        return 2
    if n == 2:
        return -3
    else:
        prev_term_1 = fib_prod_nth(n-1)
        prev_term_2 = fib_prod_nth(n-2)
        return prev_term_1 * prev_term_2