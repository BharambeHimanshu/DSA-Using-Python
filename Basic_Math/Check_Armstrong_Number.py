#Check if the number is armstong or not
# for example 153 = 1^3 + 5^3 + 3^15
#                 =153
# TC -> o(log10(n))
# SC -> o(1)
n = 153
num = n
total = 0
nod = len(str(n))
while num > 0 :
    ld = num % 10
    total = total + (ld ** nod)
    num = num // 10
print (total == n)