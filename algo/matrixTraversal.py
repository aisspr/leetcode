## matrix traversal

#basic traversal

def row_traversal(matrix):
    rows, cols = len(matrix), len(matrix[0])

    row_wise = []
    for i in rows:
        for j in cols:
            row_wise.append(matrix[i][j])
    return row_wise
    
def column_traversal(matrix):
    rows, cols = len(matrix), len(matrix[0])

    column_wise=[]
    for j in cols:
        for j in rows:
            column_wise.append(matrix[i][j])
    return column_wise

def reverse_traversals(matrix):
    rows, cols = len(matrix), len(matrix[0])

    reverse_row =[]

    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            reverse_row.append(matrix[i][j])
    
    reverse_col =[]

    for j in range(cols-1, -1, -1):
        for i in range(rows-1, -1, -1):
            reverse_col.append(matrix[i][j])

#diagonal traversal

matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
rows, cols = len(matrix), len(matrix[0])

def main_diagonal():
    main_diagonal = []
    for i in range(min(rows, cols)):
        main_diagonal.append(matrix[i][i])

def anti_diagonal():
    anti_diagonal = []
    for i in range(min(rows, cols)):
        anti_diagonal.append(matrix[i][cols-1-i])

def all_diagonals():
    all_diag = []
    for k in range(cols): #upper half
        diag = []
        i, j = 0, k
        while i < rows and j < cols:
            diag.append(matrix[i][j])
            j += 1
            i += 1
        all_diag.append(diag)

    for k in range(1, rows): #lower half, exclude main diagonal
        diag = []
        i, j = k, 0
        while i < rows and j < cols:
            diag.append(matrix[i][j])
            j += 1
            i += 1
        all_diag.append(diag)


## spiral traversal

def spiral_traversal():
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, rows-1
    left, right = 0, cols-1

    while top <= bottom and left <= right:
        for j in range(left, right+1):
            result.append(matrix[top][j])
        top += 1

        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left-1, -1):
                result.append(matrix[bottom][j])
            bottom += 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


## transpose matrix

#create a new
def transposeNew():
    transposed = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = mat[i][j]
    return transposed

def inplaceTranspose(): #only for square matrices
    n = rows
    for i in range(n):
        for j in range(1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

## rotation matrix

def rotate90_clock():
    n = rows
    #step 1: transpose
    for i in range(n):
        for j in range(i, cols):
            mat[j][i], mat[i][j] = mat[i][j], mat[j][i]

    #step 2: reverse rows
    for i in range(n):
        mat[i].reverse()
    return mat

def rotate90_counterclock():
    n = rows
    #step 1: reverse rows
    for i in range(n):
        mat[i].reverse()

    #step 2: transpose
    for i in range(n):
        for j in range(i,n):
            mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
    return mat

def rotate180(): #flip vertical + flip horizontal
    return [row[::-1] for row in mat[::-1]]

## Flip oerations

def flip_horizontal():
    return [row[::-1] for row in mat]

def flip_vertical():
    return mat[::-1]

def flood_fill(matrix, start_row, start_col, new_value):
        """Flood fill algorithm with boundary checking"""
        if not matrix or not matrix[0]:
            return matrix
        
        rows, cols = len(matrix), len(matrix[0])
        if not (0 <= start_row < rows and 0 <= start_col < cols):
            return matrix
        
        original_value = matrix[start_row][start_col]
        if original_value == new_value:
            return matrix
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                matrix[r][c] != original_value):
                return
            
            matrix[r][c] = new_value
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(start_row, start_col)
        return matrix