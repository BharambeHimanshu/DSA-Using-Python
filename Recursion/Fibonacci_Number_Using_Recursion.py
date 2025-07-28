# Fibonacci Number Using Recursion

#Logic
# f(7) = f(6) + f(5)
# f(n) = f(n-1) + f(n-2)

def func(num):
    if num == 0 or num == 1: # Base Condition
        return num
    return func (num - 1) + func(num - 2) # Flow
    
print(func(7))