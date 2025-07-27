def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
    result = []
    def _inorder(node):
        if not node:
            return 
        _inorder(node.left)
        result.append(node.val)
        _inorder(node.right)
    _inorder(root)

    return result
