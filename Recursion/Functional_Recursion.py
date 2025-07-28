# Parametirized and functioal Recursion

# Sum of 1 to N (Parameterized Way)

def func(sum,i,n):
    if i > n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,4)

# Sum of 1 to N (Functional Way)

def func(n):
    if n == 1:
        return 1
    return n+func(n-1)
print (func(5))

# Factorial Number

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
print(factorial(10))
