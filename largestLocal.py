def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        maxlocal = [[0]*(n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                max_val = 0
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if grid[r][c] > max_val:
                            max_val = grid[r][c]
                maxlocal[i][j] = max_val
        return maxlocal