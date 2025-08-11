# Find Minimum in Rotated Sorted Array
# Leetcode problem 153
'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
'''

# Brute Force   TC -> o(N)    SC-> o(1)
# Using for loop

nums = [3,4,5,1,2]
def minimum(nums):
    n = len(nums)
    minimum = float("inf")  # Initialize minimum as infinity
    for i in range(0,n):
        minimum = min(minimum, nums[i])  # Update minimum
    return minimum

print(minimum(nums))

# Optimal solution

nums = [7, 8, 9, 1, 2, 3, 4]

def Minimum(nums):
    n = len(nums)
    low = 0
    high = n - 1
    minimum = float("inf")
    while low <= high:
        mid = (low+high)//2
        if nums[mid]<= nums[high]:   # If right half is sorted
            minimum = min(minimum,nums[mid])  # Update minimum
            high = mid - 1   # Search in left half
        else:
            minimum = min(minimum,nums[low])
            low = mid - 1 # Search in right half
    return minimum

print(Minimum(nums))
