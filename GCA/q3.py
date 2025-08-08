"""
A cryptarithmetic puzzle is a mathematical game where the goal is to find the correspondence between letters and digits,
ff such that the given arithmetic equation holds true. Given a cryptarithmetic equation and a solution, verify if the solution is correct."""

def isCryptSolution(crypt, solution):
    char2digit = {c:d for c, d in solution}
    numbers = []

    for word in crypt:
        if len(word) > 1 and char2digit[word[0]] == '0':
            return False
        num_str = ''.join(char2digit[c] for c in word)
        numbers.append(int(num_str))
    n1, n2, n3 = numbers[0], numbers[1], numbers[2]
    return n1+n2 == n3

#print (isCryptSolution(["SEND", "MORE", "MONEY"], [["O", "0"], ["M", "1"], ["Y", "2"], ["E", "5"], ["N", "6"], ["D", "7"], ["R", "8"], ["S", "9"]]))

"""Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.
"""

def hasPathWithGivenSum(t,s):
    if not t:
        return s==0
    
    if not t.left and not t.right:
        return s == t.val
    
    remaining_sum = s - t.val
    left = hasPathWithGivenSum(t.left, remaining_sum) if t.left else False
    right = hasPathWithGivenSum(t.right, remaining_sum) if t.right else False

    return left or right


"""
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

def isSymmetricTree(t):
    def _is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False 
        return _is_mirror(left.left, left.right) and _is_mirror(right.left, right.right)
    if not t:
        return True
    return _is_mirror(t.left, t.right)

"""Consider a special family tree where all persons can be either engineers or doctors. This tree has the following properties:

- The root (first generation) is an engineer
- For any person who is an engineer, his direct children will be engineer, doctor (in that order)
- For any person who is a doctor, his direct children will be doctor, engineer (in that order)

Given the level and position of a person in this special tree, find their profession."""

def findProfession(level, pos):
    
    ones_cnt = bin(pos).count('1')
    return 'doctor' if ones_cnt%2 == 1 else 'engineer'




"""
Given a singly linked list of integers, determine whether or not it's a palindrome."""

def isListPalindrome(l):
    values = []
    current = l
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]


