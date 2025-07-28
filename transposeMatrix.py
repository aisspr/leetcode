  def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
      rows, cols = len(matrix), len(matrix[0])

      t_matrix = [[0]*rows for _ in range(cols)]
      for r in range(rows):
          for c in range(cols):
              t_matrix[c][r] = matrix[r][c]

      return t_matrix
      #return list(zip(*A))
