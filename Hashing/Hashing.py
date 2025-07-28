# Hashing

# Brute Force Solution

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,6,67,2]

for x in m:
    count = 0
    for y in n:
        if y == x:
            count += 1
print(count)

# Optimal Solution

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
    for num in m :
        if num < 1 and num > 10:
            print(0)
        else:
            print(hash_list[num])
print(hash_list)
