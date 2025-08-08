"""Given two arrays a and b of the same length, determine if array b is a rotation of array a.
An array b is a rotation of array a if b can be obtained by moving some elements from the beginning of a to the end, or vice versa.
"""

def arrayRotationCheck(a,b):
    if len(a) != len(b):
        return False
    
    if not a:
        return True
    a_double = a+a
    for i in range(len(a)):
        if a_double[i:i+len(a)] == b:
            return True
    return False


"""Given a 2D matrix of integers, find the maximum sum path from the top-left corner to the bottom-right corner. You can only move right or down at each step.
Additionally, you have the ability to "jump" over exactly one cell (skip it) during your entire journey. When you jump over a cell, you don't add its value to 
your sum, but you can land on any adjacent cell (right, down, or diagonal down-right from the jumped cell).
Return the maximum possible sum.
"""

def matrixTraversalJump(matrix):
    m,n = len(matrix), len(matrix[0])

    memo = {}

    def dfs(i,j,jumped):
        if i<0 or j<0 or i>= m or j >= n:
            return float('-inf')
        if (i,j, jumped) in memo:
            return memo[(i,j, jumped)]
        
        if i==m-1 and j == n-1:
            return matrix[i][j]
        
        directions = [(0,1), (1,0)]

        current_val = matrix[i][j]
        current_sum = float('-inf')

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n:
                current_sum = dfs(ni, nj, jumped)
                if current_sum != float('-inf'):
                     max_sum = max(max_sum, current_sum)

        if not jumped:
            jump_targets = [(i,j+1), (i+1, j), (i-1,j), (i,j-1)]
            for _ni, _nj in jump_targets:
                if 0 <= ni < m and 0 <= nj < n:
                    current_sum = dfs(_ni, _nj, True)
                    if current_sum != float('-inf'):
                        max_sum = max(max_sum, current_sum)
        memo[(i,j,jumped)] = max_sum
        return current_sum
    return dfs(0,0,False)
        

"""
Given a binary tree, return all root-to-leaf paths where the path values form a "zigzag" pattern. 
A zigzag pattern means the values are either strictly increasing then strictly decreasing, or strictly decreasing then strictly increasing, with exactly one "turning point".
The tree is given as an array where:

tree[0] is the root value
For node at index i: left child is at 2*i+1, right child is at 2*i+2
-1 represents a null node

Return the paths as arrays of values, sorted lexicographically."""

def zigzagTree(tree):
    if not tree or tree[0] == -1:
        return []
    result = []

    def dfs(index, path):
        if index >= len(tree) or tree[index] == -1:
            return
        
        path += [tree[index]]
        left, right = 2*i+1, 2*1+2

        if (left >= len(tree) or tree[left] == -1) and (right>= len(tree) or tree[right]==-1):
            if is_zigzag(path):
                result.append(path:)
        else:
            dfs(left, path)
            dfs(right, path)

        path.pop()

    def is_zigzag(p):
        if len(p)< 3:
            return True
        changes = [1 if p[i]>p[i-1] else -1 for i in range(1, len(p))]
        return len(set(changes)) == 2 and changes.count(changes[0]) == 1 or changes.count(changes[0]) == len(changes)-1
    
    dfs(0, [])
    return sorted(result)