# Find a Single Number
# Leetcode 136

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

# Brute Force    
# Approach :- We can do this by using hash_map or sets
nums = [4,1,2,1,2]
def singlenumber(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num,0)+1

    for key in hash_map:
        if hash_map[key] == 1:
            return key
print(singlenumber(nums))


# Optimal Solution       TC -> o(N)           SC ->o(1)
# Using the XOR operator

nums = [2,2,1]
def SingleNumber(nums):
    ans = 0
    for num in nums:
        ans = ans ^ num
    return ans

print(SingleNumber(nums))
