"""
You are given an m × n matrix of integers. Find the maximum sum of elements along a path from the top-left corner (0,0) to the bottom-right corner (m-1, n-1).
You can move in four directions: up, down, left, right. However, you cannot visit the same cell twice in a single path.
"""
def matrixPathsum(matrix):
    m,n = len(matrix), len(matrix[0])

    def dfs(i,j, visited):
        if i<0 or j<0 or i>m or j> n or (i,j) in visited:
            return float('-inf')
        if i == m-1 and j == n-1:
            return matrix[i][j]
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited.add((i,j))
        current_val = matrix[i][j]
        current_sum = float('-inf')

        for dr,dc in directions:
            nr,nc = dr+i, dc+j
            current_sum = dfs(nr,nc,visited)
            if current_sum != float('-inf'):
                current_sum = max(current_sum, current_val+current_sum)
        visited.remove((i,j))
        return current_sum
    return dfs(0,0,set())








"""
You are given a string containing only parentheses (), square brackets [], and curly braces {}. However, some characters might be replaced with ? wildcards.
Determine if it's possible to replace each ? with any type of opening or closing bracket to make the string a valid bracket sequence.
A valid bracket sequence is one where:

Every opening bracket has a corresponding closing bracket
Brackets are properly nested
No closing bracket appears before its corresponding opening bracket"""

def regexValidBrackets(s):
    memo = {}
    
    def dfs(i, stack):
        key = (i, tuple(stack))
        if key in memo:
            return memo[key]
        
        if i == len(s):
            return len(stack) == 0
        
        if s[i] == '?':
            # Try opening brackets
            for b in '([{':
                if dfs(i+1, stack + [b]):
                    memo[key] = True
                    return True
            # Try closing brackets  
            for b in ')]}':
                if stack and {'(': ')', '[': ']', '{': '}'}[stack[-1]] == b:
                    if dfs(i+1, stack[:-1]):
                        memo[key] = True
                        return True
            memo[key] = False
            return False
        else:
            if s[i] in '([{':
                res = dfs(i+1, stack + [s[i]])
            else:
                res = (stack and {'(': ')', '[': ']', '{': '}'}[stack[-1]] == s[i] 
                       and dfs(i+1, stack[:-1]))
            memo[key] = res
            return res
    
    return dfs(0, [])
        