def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i,j):
        if i <0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            nr, nc = i+dr, j+dc
            dfs(nr, nc)
            
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i,j)
    return count
