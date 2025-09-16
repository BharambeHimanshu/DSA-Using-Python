# Longest Substring Without Repeating Characters
# Leetcode 3

'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# Brute Force Using Sets
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxans = 0
        for i in range(len(s)):
            set = {}
            for j in range(i, len(s)):
                if s[j] in set:
                    break
                maxans = max(maxans, j - i + 1)
                set[s[j]] = 1
        return maxans
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))

# Optimal Solution  Using Sliding window with two pointer and dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = dict()
        left = 0
        right = 0
        length = 0
        n = len(s)
        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]] + 1, left)
            hash_map[s[right]] = right
            length = max(length, right - left + 1)
            right += 1
        return length
sol = Solution()
print(sol.lengthOfLongestSubstring("bbbbb"))