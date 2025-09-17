# Fruits into Basket
# Leetcode 904

'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''

# Brute Force     TC -> o(n(n+1)/2)     SC -> o(1)

class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)
        max_length = 0
        for i in range(n):
            my_set = set()
            for j in range(i, n):
                my_set.add(fruits[j])
                if len(my_set) > 2:
                    break
                max_length = max(max_length, j - i + 1)
        return max_length
sol = Solution()
print(sol.totalFruit([1,2,3,2,2]))

# Better Solution     TC -> o(2N)  SC -> o(1)

class Solution:
    def totalFruit(self, nums):
        n = len(nums)
        left = 0
        right = 0
        maxi = 0
        my_dict = {}
        while right < n:
            my_dict[nums[right]] = my_dict.get(nums[right],0)+1
            while len(my_dict) > 2:
                my_dict[nums[left]]-= 1
                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi,right - left + 1)
            right += 1
        return maxi
sol = Solution()
print(sol.totalFruit([1,2,3,2,2]))


# Optimal Solution     TC -> o(N)     SC -> o(1)

class Solution:
    def totalFruit(self, nums):
        n = len(nums)
        left = 0
        right = 0
        maxi = 0
        my_dict = {}
        while right < n:
            my_dict[nums[right]] = my_dict.get(nums[right],0)+1
            # The only diff between better and optimal Ssolution, we are using if instead of while
            if len(my_dict) > 2:
                my_dict[nums[left]]-= 1
                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi,right - left + 1)
            right += 1
        return maxi
sol = Solution()
print(sol.totalFruit([1,2,3,2,2]))