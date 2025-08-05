# Rotate Image / Matrix

# Leetcode Problem 48 (Medim Level)

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

'''

# Brute Force TC -> o(n^2)   SC -> o(n^2)
# Approach :- Element (row =i, col =j) moves to (row =j, col = n − 1 − i).
# Because every element’s target is unique, we can safely write into a separate result matrix and finally overwrite the original.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result [j][n - 1 - i] = matrix[i][j]
    return result

print(rotate(matrix))


# Optimal Solution TC -> o(n^2)   SC -> o(1) Using Transpose 

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def Rotate(matrix):
    n = len(matrix)
    for i in range(n-1):  # Transpose Matrix
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in range(n): # Reverse array
        matrix[i].reverse()
    return matrix

print(Rotate(matrix))
