# Set Matrix Zero
# Leetcode 73

'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
 
# Brute Force Solution  TC -> o((n+m)*(n*m)+(n*m))    SC -> o(1) 
# Approch - first iterate all the elements one by one when we find zero replace that coloumn and row with float("inf") after the iteration replace the infinity to zero

matrix = [[1,1,1],[1,0,1],[1,1,1]]

class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setzero(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j) # Replace all the rows and columns to infinity which contains 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0 # Replace infinity to zeros

        return matrix

s = Solution()
print(s.setzero(matrix))


# Optimal Solution  TC -> o(n*m)  SC -> o(n+m)
# Approach :- Keep track of rows and columns 
# 1) Set initial track to zero
# 2) If [i][j] == 0 make -1 to the track
# 3) Replace -1 to 0 to all the rows and columns

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def setzero(matrix):
    r = len(matrix)
    c = len(matrix[0])
    rowtrack = [0 for _ in range(r)]
    coltrack = [0 for _ in range(c)]
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                coltrack[i] = -1
        
    for i in range(0,r):
        for j in range(0,c):
            if rowtrack[i] == -1 or coltrack[i] == -1:
                matrix[i][j] = 0
    return matrix
print(setzero(matrix))
                

