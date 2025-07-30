# Find the Missing Number
# Leetcode Problem 268

'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

# Brute Force Solution  TC -> o(n^2)   SC -> o(1)
# Logic is to run the loop (0 to n+1) and check nums to find missing value

nums = [1,2,3,4,5,6,8,0]
def missingnumber(nums):
    n = len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
print(missingnumber(nums))


# Better Solution  TC -> o(3N)  SC -> o(N)
# Logic using dictonary 
nums = [1,3,0]
def missingnumbers(nums):
    n = len(nums)
    freq = {}
    for i in range(0,n+1):
        freq[i] = 0
    for num in nums:
        freq[num] = 1
    for k,v in freq.items(): #k,v = Key Value
        if v == 0:
            return k
print(missingnumbers(nums))


# Optimal Solution TC -> o(n)   SC -> o(1)
# Logic is to add number and then subtract the nums 

# Formula to calculate N Natural Numbers = N(N+1) // 2
# Using Sum Function
nums = [1,2,0,4]
def missing(nums):
    n = len(nums)
    original_Total = (n*(n+1)) // 2
    return original_Total - sum(nums)

print(missing(nums))

# Using Loop
nums = [1,2,0,4,3]
def missing_no(nums):
    n = len(nums)
    n_sums = (n*(n+1)) // 2
    sum = 0
    for i in nums:
        sum = sum + i
    missing_number = n_sums - sum
    return missing_number

print(missing_no(nums))
