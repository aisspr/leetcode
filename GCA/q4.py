def climbingStairs(n):
    if n <2:
        return n
    p1 = 2
    p2 = 1
    current = 0
    for i in range(3, n+1):
        current = p1 + p2
        p2 = p1
        p1 = current
    return p1


def houseRobber(nums):
    n = len(nums)
    if n<=1:
        return n
    p2 = nums[0]
    p1 = max(nums[0], nums[1])

    for i in range(2, n):
        current_max=max(nums[i]+p2, p1)
        p2= p1
        p1=current_max
    return p1

"""We're given a binary tree where each node contains a single digit 0-9. Each root-to-leaf path 
in the tree forms a number. For example, the root-to-leaf path 1->2->3 represents the number 123. 
Return the total sum of all root-to-leaf numbers.
"""

def digitTreeSum(t):
    if not t:
        return 0
    def dfs(node, current_number):
        current_num = current_num * 10 + node.val
        if not node.left and not node.right:
            return current_num
        
        left_sum = dfs(node.left) if node.left else None
        right_sum = dfs(node.right) if node.right else None

        return left_sum+right_sum
    return dfs(t, 0)

"""
Given a file system represented as a string where \n\t represents the depth of folders/files, 
find the length of the longest absolute path to a file. A file is guaranteed to have a . in its name."""

def longestPath(fileSystem):
    if not fileSystem:
        return 0
    lines = fileSystem.split('\n')
    max_length = 0
    stack = []

    for line in lines:
        depth = 0
        while depth < len(line) and line[depth] == '\t':
            i+= 1
        name = line[depth:]

        while len(stack)> depth: #means we move to next dir
           stack.pop()

        if stack:
            current_l = stack[-1] + 1 + len(name) #+1 for /
        else:
            current_l = len(name)
        if '.' in name:
            max_length = max(max_length, current_l)
        else:
            stack.append(current_l)
    return max_length


"""You have a certain number of items in stock and receive a list of orders. Each order specifies 
the quantity needed. You want to fulfill as many orders as possible. Return the maximum number of orders you can fulfill.
"""

def filledOrders(orders, k):
    orders.sort()
    fulfilled = 0
    total_used = 0

    for order in orders:
        if total_used + order <= k:
            total_used += order
            fulfilled += 1
        else:
            break
    return fulfilled

"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
    def top(self):
        return self.stack[-1] if self.stack else None
    def getMin(self):
        return self.min_stack[-1] is self.min_stack else None

def minimumStack(operations):
    mini_stack = MinStack()
    result = []

    for op in operations:
        if op[0] == 'MinStack':
            result.append(None)
        elif op[0] == 'push':
            mini_stack.push(op[1])
            result.append(None)
        elif op[0] == 'pop':
            result.append(mini_stack.pop())
        elif op[0] == 'top':
            result.append(mini_stack.top())
        elif op[0] == 'getMin':
            result.append(mini_stack.getMin())

"""Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically."""
def countClouds(grid)
    m, n = len(grid), len(grid[0])

    cnt_islands = 0

    def dfs(r,c):
        if r < 0 or r >= m or c <0 or c>= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        directions = [(0,1),(0,-1), (-1,0), (1,0)]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            dfs(nr,nc)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                cnt_islands += 1
                dfs(i,j)
    return cnt_islands

"""You have n tasks and n workers. Each worker has a different efficiency level, 
and each task has a different difficulty level. You want to assign tasks to workers 
such that the total time is minimized. The time for a worker to complete a task is task_difficulty / worker_efficiency."""
    
def taskAssignment(tasks, workers):
    total_time = 0
    tasks.sort(reverse=True) #hardest first
    workers.sort(reverse=True) #most efficient first

    for i in range(len(tasks)):
        total_time += tasks[i]/workers[i]
    return total_time


"""
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element"""
def regularExpressionMatching(s,p):
    memo = {}
    def dp(i,j):
        # 1. the next char is not a *
        if (i,j) in memo:
            return memo[(i,j)]
        
        #endo of pattern
        if j == len(p):
            return i == len(s)

        first_match = i < len(s) and (p[j]==s[i] or p[j]== '.')

        #handle the '*' case
        if j+1 < len(p) and p[j+1] == '*':
            # Two options: # 1. Skip the pattern (0 occurrences)
            # # 2. Use the pattern if first char matches, then advance in string

            result = dp(i,j+2) or (first_match and dp(i+1, j+1))

        else:
            result = first_match and dp(i+1, j+1)

        memo[(i,j)] = result
        return result   
    return dp(0,0) 



def longestIncreasingSubsequence(nums):
    if not nums:
        return 0
    import bisect
    tails = []
    for el in nums:
        pos = bisect.bisect_left(tails, el)
        if pos == len(tails):
            tails.append(el)
        else:
            tails[pos] = el
    return len(tails)



