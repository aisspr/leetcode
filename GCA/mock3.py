"""
You are given an array of integers arr and need to transform it according to the following rules:

If a number is even, divide it by 2
If a number is odd, multiply it by 3 and add 1
Apply this transformation k times to each element
Return the final array"""

def question1(arr, k):
    if not arr:
        return []
    result = arr
    for _ in range(k):
        transformed_arr = []
        for el in result:
            if el % 2 == 0:
                el = el // 2
            else:
                el = el*3+1
            transformed_arr.append(el)
        result = transformed_arr
    return result

    
"""Given a string s and a pattern p, determine if the string follows the pattern. The pattern contains:

Lowercase letters (a-z) representing single characters
'?' representing exactly one character
'*' representing zero or more characters

Return true if the string matches the pattern, false otherwise.
def stringPatternMatching(s,p):
    if not p:
        return not s
    if not s:
        return p == '*'*len(p)
    
    if p[0] == '*':
        return stringPatternMatching(s, p[1:]) or stringPatternMatching(s[1:],p)
    elif p[0] == '?' or p[0] == s[0]:
        return stringPatternMatching(s[1:],p[1:])
    else:
        return False
"""

def stringPatternMatching(s,p):
    memo = {}

    def match(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if j == len(p):
            res = i = len(s)
        elif i == len(s):
            res = all(c=='*' for c in p[j:])
        elif p[j] == '*':
            res = match(i,j+1) or match(i+1, j)
        elif p[j] == '?' or p[j] == s[i]:
            res = match(i+1, j+1)
        memo[(i,j)] = res
        return res
    
    return match(0,0)
    

"""
Given a binary tree and a target sum, find the number of paths where the sum of values along the path equals the target.
The path does not need to start or end at the root or a leaf, but it must go downwards (from parent to child nodes)."""

def bstTargetSum(tree, target):
    from collections import defaultdict
    cnt = [0]
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1

    def dfs(node, current_sum):
        if not node:
            return 0
        
        current_sum += node.val
        cnt[0] += prefix_sum[current_sum-target]

        prefix_sum[current_sum] += 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        prefix_sum[current_sum] -= 1
    dfs(tree, 0)
    return cnt[0]

"""You are given a 2D grid where each cell contains a non-negative integer representing the cost to pass through that cell.
 You start at the top-left corner (0,0) and want to reach the bottom-right corner (m-1,n-1).
You can move in 4 directions (up, down, left, right), and you want to find the minimum cost path. 
However, you have a special ability: you can use a "teleport" exactly once to jump to any cell in the grid without paying its cost.
Return the minimum total cost to reach the destination.
"""

def costTraversal(grid):
    m, n = len(grid), len(grid[0])
    memo = {}

    def dfs(i,j, teleport_used):
        if (i,j, teleport_used) in memo:
            return memo[(i,j, teleport_used)]
        if i == m-1 and j == n-1:
            return 0
        
        min_cost = 1000
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        for dr, dc in directions:
            nr, nc = dr+i, dc+j
            if 0 <= nr < m and 0 <= nc < n:
                cost = min(min_cost, grid[nr][nc] + dfs(nr, nc, teleport_used))

        if not teleport_used:
            for _i in range(m):
                for _j in range(n):
                    if (i,j) != (_i,_j):
                        min_cost = min(min_cost, dfs(_i,_j))

        memo[(i,j,teleport_used)] = min_cost
        return min_cost
    return grid[0][0] + dfs(0,0,0)

