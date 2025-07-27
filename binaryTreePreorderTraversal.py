def preorderTraversal(root):
  result = []
  def _preorder(node):
    if not node:
      return
    result.append(node.val)
    _preorder(node.left)
    _preorder(node.right)
  _preorder(root)
  return result
