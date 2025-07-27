def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def validate(node, lower_bound, upper_bound):
        if not node:
            return True
         # Check if the current node's value violates the bounds
        if not (lower_bound < node.val < upper_bound):
            return False
        #recursively validate left subtree

        if not validate(node.left, lower_bound, node.val):
            return False
        
        #recursively validate right
        if not validate(node.right, node.val, upper_bound):
            return False
        return True
    return validate(root, float('-inf'), float('inf'))
        
