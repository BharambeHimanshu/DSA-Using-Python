# Search in Rotated Sorted Array 2
# Binary Search With duplicates
# Leetcode Problem 81 [Medium Level]

'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''

# Brute Force TC-> o(N)  SC -> o(1)
nums = [2,5,6,0,0,1,2] 
target = 0
def Search(nums,target):
    n = len(nums)
    for i in range(0,n):
        if nums[i] == target:
            return True
    return False

print(Search(nums,target))

# Optimal Solution
nums = [2,5,6,0,0,1,2] 
target = 3

def search(nums,target):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            if nums[low] == nums[mid] == nums[high]: # Check if the low, mid and high has the same element
                low +=1     # if yes, remove the element of low
                high -=1    # remove the element of high
                continue
            if nums[mid]<= nums[high]: # Check if the array is sorted
                if nums[mid]<= target<= nums[high]: # Check if the element is present in sorted array
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low]<= target<= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return False

print(search(nums,target))