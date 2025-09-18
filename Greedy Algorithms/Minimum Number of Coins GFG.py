# Minimum Number of coins
# GFG

'''
Problem Statement - What Does the Problem Say?
You are given a value N. Your task is to represent this value using the minimum number of coins and notes available in the Indian currency system.

The available denominations are:

[2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
You need to output the coins/notes used in making the change for the given amount.

Example 1:
Input: N = 43
Output: [20, 20, 2, 1]
Explanation: 
- 20 + 20 + 2 + 1 = 43 using 4 coins/notes.

Example 2:
Input: N = 1000
Output: [500, 500]
Explanation:
- The amount 1000 can be formed using only two 500 rupee notes.
The problem essentially asks: How can we represent the number with the least number of coins/notes possible?
'''

class Solution:
    def minPartition(self, N):
        # Available denominations in Indian currency
        coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

        i = 0
        total = N
        result = []

        while total > 0:
            if total >= coins[i]:
                # Take the current coin/note
                result.append(coins[i])
                total = total - coins[i]
            else:
                # Move to the next smaller denomination
                i += 1
        return result

sol = Solution()
print(sol.minPartition(43))