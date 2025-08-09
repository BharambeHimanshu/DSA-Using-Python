# 4 Sum
# Leetcode problem 18
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output  [[2,2,2,2]]

'''

# Brute Force Solution    TC -> o(n^4)  SC -> o(n)

nums = [1,0,-1,0,-2,2]
target = 0
def foursum(nums,target):
    n = len(nums)
    if n < 4:
        return []
    my_set = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))

    result = []

    for ans in my_set:
        result.append(list(ans))
    return result

print(foursum(nums,target))


# Better Solution   TC -> o(n^3)  SC -> o(n)
# Something like fourth = -(nums[i]+nums[j]+nums[k])

nums = [2,2,2,2,2]
target = 8

def Foursum(nums,target):
    n =len(nums)
    if n < 4:
        return []
    
    my_set = set()  # Store unique quadrauplets

    # Fix first two indices
    for i  in range(0,n):
        for j in range(i+1,n):
            hash_set =set()  # Track needed fourth element

            # Scan remaining indices for third element

            for k in range(j+1,n):
                fourth = target - (nums[i]+nums[j]+nums[k])

                if fourth in hash_set:
                    temp = [nums[i],nums[j],nums[k],fourth]
                    temp.sort()
                    my_set.add(tuple(temp))

                # Add current third element to the hashset
                hash_set.add(nums[k])

    # Convert to required list format
    result = []

    for ans in my_set:
        result.append(list(ans))
    return result
    
print(Foursum(nums,target))


# Optimal Solution        TC -> o(n^3)    SC -> o(1)
# By Sorting the list and find the value based on condition

nums = [1,0,-1,0,-2,2]
target = 0
def FourSum(nums,target):
    n = len(nums)
    ans = []
    nums.sort()  # Step 1: sort to simplify duplicates

    #  Step 2: pick first two numbers
    for i in range(0, n):
        if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for i
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates for j
                continue

            # Step 3: two-pointer search for remaining two
            k = j + 1               # left pointer
            l = n - 1               # right pointer

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    # skip duplicate values for k
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    # skip duplicate values for l
                    while l > k and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1           # need a larger sum

                else:
                    l -= 1           # need a smaller sum

    return ans

print(FourSum(nums,target))