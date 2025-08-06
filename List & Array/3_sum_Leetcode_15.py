# 3 Sum
# Leetcode Problem 15

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''

# Brute Force Solution TC -> o(n^3)   SC -> o(no.of triplet)

nums = [-1,0,1,2,-1,-4]

def threesumm(nums):
    n = len(nums)
    my_set = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    return [list(ans) for ans in my_set]

print(threesumm(nums))


# Better Solution  TC -> o(n^2)  SC -> o(n)+o(no.of triplet)
# we do something like nums[k] = -(nums[i]+nums[j])

nums = [-1,0,1,2,-1,-4]
def Threesum(nums):
    n = len(nums)
    result = set()
    for i in range(0,n):
        my_Set = set()  #Empty set 
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in my_Set:
                temp = [nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))  # Convert to tuple because list cannot be added to the set
            my_Set.add(nums[j])          # Add Every element which iterate by j and store it into set
    return[list(ans) for ans in result]  # Convert back to list

print(Threesum(nums))



# Optimal Solution  TC -> o(Nlogn) + o(n^2)      SC -> o(1)

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    ans = []
    n = len(nums)
    nums.sort()  # sort first for two-pointer technique

    for i in range(n):
        # skip duplicate fixed elements
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        # set up the two pointers
        j = i + 1
        k = n - 1

        # move pointers toward each other
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]

            if total_sum < 0:
                j += 1                     # need a larger sum
            elif total_sum > 0:
                k -= 1                     # need a smaller sum
            else:
                # found a valid triplet
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)

                # move both pointers and skip duplicates
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return ans

print(threeSum(nums))