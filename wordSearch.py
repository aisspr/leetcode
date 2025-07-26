def exist(self, board: List[List[str]], word: str) -> bool:
  """Given an m x n grid of characters board and a string word, return true if word exists in the grid.
  The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
  The same letter cell may not be used more than once."""
  rows = len(board)
  cols = len(board[0])

  def dfs(r,c,k):
      if k == len(word):
          return True
      if r<0 or r>= rows or c<0 or c >= cols or word[k] != board[r][c]:
          return False

      orig_char = board[r][c]
      board[r][c] = '*'
      found = False
      directions = [(1,0), (-1,0), (0,-1), (0,1)]

      for dr, dc in directions:
          new_r, new_c = r+dr, c+dc
          if dfs(new_r, new_c, k+1):
              found = True
              break

      board[r][c] = orig_char
      return found
  
  for r in range(rows):
      for c in range(cols):
          if board[r][c] == word[0]:
              if dfs(r,c,0):
                  return True
  return False
