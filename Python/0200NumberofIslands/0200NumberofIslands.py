## Time complexity: O(n * m)
## memory comlexity:O(1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_island = 0

        rows, cols = len(grid), len(grid[0])

        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(i,j):
            if 0<=i <rows and 0<= j<cols and grid[i][j] =="1":
                grid[i][j] = "0"

                for di, dj in direction:
                    dfs(i+di, j+dj)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    n_island+=1

        return n_island
