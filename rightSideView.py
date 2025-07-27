  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      result = []
      from collections import deque

      if not root:
          return result

      q = deque()
      q.append(root)

      while q:
          level_size = len(q)
          right_most_value = None

          for _ in range(level_size):
              node = q.popleft()
              right_most_value = node.val #we process the node left to right so last is rightmost

              if node.left :
                  q.append(node.left)
              if node.right:
                  q.append(node.right)
          result.append(right_most_value)
      return result
