from collections import deque
def BFS(root):
  result = []

  if not root:
    return result

  q = deque()
  q.append(root)

  while q:
    current_level_nodes = []
    level_size = len(q)

    for _ in range(level_size):
      node = q.popleft()
      current_level_nodes.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
      result.append(current_level_nodes)
  return result
