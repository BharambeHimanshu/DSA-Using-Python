# Check if a Subsequence with sum = k               TC ->o(2^n)      SC -> o(N)
# GeekforGeeks Problem
'''
Input:  nums = [10,1,2,7,6,1,5], target = 8.
Output:  Yes
Explanation:  Subsequences like [2, 6], [1, 7] sum upto 8

Input:  nums = [2,3,5,7,9], target = 100. 
Output:  No
Explanation:  No subsequence can sum upto 100
'''

# If we want to print only one subset

def backtrack(subset, index, total):
    if total == target:
        # result.append(subset.copy())  # Uncomment if you want to collect the subset
        return True
    elif total > target:
        return False
    if index >= len(nums):
        return False
        
    subset.append(nums[index])
    sum = total + nums[index]
    pick = backtrack(subset, index + 1, sum)
    if pick == True:
        return True
        
    e = subset.pop()
    # No need for Sum -= e; just pass total for not pick
    return backtrack(subset, index + 1, sum)
                   

nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
target = 3
print(backtrack([], 0, 0))          


