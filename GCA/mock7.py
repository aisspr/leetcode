"""Given an array of integers, find all pairs of elements that sum to a target value. Return the number of unique pairs.
A pair (i, j) is considered the same as pair (j, i), so count each unique pair only once. Also, an element cannot be paired with itself (i ≠ j).
"""

def countSumPairs(arr, target):
    from collections import Counter

    freqMap = Counter(arr)
    cnt = 0

    for i, el in enumerate(arr):
        diff = target - el
        if diff in freqMap:
            if el == diff:
                if freqMap[el] < 1:
                    cnt += 1
            else:
                if el < diff:
                    cnt += 1
    return cnt
                


"""
You are given a string representing a simple mathematical expression containing only digits, '+', '-', and parentheses. Evaluate the expression and return the result.
The expression is guaranteed to be valid. Numbers can be multi-digit."""

def mathExpression(s):
    if not s:
        return True
    stack = []
    result = 0
    sign = 1
    num = 1
    for c in s:
        if c.isdigit():
            num = num*10+int(c)
        elif c =='+':
            result += sign*number
            number = 0
            sign = 1
        elif c == '-':
            result += sign*number
            number = 0
            sign = -1
        elif c=='(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif c==')':
            result += sign*number
            number = 0
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result +prev_sign*result
    if num != 0:
        result += sign*number
    return result


"""
You are given a 2D grid representing a game board where:

0 represents an empty cell
1 represents a wall
2 represents a treasure

You start at position (0, 0) and want to collect all treasures. You can move up, down, left, or right to adjacent cells, but cannot move through walls or outside the grid boundaries.
Return the minimum number of steps needed to collect all treasures, or -1 if it's impossible."""

def collectTreasures(grid):
    m,n = len(grid), len(grid[0])
    treasures = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                treasures.append((i,j))
    if not treasures:
        return 0
    
    memo = {}

    def dfs(i,j,collected):
        if (i,j,collected) in memo:
            return memo[(i,j,collected)]
        
        if len(collected) == len(treasures):
            return 0
        
        min_steps = float('inf')

        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        for dr,dc in directions:
            nr, nc = i+dr, j+dc
            if 0 <= nr < m and 0 <= nc < m and grid[nr][nc] != 1:
                new_collected = collected[:]
                if (nr,nc) in treasures:
                    new_collected.add((nr,nc))
                result = dfs(nr,nc, new_collected)
                if result != float('inf'):
                    min_steps = min(min_steps, 1+result)

        memo[(i,j,collected)] = min_steps
        return min_steps
    start_collected = set()
    if (0,0) in treasures:
        start_collected.add((0,0))
    result = dfs(0,0,start_collected)
    return result if result != float('inf') else -1
        




"""You are given a binary tree where each node contains an integer value. You need to find the maximum sum of any path in the tree.
A path is defined as a sequence of connected nodes where each pair of adjacent nodes in the sequence has a parent-child relationship.
 A path must contain at least one node and does not need to go through the root.
"""

def maxSumPathTree(tree):
    from collections import defaultdict

    max_sum = [0]

    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1

    def dfs(node):
        if not node:
            return 0
        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))
        current_path_sum = node.val + left_sum + right_sum
        max_sum[0] = ax(max_sum[0], current_path_sum)

        return node.val + max(left_sum, right_sum)
        
    dfs(tree)
    return max_sum[0]


