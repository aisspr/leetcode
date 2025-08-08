"""You are given a string containing a pattern like "3[a2[c]]" and need to decode it. 
Numbers indicate how many times to repeat the content within the following brackets.
The pattern is always well-formed and valid.
"""

def patternDecoder(input):
    if not input:
        return
    
    stack = []
    current_num = 0
    current_string = ""

    for c in input:
        if c.isdigit():
            current_num = current_num*10 + int(c)

        elif c == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif c == ']':
            prev_string, num_repeat = stack.pop()
            current_string = prev_string+ current_string*num_repeat
        else:
            current_string += c
    return current_string

"""Given a 2D matrix, return all elements in spiral order (clockwise from outside to inside).
You need to traverse: right → down → left → up → right → down... until all elements are visited."""
def spiralMatrix(mat):
    rows, cols = len(mat), len(mat[0])

    top, bottom = 0, len(rows)-1
    left, right = 0, len(cols)-1

    result = []

    while left < right and top< bottom:
        for col in range(1, cols+1):
            result.append(mat[top][col])
        top += 1

        if top <= bottom:
            for row in range(1, bottom+1):
                result.append(mat[row][right])
            right -= 1

        if left <= right and top <= bottom:
            for col in range(right, left-1, -1):
                result.append(mat[bottom][col])
            bottom -= 1

        if top <= bottom and left <= right:
            for row in range(bottom-1, -1, -1):
                result.append(mat[row][left])
            left += 1
        return result



"""You are given a binary tree and a target sum. Determine if there exists a root-to-leaf path where the sum of node values equals the target.
The tree is represented as a nested array where each node is [value, left_child, right_child]. null represents no child.
"""
def rootToLeafSum(tree, target):
    if not tree:
        return False
    
    
    def dfs(node, current_sum):
        if not node:
            return False
        
        current_sum += node[0]

        left_child = node[1] if len(node) > 1 else None
        right_child = node[2] if len(node) > 1 else None

        if not left_child and not right_child:
            return current_sum == target
        return dfs(left_child, current_sum) or dfs(right_child, current_sum)
    return dfs(tree, 0)
        

