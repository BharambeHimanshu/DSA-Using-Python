# Maximum Subaaray

# Leetcode Problem 53 (Medium Level)

'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# Brute Force Solution  TC -> o(n(n+1))//2   SC -> o(1)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def MaximumArray(nums):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0,n):
        total = 0        # Every time i+1 the total value will reset
        for j in range(i,n):
            total = total + nums[j]  #Calculate Total
            maxi = max(total,maxi)   #Select Maximum Value
    return maxi

print(MaximumArray(nums))


# Optimal Solution Using concept kadane's Algorithm   TC -> o(n)   SC -> o(1)
# Here if the value of total is in negative just reset to 0

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maximum_subarray(nums):
    n = len(nums)
    maxi = float("-inf")
    total = 0
    for i in range(0,n):
        total = total + nums[i]
        maxi = max(total,maxi)
        if total <  0:
            total = 0   #reset total if value is in -
    return maxi

print(maximum_subarray(nums))
