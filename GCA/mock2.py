"""Given an array of integers arr and an integer k, you need to find the maximum sum of any contiguous subarray of length k. 
Additionally, return the starting index of this subarray. If there are multiple subarrays with the same maximum sum, return the one with the smallest starting index.
"""

def maxSum(arr, k):
    if not arr or k > len(arr) or k<= 0:
        return [-1, 0]
    
    current_sum = sum(arr[:k])
    max_sum = current_sum
    max_start_idx = 0

    

    for right in range(k, len(arr)):
        left = right - k + 1
        current_sum = current_sum +  arr[right] - arr[right-k]

        if current_sum > max_sum:
            max_sum = current_sum
            max_start_idx = left
    return [max_start_idx, max_sum]


"""You are given a string s containing only lowercase English letters. You need to find the length of the longest substring that contains at most 
k distinct characters and where each character appears at least minFreq times within that substring.
"""

def longestSubstringMinfreq(s, minFreq):
    from collections import defaultdict
    if not s:
        return 0
    
    max_length = 0
    left = 0
    char_cnt = defaultdict(int)

    for right in range(len(s)):
        char_cnt[s[right]] += 1

        while len(char_cnt) > k:
            char_cnt[s[left]] -= 1
            if char_cnt[s[left]] == 0:
                del char_cnt[s[left]]
            left += 1
        valid = True
        for cnt in char_cnt.value():
            if cnt < minFreq:
                valid = False
                break
        if valid:
            max_length = max(max_length, right-left+1)
    return max_length
        


"""You are given a binary tree where each node contains an integer value. 
You need to find the maximum sum of any path in the tree. A path is defined as any sequence of nodes from some starting node 
to any ending node along parent-child connections. The path must contain at least one node and doesn't need to go through the root.
However, there's a twist: you can "flip" at most k negative values to their positive equivalents along any path you choose.
"""

def maxPathFlip(tree, k):
    max_sum = [0]
    def dfs(node, flips_left):
        if not node:
            return 0
        max_sum = 0
        cnt_flip = k

        left_depth = dfs(node.left, flips_left)
        right_depth = dfs(node.right, flips_left)

        current_val = node.val
        current_sum = current_val + left_depth + right_depth

        #try flipping this node

        if current_val <0 and flips_left > 0

        left_depth_flip = dfs(node.left, flips_left-1)
        right_depth_flip = dfs(node.right, flips_left-1)

        flipped_sum = abs(current_val) + left_depth_flip + right_depth_flip
        current_sum = max(current_sum, flipped_sum)

    
        max_sum[0] = max(max_sum[0], current_sum)

        single_path = current_val + max(left_depth, right_depth)
        if current_val < 0 and flips_left > 0:
            single_path_flip = abs(current_val) + max(left_depth_flip, right_depth_flip)
            single_path = max(single_path, single_path_flip)

        return max(0, single_path)
    dfs(tree, k)
    return max_sum[0]



"""You are playing a game on a grid of size m × n. You start at the top-left corner (0, 0) and want to reach the bottom-right corner (m-1, n-1). 
Each cell (i, j) contains an integer grid[i][j].
The rules are:

You can only move right or down
You have a "power" value that starts at initialPower
When you enter a cell, your power changes by the value in that cell (can be negative)
If your power ever becomes ≤ 0, you lose the game
You have exactly shields that can protect you: when you would lose the game (power ≤ 0), you can use a shield to set your power to 1 instead

Find the minimum initial power needed to guarantee you can reach the destination.
"""

def gameGridShields(grid, shields):
    #Find the minimum initial power needed to guarantee 
    # you can reach the destination.

    m, n = len(grid), len(grid[0])
    memo = {}

    def dfs(i,j,s):
        if (i,j,s) in memo:
            return memo[(i,j,s)]
        if i == m-1 and j == n-1:
            return max(1, 1-grid[i][j])
        res = 1000
        for di,dj in [(0,1), (1,0)]:
            ni, nj = i+di, j+dj
            res = min(res, max(1, 1-dfs(ni,nj,s)-grid[i][j]))
            if s > 0:
                res = min(res, max(1, 1-dfs(ni,nj,s-1)))

            memo[(i,j,s)] = res
            return res
    return dfs(0,0,shields)
    