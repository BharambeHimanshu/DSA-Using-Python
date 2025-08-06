# Spiral Matrix
# Leetcode Problem 54
'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

# Solution  TC ->o(n*m)  SC -> o(1)
'''
Intuition and Approach
1. Four Pointers mark the current “unvisited rectangle”:
top row, bottom row, left column, right column.
2. Repeatedly walk the perimeter of that rectangle in four mini-passes:
   Left ➜ Right across the top row.
   Top ➜ Bottom down the right column.
   Right ➜ Left across the bottom row (if any rows remain).
   Bottom ➜ Top up the left column (if any cols remain).
3. After completing the loop, shrink the rectangle:
increment top, decrement bottom, increment left, decrement right.
4. Stop when top > bottom or left > right
'''

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def spiralOrder(matrix):
    # Handle empty input
    if not matrix or not matrix[0]:
        return []

    result = []               # stores the spiral order

    # Initialize boundary pointers
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1

    # Continue until the boundaries cross
    while top <= bottom and left <= right:
        # Traverse the top row from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1            # top row is done

        # Traverse the right column from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1         # right column is done

        # Traverse the bottom row from right to left (if any)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1     # bottom row is done

        # Traverse the left column from bottom to top (if any)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1       # left column is done
    return result

print(spiralOrder(matrix))
