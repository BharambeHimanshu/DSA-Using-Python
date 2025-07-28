# Check if the number is palindrome
# TC -> o(log10(n))
# SC -> o(1)

n = 1234
num = n
result = 0
while num >0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10
print(n == result)