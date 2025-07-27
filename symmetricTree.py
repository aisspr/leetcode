def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return self._is_mirror(root.left, root.right)

def _is_mirror(self, node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2 or node1.val != node2.val :
        return False
    return (self._is_mirror(node1.left, node2.right) and self._is_mirror(node1.right, node2.left))
