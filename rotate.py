def rotate(self, matrix: List[List[int]]) -> None:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    #step 1: transpose the matrix
    for i in range(n):
        for j in range(i+1,n): # j starts from i + 1 to swap each pair only once
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #step 2: reverse row horizontally
    for i in range(n):
        matrix[i].reverse()
