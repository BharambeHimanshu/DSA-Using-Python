# Two Sum 
# Leetcode Problem 1

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Brute Force Solution  TC -> o(n(n+1)) // 2      SC -> o(1)

nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13
def TwoSum(nums, target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
            
print(TwoSum(nums,target))


#Optimal Solution Using hashmap

nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 20
def Twosum(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return[hash_map[remaining],i]
        hash_map[nums[i]] = i
        
print(Twosum(nums,target))

