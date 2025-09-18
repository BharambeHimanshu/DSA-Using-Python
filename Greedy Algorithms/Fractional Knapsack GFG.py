# Fractional Knapsack
# GeekforGeeks problem

'''
Problem Statement - What Does the Problem Say?
You are given:

A set of items, each with a value and a weight.
A knapsack (bag) with a maximum capacity.
Your task is to:

Fill the knapsack such that the total value is maximized.
Unlike the 0/1 Knapsack problem, you are allowed to take fractions of items.

Example 1:
Input: 
val = [60, 100, 120] 
wt = [10, 20, 30] 
capacity = 50
Output: 240.0
Explanation:
- Pick item2 (value=100, weight=20) fully → remaining capacity = 30
- Pick item3 (value=120, weight=30) fully → remaining capacity = 0
Total value = 100 + 120 = 220

But better choice:
- Pick item1 (value=60, weight=10) fully → remaining capacity = 40
- Pick item2 (value=100, weight=20) fully → remaining capacity = 20
- Pick 2/3 fraction of item3 (value=120, weight=30) → add 80
Total value = 60 + 100 + 80 = 240
'''

class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        # Build list of (value/weight ratio, value, weight) for each item
        # Ignore any items with zero weight to avoid division by zero
        items = [(v / w, v, w) for v, w in zip(val, wt) if w > 0]

        # Sort by ratio in descending order
        items.sort(key=lambda x: x[0], reverse=True)

        cur_weight = 0
        total_value = 0.0

        for ratio, v, w in items:
            if cur_weight + w <= capacity:
                # take the whole item
                cur_weight += w
                total_value += v
            else:
                # take only the fraction that fits
                remain = capacity - cur_weight
                if remain <= 0:
                    break
                total_value += ratio * remain
                break  # knapsack is full

        return total_value
sol = Solution()
print(sol.fractionalknapsack(val = [60, 100, 120] , wt = [10, 20, 30] , capacity = 50))