#To find the Factors of Number
# Brute force solution 

num = 20

result = []
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)
print(result)

#Better solution

num = 10

result = []
for i in range(1,num // 2):
    if num % 2 == 0:
        result.append(i)
result.append(num)
print(result)


#Optimal solution

from math import sqrt
num = 36
result = []
for i in range(1,int(sqrt(num)+1)):
    if num % i ==0:
        result.append(i)
        if num//i != i :
            result.append(num//i)
result.sort()
print(result)
