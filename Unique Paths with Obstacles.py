class Solution:
    def uniquePathsWithObstacles(self, grid):
        # time complexity O(m*n)
        # space complexity O(1)
        # m * n grid
        m = len(grid)
        n = len(grid[0])
        
        # base case
        if grid[0][0] == 1: return 0
        
        # initialize: there is 1 way to start from the starting cell
        grid[0][0] = 1
        
        # filling value for the first column
        for i in range(1, m):
            if grid[i][0] == 0 and grid[i-1][0] == 1:
                grid[i][0] = 1
            else: grid[i][0] = 0
        
        # filling value for the first row
        for j in range(1, n):
            if grid[0][j] == 0 and grid[0][j-1] == 1:
                grid[0][j] = 1
            else: grid[0][j] = 0
                
        # start filling the remain cells 
        # number of ways of reaching cell[i][j] is 
        # cell[i-1][j] + cell[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0: 
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0
        
        return grid[-1][-1]