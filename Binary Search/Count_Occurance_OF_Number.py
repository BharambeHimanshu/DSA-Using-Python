# Cound occurance of a number in an sorted array with duplicates
'''
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Example 1 
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Example 2
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.

Example 3
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3
'''

# Brute Force Solution       TC -> o(N)   SC -> o(1)

nums = [5,7,7,8,8, 8, 10]
target = 8
def countNo(nums,target):
    n = len(nums)
    last = -1
    first = -1
    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return last - first + 1

print(countNo(nums,target))

# Optimal Solution Using lower and upper bound   TC -> o(logn)     SC -> o(1)

nums= [1, 1, 2, 2, 2, 2, 3]
target = 2

class Solution:
    def lower_bound(self, nums, target):
        n = len(nums)
        lb = -1  # Default value if target is not found
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid  # Possible lower bound found
                high = mid - 1  # Search left for first occurrence
            else:
                low = mid + 1

        return lb

    def upper_bound(self, nums, target):
        n = len(nums)
        ub = n  # Default value if target is greater than all elements
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid  # Possible upper bound found
                high = mid - 1  # Search left for first element > target
            else:
                low = mid + 1

        return ub

    def countFreq(self, nums, target):
        lb = self.lower_bound(nums, target)
        if lb == -1 or nums[lb] != target:
            return 0  # Target is not found in the array

        ub = self.upper_bound(nums, target)
        return ub - lb  # Count of occurrences

sol = Solution()
print(sol.countFreq(nums, target))    


