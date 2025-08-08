def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows== 0:
            return mat

        #step 1: check if possible
        if rows*cols != r*c:
            return mat
        
        flat = []
        for i in range(rows):
            for j in range(cols):
                flat.append(mat[i][j])
        new = []
        for i in range(r):
            row_start_idx = i*c
            row_end_idx = row_start_idx + c
            new_row = flat[row_start_idx:row_end_idx]
            new.append(new_row)
        return new