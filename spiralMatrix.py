def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])
    """Given an m x n matrix, return all elements of the matrix in spiral order."""
    result = []

    top = 0
    bottom = rows -1
    left = 0
    right = cols -1

    while top <= bottom and left <= right:
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top +=1

        if top <= bottom:
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -= 1
        
        if top <= bottom and left <= right:
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if top <= bottom and left <= right:
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
