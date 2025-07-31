# Max Consecutive Ones  (Easy Level)
# Leetcode Problem 485

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output:2
'''


nums = [1,1,1,0,0,1,1,1,1,0]

def maxconsecutivenumber(nums):
    count = 0
    max_count = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            count +=1
        else:
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)

print(maxconsecutivenumber(nums))