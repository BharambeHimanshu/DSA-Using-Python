# Find the first and last occurance
# Leetcode 34
'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''

# Brute force

nums = [5,7,7,8,8,10]
target = 8
def occurance(nums,target):
    n = len(nums)
    last = -1
    first = -1
    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first,last]

print(occurance(nums,target))


# Optimal Solution
# Using lower and upper bound

nums = [5,7,7,8,8,10]
target = 6
class Solution:
    def binarySearchLeft(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1  # Default index if target is not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid  # Update index and continue searching left
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def binarySearchRight(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1  # Default index if target is not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid  # Update index and continue searching right
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def searchRange(self, nums, target):
        ext_left = self.binarySearchLeft(nums, target)
        if ext_left == -1:
            return [-1, -1]  # If first occurrence is not found, target does not exist
        
        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]
    
sol = Solution()
print(sol.searchRange(nums, target))    