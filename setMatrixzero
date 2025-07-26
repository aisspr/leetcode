def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    Do not return anything, modify matrix in-place instead.
    """
    rows, cols = len(matrix), len(matrix[0])
    first_col_has_zero = False

    #first pass : Iterate through the matrix to find zeros and mark rows/columns
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_has_zero = True

        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    #second pass; Zero out the inner part of the matrix (excluding first row/column)
    for i in range(1, rows): #start from 2nd row and 2nd cols
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    #third pass: zero out the first row if its marker (matrix[0][0]) is zero
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    #fourth pass: Zero out the first column if 'first_col_has_zero' flag is true
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0
