# Count the Number of bits to flipped to convert start -> goal
# Leetcode 2220
# Approach :- we use XOR Opeartor and then count the number of "1"s

def minBitFlips(start,goal):
    ans = start ^ goal        # XOR Operator
    count = 0
    for i in range(0,32):
        if ans & (1<<i) != 0:  # if ith bit is set (1) , increment count
            count += 1
    return count

print(minBitFlips(3,4))