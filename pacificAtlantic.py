def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      rows, cols = len(heights), len(heights[0])

      pacific_reachable = set()
      atlantic_reachable = set()

      directions = [(0,1), (0,-1), (1, 0), (-1,0)]

      def dfs(r, c, visited_set, prev_height):
          #base case 1: out of bounds
          if not (0 <= r < rows or 0 <= c < cols):
              return
          #base case 2: already visited
          if (r,c) in visited_set:
              return
          #base case 3: current cell is lower of prev
          if heights[r][c] < prev_height:
              return

          visited_set.add((r,c)) #mark current cell as pacific_reachable

          #explore neighbors
          for dr, dc in directions:
              nr, nc = r + dr, c + dc
              dfs(nr, nc, visited_set, heights[r][c]) #--> current cell become prev for next recursion

      #populate pacific_reachable
      for r in range(rows):
          dfs(r, 0, pacific_reachable, -1000) #left border
      for c in range(cols):
          dfs(0, c, pacific_reachable, -1000) #top border

      #populate atlantic_reachable
      for r in range(rows):
          dfs(r, cols-1, atlantic_reachable, -1000) #right border
      for c in range(cols):
          dfs(rows-1, c, atlantic_reachable, -1000) #top border

      result = []
      for r in range(rows):
          for c in range(cols):
              if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                  result.append([r,c])

      return result
