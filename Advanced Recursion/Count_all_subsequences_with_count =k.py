# Count all Subsequences with count = k
# GeekforGeeks Problem
'''
Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
Output: 3
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.

Input: arr[] = [2, 5, 1, 4, 3], target = 10
Output: 3
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.

Input: arr[] = [5, 7, 8], target = 3
Output: 0
Explanation: There are no subsets of the array that sum up to the target 3.

Input: arr[] = [35, 2, 8, 22], target = 0
Output: 1
Explanation: The empty subset is the only subset with a sum of 0.
'''

def backtrack(index,total):
    if total == target:
        return 1
    elif total > target:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index+1, sum)
    sum = total
    not_pick = backtrack(index+1,sum)
    return pick + not_pick

nums = [5, 2, 3, 10, 6, 8]
target = 10
print(backtrack(0,0))