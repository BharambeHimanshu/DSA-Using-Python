# Letter Combination of Number
# Leetcode 17
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
'''
# TC -> o(4^n * N)
# SC -> o(N)


class Solution:
    def __init__(self):
        # Phone keypad mapping - same as traditional phone buttons
        self.char_map = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
    
    def solve(self,index,subset,digits,result):
        # Base Condition
        if index == len(digits):
            result.append("".join(subset))
            return
        for ch in self.char_map[digits[index]]:   # "4" -> "ghi" ka loop chalega
            subset.append(ch)
            self.solve(index+1,subset,digits,result)
            subset.pop()
    def letterCombinations(self, digits):
        result = []
        if not digits:   # Agar Digits empty honge to empty list return karo
            return result
        self.solve(0,[],digits,result)
        return result
solution = Solution()
digits = "23"
print(solution.letterCombinations(digits))