# Rat in a Maze Problem
# Geekforgeeks problem

'''
Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

Input: mat[][] = [[1, 0], [1, 0]]
Output: []
Explanation: No path exists as the destination cell is blocked.

Input: mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: ["DDRR", "RRDD"]
Explanation: The rat has two possible paths to reach the destination: 1. "DDRR" 2. "RRDD", These are returned in lexicographically sorted order.
'''
class Solution:
    def pathtracking(self,i,j,a,n,ans,move,vis):
        # Base Case
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
    
        # Down
        if i + 1 < n and not vis[i+1][j] and a[i+1][j] == 1:
            vis[i][j] = 1  #Mark Current cell as visites
            self.pathtracking(i+1,j,a,n,ans,move + "D",vis)
            vis[i][j] = 0   # BAcktrak : Unmark current cell
        # Left
        if j - 1 >=0 and not vis[i][j-1] and a[i][j-1] == 1:
            vis[i][j] = 1
            self.pathtracking(i,j - 1,a,n,ans,move + "L",vis)
            vis[i][j] = 0
        # Right
        if j + 1 < n and not vis[i][j+1] and a[i][j+1] == 1:
            vis[i][j] = 1
            self.pathtracking(i,j + 1,a,n,ans,move + "R",vis)
            vis[i][j] = 0
        # Up
        if i - 1 >= 0 and not vis[i-1][j] and a[i-1][j] == 1:
            vis[i][j] = 1
            self.pathtracking(i - 1,j,a,n,ans,move + "U",vis)
            vis[i][j] = 0

    def RAT(self, matrix):
        n = len(matrix)
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]   # Visited Array
        # Only start if source cell is open
        if matrix[0][0] == 1:
            self.pathtracking(0,0,matrix,n,ans,"",vis)
        return ans

solution = Solution()
matrix1 = [[1, 0, 0, 0],
           [1, 1, 0, 1],
           [1, 1, 0, 0],
           [0, 1, 1, 1]]

matrix2 = [[1, 0],
           [1, 0]]

matrix3 = [[1, 1, 1],
           [1, 0, 1],
           [1, 1, 1]]

print(solution.RAT(matrix1))  
print(solution.RAT(matrix2))  
print(solution.RAT(matrix3))  
