def minPathSum(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    #step 1: init the first row

    for j in range(1, cols):
        grid[0][j] += grid[0][j-1] # grid[0][j] = grid[0][j-1] + grid[0][j]

    #step 2
    for i in range(1, rows):
        grid[i][0] += grid[i-1][0]
    
    #step 3
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[rows-1][cols-1]