"""You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money. Return the fewest number of coins
 that you need to make up that amount. If that amount of money cannot be made up by any combination 
 of the coins, return -1.
"""

def coinChange(coins, amount):
    dp= [1000]*(amount-1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in cois:
            dp[i] = max(dp[i], dp[i-coin])
    return dp[amount] if dp[amount] != 1000 else -1
    

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of 
shortest transformation sequence from beginWord to endWord.
"""
def wordLadder(beginWord, endWord, wordList):
    from collections import deque
    import string

    if endWord not in wordList:
        return 0
    
    wordset = set(wordList)
    q = deque([(beginWord,1)])
    visited = {beginWord}

    while q:
        word, length = q.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                new_word = word[:i] + c + word[i+1:] #generate all possible words that are one letter different from word
                if new_word in wordset and new_word not in visited:
                    visited.add(new_word)
                    q.append([(new_word, length+1)])
    return 0

"""A message containing letters from A-Z can be encoded into numbers using the mapping A=1, B=2, ..., Z=26. 
Given a string containing only digits, determine the total number of ways to decode it.
"""

def decodeWays(s):
    if not s or s[0]=='0':
        return 0
    dp = [0]*(len(s)+1)
    dp[0] = 1 #num of ways to decode the empty string
    dp[1] = 1

    for i in range(2, len(s)):
        if s[i-1] != 0: #single digit decode
            dp[i] += dp[i-1]

        #two digit decode
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    return dp[n]

"""Robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at
 any point in time. How many possible unique paths are there?
"""

def uniquePaths(m,n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


"""Given an array of strings words and a width maxWidth, format the text such that each line has exactly 
maxWidth characters and is fully (left and right) justified.
"""

def textJustification(words, maxWidth):


"""
You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, 
where one number is taken from a and the other from b, that can be added together to get a sum of v."""

def sumOfTwo(a,b, v):
    setb = set(b)
    for el in a:
        if v-a in set:
            return True
    return False


"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-indexed). 
Find the sum of the elements between the given indices, inclusive."""

def sumInRange(arr, queries):
    prefix = [0]
    for el in arr:
        prefix.append(prefix[-1]+el)

    result = []
    for start, end in queries:
        result.append(prefix[end+1]-prefix[start])
    return result


"""
Given an array of integers and an integer k, determine whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k."""

def containsDuplicates(arr, k):
   
    seen = {}

    for i, el in enumerate(arr):
        if el in seen and i-seen[el] <= k:
            return True
        seen[el] = i
    return False


"""
Given a string str and array of pairs, where each pair contains two distinct indices in the string, find the lexicographically largest string 
that can be obtained by swapping characters at the given indices any number of times."""

def swapLexOrder(s, pairs):
    n = len(s)

    graph = [[] for _ in range(n)]
    for u,v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False]*n
    result = list(s)

    for i in range(n):
        if not visited[i]:
            idx = []
            chars = []

            stack = [i]
            visited[i] = True

            while stack:
                u = stack.pop()
                idx.append(u)
                chars.append(str(u))

                for v in graph[u]:
                    if not visited[v]:
                        visited[v]= True
                        stack.append(v)
            chars.sort(reverse=True)
            idx.sort()

            for index, char in zip(idx, chars):
                result[idx] = char
    return ''.join(result)



### classifyStrings
"""
You are given a string. Your task is to count the number of ways of choosing a non-empty substring such that 
it contains an equal number of uppercase and lowercase letters. """

def classifyStrings(s):
    if not s:
        return 0
    
    prefix_sum_cnt = {0:1}
    valid_substring_cnt = 0
    current_balance = 0

    for c in s:
        if c.islower():
            current_balance -= 1
        elif c.isupper():
            current_balance += 1

        if current_balance in prefix_sum_cnt:
            valid_substring_cnt += prefix_sum_cnt[current_balance]
            prefix_sum_cnt[current_balance] += 1
        else:
            prefix_sum_cnt[current_balance] = 1
    return valid_substring_cnt




"""Given an array of strings strs, group the anagrams together."""

def groupAnagrams(arr):
    from collections import defaultdict

    groups = defaultdict(list)

    for s in arr:
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


"""**Description:**
Given an array of integers, find the number of pairs (i, j) such that 0 <= i < j < len(numbers), where numbers[i] and numbers[j] satisfy the following conditions:
1. They have the same number of digits
2. They differ in exactly one digit position"""

def digitDifferencePairs(arr):
    if not arr:
        return 0
    def differsByOne(a,b):
        stra, strb = str(a), str(b)
        if len(stra) != len(strb):
            return False
        diff_cnt = sum(c1 != c2 for c1, c2 in zip(stra,strb))
        return diff_cnt == 1
    
    cnt = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if differsByOne(arr[i], arr[j]):
                cnt += 1
    return cnt




    