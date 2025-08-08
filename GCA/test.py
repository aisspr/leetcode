
"""You are given the root of a binary tree and an integer targetSum. Find all root-to-leaf paths where the sum of node values equals targetSum.
Additionally, implement a helper function that counts how many nodes in the entire tree have a value that appears in at least one valid path.
"""

def findPaths(tree, targetSum):
    result = []

    def dfs(node, current_sum, path):
        if not node:
            return
        path.append(node.val)
        current_sum += node.val

        if not node.left and not node.right:
            if current_sum == targetSum:
                result.append(path[:])

        else:
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)

        path.pop()
    
    dfs(tree, 0, [])
    return result


"""You are given a string s containing lowercase English letters and a list of operations. Each operation is represented as a tuple (char, replacement) 
where char is the character to replace and replacement is what to replace it with.
Apply all operations to the string in the given order. However, if applying an operation would create a cycle (where character A maps to B, B maps to C, 
and C maps to A), skip that operation.
"""

def modifyString(s, operations):
    mapping = {}
    def would_create_cycle(c, replacement):
        current = replacement
        visited = set()

        while current in mapping:
            if current == c:
                return True #this is cycle
            if current in visited:
                break #found a different cycle
            visited.add(current)
            current = mapping[current]
        return False
    for c, replacement in operations:
        if not would_create_cycle(c, replacement):
            mapping[c] = replacement
    result = []

    for c in s:
        current = c
        visited = set()

        while current in mapping and current not in visited:
            visited.add(current)
            current = mapping[current]

        result.append(current)
    return ''.join(result)



"""Given a 2D matrix of integers, find the path from the top-left corner to the bottom-right corner that maximizes the sum of elements along the path. 
You can only move right or down.
Additionally, you can use up to k "jumps" where a jump allows you to move to any adjacent cell (including diagonally) instead of just right or down.
Return the maximum sum possible.
"""

def maxSumMatrixKJumps(grid, k_jumps):
    #you can use up to k "jumps" where a jump allows you 
    # to move to any adjacent cell (including diagonally)
    m,n = len(grid), len(grid[0])

    memo = {}

    def solve(i,j,remaining_jumps):
        if i == m-1 and j==n-1:
            return grid[i][j]
        if (i,j, remaining_jumps) in memo:
            return memo[(i,j,remaining_jumps)]
        result = float('-inf')
        if i+1 < m:
            result = max(result, grid[i][j]+solve(i+1,j,remaining_jumps))
        if j+1 < n:
            result = max(result, grid[i][j]+solve(i,j+1,remaining_jumps))

        if remaining_jumps > 0:
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di == 0 and dj == 0:
                        continue
                    ni,nj = i+di, j+dj
                    if 0 <= ni <= m and 0 <= nj <= n:
                        result = max(result, grid[i][j] + solve(ni,nj, remaining_jumps-1))
        memo[(i,j,remaining_jumps)] = result
        return result
    return solve(0,0,k)
        


"""You are given a binary tree represented as a list of parent-child relationships and a target sum. Some nodes in the tree have been corrupted (their values changed to -1).
Your task is to:

Reconstruct the tree from the parent-child relationships
Determine the minimum number of corrupted nodes you need to fix
Return the minimum number of nodes to change so that there exists at least one root-to-leaf path with sum equal to the target

You can change any corrupted node (-1) to any integer value.
"""



"""
You are given an n × n matrix filled with integers. Perform the following operations in sequence:

Rotate the matrix 90 degrees clockwise
For each row, move all zeros to the end while maintaining the relative order of non-zero elements
Replace each element with the sum of all elements in its column"""


def modifyMatrix(mat):

    n = len(mat)
    mat = rotate90(mat)
    mat = move_zeros_to_end(mat)
    mat = replace_col_with_sum(mat)

    def rotate90(mat):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for row in range(n)
            row.reverse()
        return mat
    
    def move_zeros_to_end(mat):
        for i in range(i):
            non_zeros = [x for x in mat[i] if x != 0]
            mat[i] = non_zeros + [0]*(n-len(non_zeros))
        return mat
    
    def replace_col_with_sum(mat):
        n = len(mat)
        col_sums = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = col_sums[j]
        return mat




"""
You are given a binary tree where each node contains an integer value. Find all root-to-leaf paths where the sum of node values equals 
a target sum. However, you can "flip" the sign of at most k nodes along any path.
Return the number of valid paths that can achieve the target sum with at most k sign flips."""



"""
You are given a pattern string containing only the characters 'a' and 'b', and a string s. Determine if s follows the same pattern, 
where 'a' and 'b' represent different non-empty substrings."""








"""
You are given a binary tree where each node contains a positive integer value. Find the path from root to any leaf that has the maximum sum. 
If multiple paths have the same maximum sum, return the lexicographically smallest one when comparing the sequence of values."""







"""
You are given a binary tree where each node contains an integer value. Implement a function that transforms the tree according to these rules:

Replace each node's value with the sum of all values in its subtree (including itself)
After transformation, find and return all root-to-leaf paths where the path sum equals a given target value
The paths should be returned in lexicographically smallest order when compared as arrays"""










"""
Given a string containing only the characters '(', ')', '{', '}', '[' and ']', determine if the input string has valid parentheses combinations.
An input string is valid if:

Open brackets are closed by the same type of brackets
Open brackets are closed in the correct order
Every close bracket has a corresponding open bracket"""



"""
Given the root of a binary tree, return the maximum path sum of any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root.
The path sum is the sum of the node values in the path.
"""










"""
Given a string s and a dictionary of strings wordDict, determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
The same word in the dictionary may be reused multiple times in the segmentation.
Additionally, return the number of different ways s can be segmented into dictionary words."""





"""Design and implement a data structure for a Least Recently Used (LRU) cache that supports the following operations:

get(key): Return the value of the key if it exists in the cache, otherwise return -1
put(key, value): Update the value of the key if it exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity, evict the least recently used key.

Both operations must run in O(1) average time complexity.
Implementation Requirements
Implement a class LRUCache with:

Constructor: LRUCache(capacity) - Initialize the cache with positive size capacity
Method: get(key) - Get the value (will always be positive) of the key
Method: put(key, value) - Set or insert the value

Input/Output Format for Testing

Input: Array of operations and their parameters
Output: Array of results for each operation
"""






"""Given a string word, return the number of substrings that contain exactly one occurrence of each vowel ('a', 'e', 'i', 'o', 'u') and no consonants."""

"""
You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray of length exactly k that has the maximum average value and return this value."""

"""
You are given an m x n matrix and an integer k. Rotate each layer of the matrix clockwise by k positions. A layer is defined as the elements forming a rectangle ring in the matrix.
For example, in a 4x5 matrix:

Layer 0 (outermost): all border elements
Layer 1: inner border elements (if exists)

Each layer should be rotated independently."""


"""
You have a rectangular board of size m x n and a list of Tetris-like pieces. Each piece is represented as a 2D array of 1s and 0s. 
Determine the maximum number of pieces that can be placed on the board without overlapping. Pieces cannot be rotated or flipped."""