"""You're given two huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. 
The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoHugeNumbers(a,b):
    dummy_head = ListNode(-1)
    current = dummy_head

    carry = 0

    while a or b or carry:
        v1 = a.val if a else 0
        v2 = b.val if b else 0

        total_sum = v1 + v2 + carry
        new_v = total_sum % 10000
        carry = total_sum // 10000

        current.next = ListNode(new_v)
        current = current.next
        if a: 
            a = a.next
        if b :
            b = b.next
    return dummy_head.next

"""Construct a square matrix with a given parameter n filled with numbers from 1 to n² in spiral order.
"""

def spiralNumbers(n):
    matrix = [[0]*n for _ in range(n)]

    top, bottom = 0, n-1
    left, right = 0, n-1
    i = 0
    j = 0
    val = 1

    while left <= right and top <= bottom:
        for col in range(left, right+1):
            matrix[top][col] = val
            val += 1
        top += 1

        for row in range(top, bottom+1):
            matrix[row][right] = val
            val += 1
        right -=1

        if top <= bottom:
            for col in range(right, left-1, -1):
                matrix[bottom][col] = val
                val += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top-1, -1):
                matrix[row][left] = val
                val += 1
            left += 1
    return matrix

"""
Given a string consisting of lowercase English letters, find the largest square number which can be 
obtained by reordering the string's characters and replacing them with any digits you want. Return the result as a string. 
If there is no solution, return "-1"."""

def constructSquare(s):
    from collections import Counter
    n = len(s)
    char_cnt = sorted(list(Counter(s).values())) #1. Compute the frequency pattern of the input string

    max_num = int('9'*n)
    max_sqrt = int(max_num**0.5)

    min_num = 10**(n-1)
    min_sqrt = int(min_sqrt**0.5)

    for i in range(max_sqrt, min_sqrt-1, -1):
        square = i*i
        square_str = str(square)

        if len(square_str) != n:
            continue

        digit_cnt = sorted(list(Counter(square_str.values())))
        if digit_cnt == char_cnt:
            return square_str
    return -1

"""You have a string `s` that consists of English letters, whitespace characters, and possibly some other characters. 
You want to modify this string as follows:
- If a character is an uppercase English letter, change it to lowercase and add a space before it (except if it's the first character).
"""
def amendSentence(s):
    if not s:
        return ''
    ans = []
    for i,c in enumerate(s):
        if c.isupper():
            if i> 0 and s[i-1] != ' ':
                ans.append(' ')
            ans.append(c.lower())
        else:

            ans.append(c)
    return ''.join(ans)
print(amendSentence('Hello World!'))
            
"""Find the kth largest element in an unsorted array.
"""

def kthLargest(arr):
    import heapq
    return heapq.nlargest(k, arr)

"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number."""
def deleteDigit(n):
    s = str(n)
    max_num = 0
    for i in range(len(s)):
        new_s = int(s[:i]+s[i+1:])
        max_num = max(max_num, new_s)
    return max_num

"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements."""
def arrayMaxConsecutiveSum(arr, k):
    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum = current_sum + arr[k] - arr[i-k]
        max_sum = max(current_sum, max_sum)
    return max_sum

"""
Given the positions of a white bishop and a black pawn on the standard chessboard, determine whether the bishop can capture the pawn in one move."""

def bishopAndPawn(bishop, pawn):
    def pos2coords(pos):
        return ord(pos[0]-ord('a')), int(pos[1])-1
    
    bx, by = pos2coords(bishop)
    px, py = pos2coords(pawn)

    return abs(bx-px) == abs(by-py)

"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string;
ie: b occurs no more times than a; c occurs no more times than b; etc."""

def beautifulString(s):
    from collections import Counter
    cnt = Counter(s)

    prev_cnt = float('inf')

    for i in range(26):
        c = chr(ord('a')+1)
        current_cnt = cnt.get(c, 0)
        if current_cnt > prev_count:
            return False
        prev_cnt = current_cnt
    return True


"""An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com"). 
The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of 
different special characters. Here you can see the general email address syntax."""

def findEmailDomain(address):
    return address.split('@')[-1]


"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome."""

def buildPalindrome(s):
    def is_palidrome(s):
        return s == s[::-1]
    
    for i in range(len(s)):
        candidate = s + s[:i][::-1]
        if is_palidrome(candidate):
            return candidate
    return s + s[:-1][::-1]

"""Given a tree, find the longest path between any two nodes."""

def treeLongestPath(adjacency_list):
    if not adjacency_list:
        return 0
    max_diameter = [0]
    def dfs(node, parent):
        child_depths = []
        for neighbor in adjacency_list[node]:
            if neighbor != parent:
                depth = dfs(neighbor, node)
                child_depths.append(depth)
        child_depths.sort(reverse=True) #decreasing order

        longest = child_depths[0] if child_depths else 0
        second_longest = child_depths[1] if child_depths else 0

        diam_here = longest + second_longest
        max_diam[0] = max(max_diameter[0], diam_here)
        return longest + 1
    
    dfs(0, -1)
    return max_diameter[0]


"""A restaurant received n orders. Each order consists of specific dishes with their quantities. 
Find which dishes were ordered the most."""
        
def restaurantGuestList(orders):
    from collections import Counter

    dish_cnt = Counter()

    for order in orders:
        for dish, quantity in order:
            dish_cnt[dish] += quantity
    if not dish_cnt:
        return []
    
    max_quantity = max(dish_cnt.values())

    result = [dish for dish, cnt in dish_cnt.items() if cnt == max_quantity]
    result.sort()
    return result

"""Given a telephone number, return all possible words that can be formed using the letters on the keypad.
"""

def telephoneWords(num):
    mapping = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def backtrack(idx, current):
        if idx == len(num):
            return [current]
        digit = num[idx]
        if digit not in mapping:
            return backtrack(idx+1, current+digit)
        result = []
        for letter in mapping[digit]:
            result.extend(backtrack(idx+1, current+letter))
        return result
    return backtrack(0, '')
        

"""
In a 2D city, the skyline is the outer contour of the building heights. You can increase the height 
of any number of buildings, without changing the skyline. Find the maximum total sum that the height 
of the buildings can be increased."""

def maxIncreaseKeepingSkyline(grid):
    rows, cols = len(grid), len(grid[0])

    row_max = [max(row) for row in grid]
    col_max = [max(grid[r][c]) for r in range(rows) for c in range(cols)]

    total_increase = 0
    for r in range(rows):
        for c in range(cols):
            max_possible = min(row_max[r], col_max[c])
            total_increase += max_possible -grid[r][c]
    return total_increase

"""Once upon a time, in a kingdom far, far away, there lived a King Byteasar I. As a kind and wise ruler, 
he did everything in his (unlimited) power to make life for his subjects comfortable and pleasant. One day 
the king decided to build a new road system in his kingdom such that it would be possible to drive from any 
town to any other town.  design or determine a road system such that it is possible to travel from any town 
to any other town in the kingdom.
"""

def newRoadSystem(roadRegister):
    n = len(roadRegister)
    for i in range(n):
        out_degree = sum(roadRegister[i]) # This is the sum of '1's in row 'i'
        in_degree = sum(roadRegister[j][i] for j in range(n)) #This is the sum of '1's in column 'i'

        if out_degree != in_degree:
            return False
    return True

"""A step-by-step process of obtaining the digital root is as follows:

1. Take the sum of digits of the initial number
2. If the obtained sum has only one digit, then it is a digital root
3. Otherwise, replace the initial number with this sum and repeat the process

Find the most frequent digit sum obtained during this process.
"""

def mostFrequentDigitSum(n):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    sums = []
    current = abs(n)

    while current:
        current = digit_sum(current)
        sums.append(current)
    if not sums:
        return digit_sum(abs(n))
    from collections import Counter
    cnt = Counter(sums)
    return max(cnt.keys())


"""
You have a strongly connected directed graph that has positive weights on all edges. 
You want to find the shortest path from vertex s to vertex t."""

def editDistance(g,s):
    import heapq
    n = len(g)

    dist = [float('inf')]*n
    dist[s] = 0
    pq = [(0,s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in range(n):
            if g[u][v] != -1: #edge exists
                if dist[u] + g[u][v] < dist[v]:
                    dist[v] = dist[u] + g[u][v]
                    heapq.heappush(pq, (dist[v], v))
    
    return [d if d!=float('inf') else -1 for d in dist]


"""You are given two strings s and t of the same length, consisting of uppercase English letters. 
Your task is to find the minimum number of "replacement operations" needed to get an anagram of string s from string t.
"""

def createAnagram(s,t):
    from collections import Counter
    cnt_s = Counter(s)
    cnt_t = Counter(t)

    operations = 0
    for c in cnt_s:
        if cnt_s[c] > cnt_t.get(c,0):
            operations += cnt_s[c] - cnt_t.get(c,0)

    return operations


"""
Given a string s, return the longest palindromic substring in s."""

def longestPalindromicSubstring(s):
    n = len(s)
    start = 0
    max_len = 0

    if n<2:
        return s
    for i in range(n):
        left_o = i
        right_o = i
        current_l_o = 0

        #expand outwords from the center
        while left_o >= 0 and right_o < n and s[left_o] == s[right_o]:
            current_l_o = right_o - left_o + 1
            if current_l_o > current_max:
                max_len = current_l_o
                start = left_o
            left_o -= 1
            right_o += 1

        left_e = i
        right_e = i+1
        current_l_e = 0

        while left_e >= 0 and right_e < n and s[left_e] == s[right_e]:
            current_l_e = right_e - left_e + 1
            if current_l_e > current_max:
                max_len = current_l_e
                start = left_e
            left_e -= 1
            right_e -= 1

        return s[start:start+max_len]

# v2

    def expand(left, right):
        while left >= 0 and right < s and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left + 1

    if n < 2:
        return s
    for i in range(len(s)):
        l1 = expand(i,i)
        l2 = expand(i, i+1)

        current_max = max(l1, l2)
        max_len= current_max
        start = i - (current_max-1)//2
    return s[start:start+max_len]


"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
"""
def validParentheses(s):
    mapping = {'}':'{', ']':'[', ')':'('}
    stack = []

    for c in s:
        if c in mapping:
            if not stack or stack.pop() != mapping[c]:
                return False
            else:
                stack.append(c)
    return not stack

"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai. Return true if you can finish all courses.
"""

def courseSchedule(numCourses, prereq):
    from collections import defaultdict
    graph = defaultdict(list)
    for course, req in prereq:
        graph[req].append(course)

    visited = set()
    visiting = set()

    def dfs(node):
        if node in visiting:
            return False #because cycle
        if node in visited:
            return True 
        
        visiting.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False #propagate cycle detected
        visiting.remove(node)
        visited.add(node)

        return True

    for course_node in range(numCourses):
        if not dfs(course_node):
            return False
    return True

"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.
"""

def wordSearch(board, word):
    m,n = len(board), len(board[0])
    def dfs(r,c, idx):
        if idx == len(word):
            return True
        if (r<0 or r >=m) or (c<0 or c>=n) or (board[r][c] != word[idx]):
            return False
        
        temp = board[r][c]
        board[r][c] = '#'
        found = False

        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for dr,dc in directions:
            nr,nc = r+dr, c+dc
            if dfs(nr, nc, idx+1):
                found = True
                break
        board[r][c] = temp
        return found
    
    for i in range(m):
        for j in range(n):
            if dfs(i,j,0):
                return True
    return False


"""Implement a trie (prefix tree) with insert, search, and startsWith methods.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    

"""Given a tournament bracket represented as a binary tree, determine the winner by comparing adjacent players.
""" 

def tournament(tree):
    if not tree:
        return None
    
    if not tree.left and not tree.right:
        return tree.val
    
    left_winner = tournament(tree.left) if tree.left else None
    right_winner = tournament(tree.right) if tree.right else None

    if left_winner is None:
        return right_winner
    if right_winner is None:
        return left_winner
    return max(left_winner, right_winner)


"""Given player scores and names, create a leaderboard with proper ranking and tiebreaker handling."""

def leaderboard(players):
    sorted_players = sorted(players, key=lambda x: (-x[1], x[0]))

    leaderboard = []
    current_rank = 1

    prev_score = None

    for i, (name, score) in enumerate(players):
        if score != prev_score:
            current_rank = i+1
            leaderboard.append([current_rank,name, score])
        prev_score = score
    return leaderboard

print(leaderboard([["Alice", 100], ["Bob", 90], ["Charlie", 100]]))
