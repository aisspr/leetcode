def postOrder(root):
  result = []
  def _postorder(node):
    if not node:
      return
    _postorder(node.left)
    _postorder(node.right)
    result.append(node.val)
  _postorder(root)
  return result
