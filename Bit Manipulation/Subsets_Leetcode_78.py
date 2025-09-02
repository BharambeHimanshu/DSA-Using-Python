# Power Set [Print all subsets]      TC -> o(N * 2^n)      SC -> o(1)
# Leetcode 78

'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''


nums = [1,2,3]
def Subset(nums):
    n = len(nums)
    total_subset = 1 << n  # 2^n subsets
    result = []            # List to store all subsets
        
    # Loop through each possible subset mask
    for num in range(total_subset):
        lst = []           # Current subset
        # Check each bit in the mask
        for i in range(0, n):
            if num & (1 << i) != 0:
                lst.append(nums[i])  # Include if bit is set
            result.append(lst)   # Add to result
        
    return result

print(Subset(nums))
