# Check if the string is palindrome or not Using Recursion

s = "ABCDDCBA"
def func(s,left,right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s,left + 1,right -1)
    
print(func(s,0,len(s)-1))

