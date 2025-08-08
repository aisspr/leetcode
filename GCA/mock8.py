"""
Given a string s, implement a function that removes all duplicate characters while keeping the lexicographically smallest result. 
Each character should appear exactly once in the final string."""

def removeDuplicates(s):
    stack = []
    seen = set()
    last_occurrence = {char: i for i, char in enumerate(s)}

    for i,c in enumerate(s):
        if c in set:
            continue
        while stack and c < stack[-1] and last_occurrence[stack[-1]] > i:
            popped_c = stack.pop()
            stack.remove(popped_c)
        stack.append(c)
        seen.add(c)
    return ''.join(stack) 




"""
You are given a 2D grid representing a maze where:

0 represents an empty cell
1 represents a wall
2 represents the start position
3 represents the end position

Find the shortest path from start to end. You can move up, down, left, or right. Return the length of the shortest path, or -1 if no path exists."""

def maze(grid):
    from collections import deque
    m,n = len(grid), len(grid[0])
    start = None
    end = None

    len_path = [0]
    memo = {}

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                start = (i,j)
            elif grid[i][j] = 3:
                end = (i,j)

    if not start or not end:
        return -1
    q = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}

    while q:
        i,j,dist = q.popleft()

        if (i,j) == end:
            return dist
        for dr,dc in [(0,1), (0,-1), (-1,0), (1,0)]:
            nr,nc = dr+i, dc+j
            if 0<=nr<=m and 0<= nc<=n and grid[nr][nc] != 1  and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc,dist+1))

    return dist+1




"""
Design a data structure that supports the following operations efficiently:

insert(val) - Insert a value into the data structure
remove(val) - Remove a value from the data structure
getRandom() - Return a random element from the current elements with equal probability
getFrequent() - Return the most frequently inserted element (if tie, return any)

All operations should run in O(1) average time complexity."""


import random

class DataStructure:
    def __init__(self):
        self.val_to_index = {}
        self.values = []
        self.counts = {}
        self.max_freq = 0
        self.most_frequent_val = None

    def insert(self, val: int) -> bool:
        """Inserts a value into the data structure."""
        # Add to values list and val_to_index map
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        
        # Update counts
        self.counts[val] = self.counts.get(val, 0) + 1
        
        # Update most frequent element
        if self.counts[val] > self.max_freq:
            self.max_freq = self.counts[val]
            self.most_frequent_val = val
            
        return True

    def remove(self, val: int) -> bool:
        """Removes a value from the data structure."""
        if val not in self.val_to_index:
            return False

        # Get the index of the value to be removed
        idx_to_remove = self.val_to_index[val]
        
        # To achieve O(1) removal from the list, swap with the last element
        last_val = self.values[-1]
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        
        # Pop the last element and remove from val_to_index
        self.values.pop()
        del self.val_to_index[val]
        
        # Update counts
        self.counts[val] -= 1
        if self.counts[val] == 0:
            del self.counts[val]

        # Re-evaluate most frequent element if needed
        # This is the part that is O(k) in the worst case but O(1) on average
        if self.most_frequent_val == val:
            if val not in self.counts or self.counts[val] < self.max_freq:
                # Re-evaluate max_freq and most_frequent_val
                if not self.counts:
                    self.max_freq = 0
                    self.most_frequent_val = None
                else:
                    new_max_freq = 0
                    new_most_frequent_val = None
                    for element, count in self.counts.items():
                        if count > new_max_freq:
                            new_max_freq = count
                            new_most_frequent_val = element
                    self.max_freq = new_max_freq
                    self.most_frequent_val = new_most_frequent_val

        return True

    def getRandom(self) -> int:
        """Returns a random element from the current elements with equal probability."""
        if not self.values:
            return None # or raise an error
        return random.choice(self.values)

    def getFrequent(self) -> int:
        """Returns the most frequently inserted element."""
        if not self.values:
            return None # or raise an error
        return self.most_frequent_val



"""
You are given an array of integers nums and an integer target. You need to find all pairs of indices (i, j) where i < j and nums[i] + nums[j] = target.
 Return the count of such valid pairs."""

