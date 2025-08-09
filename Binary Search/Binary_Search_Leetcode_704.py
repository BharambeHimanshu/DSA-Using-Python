# Binary Search 
# Leetcode Problem 704
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

# Optimal Solution Using Iterative  TC -> log2(n)     SC -> o(1)
# Here we divide the list my half and remove the part that will dont want

nums = [-1,0,3,5,9,12]
target = 9

def binarysearch(nums):
    n = len(nums)
    low = 0
    high = n-1

    while low < high:
        mid = (low+high) // 2

        if nums[mid] == target :
            return mid      # Target Found , return index
        
        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1 

    return -1               # Target Not found

print(binarysearch(nums))



# Optimal Solution Using Recursion

nums = [-1,0,3,5,9,12]
target = 9

def Binarysearch(nums,low,high):

    if low > high:
        return -1
    
    mid = (low+high) // 2

    if nums[mid] == target:
        return mid
    
    elif nums[mid] < target:
        return Binarysearch(nums,mid+1,high)
    
    else:
        return Binarysearch(nums,low,mid-1)
    
result = Binarysearch(nums,0,len(nums)- 1)
print(result)