def sumPairs(arr, target):
    #nums[i] + nums[j] = target.
    #Return the count of such valid pairs.

    seen = {}
    cnt = 0

    for i, el in enumerate(arr):
        diff = target - el
        if diff in seen:
            cnt += seen[diff]
        seen[el] = seen.get(el, 0)
    return cnt
    


"""You are given a string s containing only lowercase English letters. You need to rearrange the characters to create the lexicographically smallest 
string where no two adjacent characters are the same. If it's impossible, return an empty string.
"""

def arrangeString(s):
    #rearrange the characters to create the lexicographically smallest 
    #string where no two adjacent characters are the same
    from collections import Counter
    n = len(s)
    cnts = Counter(s)

    max_freq = max(cnts.values())
    if max_freq > (n+1)//2: 
        return ''
    result = []
    while cnts:
        candidates = []
        for c, freq in cnts.items():
            if not result or c != result[-1]:
                candidates.append((c,freq))
        if not candidates:
            return ''
        
        candidates.sort(key=lambda x: (-x[0], x[1])) #lexicographically smallest if tie
        freq, c = candidates[0]

        result.append(c)
        cnts[c] -= 1
        if cnt[c] == 0:
            del cnt[c]
    return ''.join(result)



"""You are given a 2D grid of integers. You need to find the number of "islands" where an island is defined as a group of connected cells (horizontally or vertically) 
that have the same value. Additionally, an island must have at least 2 cells to be considered valid.
After counting islands, you need to return a dictionary where keys are the unique values that form islands, and values are the count of islands formed by that value.
"""
def numIslands(grid):
    #After counting islands, you need to return a dictionary where
    #  keys are the unique values that form islands, 
    # and values are the count of islands formed by that value
    if not grid:
        return {}
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    result = {}
    
    def dfs(i, j, val):
        if (i < 0 or i >= m or j < 0 or j >= n or 
            visited[i][j] or grid[i][j] != val):
            return 0
        
        visited[i][j] = True
        return 1 + dfs(i+1,j,val) + dfs(i-1,j,val) + dfs(i,j+1,val) + dfs(i,j-1,val)
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                size = dfs(i, j, grid[i][j])
                if size >= 2:
                    val = grid[i][j]
                    result[val] = result.get(val, 0) + 1
    
    return result



"""You are given a binary tree where each node contains an integer value. You need to implement a function that finds all paths from root to leaf 
where the sum of values along the path equals a given target sum.
However, there's a twist: you can "flip" the sign of at most one node value in each path. Return the total number of valid paths possible with this flexibility.
"""

def cntPathsBinaryTreeFlip(tree, target):
    count[0] = 0

    def dfs(node, current_sum, flip_used):
        if not node:
            return 
        original_sum = current_sum + node.val
        flipped_sum = current_sum - node.val

        if not node.left and not node.right:
            if original_sum == target:
                count[0] += 1
            if not flip_used and flipped_sum == target:
                count[0] += 1
            return
        # Continue DFS for internal nodes
        # Path 1: Don't flip current node
        if node.left:
            dfs(node.left, original_sum, flip_used)
        if node.right:
            dfs(node.right, original_sum, flip_used)
        
        # Path 2: Flip current node (if flip not used)
        if not flip_used:
            if node.left:
                dfs(node.left, flipped_sum, True)
            if node.right:
                dfs(node.right, flipped_sum, True)
    
    dfs(tree, 0, False)
    return count[0]

    










"""
Given an array of integers arr and a positive integer k, rotate the array to the right by k steps. A step means moving each element one position to the right, 
with the last element wrapping around to the first position.
Note: Try to solve this in-place with O(1) extra space."""

def rotateArray(arr, k):
    n = len(arr)
    k = k%n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k,n-1)
    return arr


"""
You are given a pattern string and a text string. The pattern may contain regular characters and two special characters:

'.' matches any single character
'*' matches zero or more of the preceding character
"""

def pattern_match(s,p):
    memo = {}
    def match(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if j == len(p):
            return i == len(s)
        if i == len(s):
            return all(c == '*' for c in p[j:])
        
        result = False

        if p[j] == '*':
            result = match(i, j+1) or match(i+1,j)
        elif p[j] == '?' or p[j] == s[ji]:
            result = match(i+1, j+1)
        else:
            result = False
        memo[(i,j)] = result

        return result
    return match(0,0)
            



