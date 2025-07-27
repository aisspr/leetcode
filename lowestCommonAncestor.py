def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #base case 1: node is none or p or q
    if root is None or root == p or root == q:
        return root
    
    #recursion to search for p and q in the left subtree
    left_search_result = self.lowestCommonAncestor(root.left, p, q)

    right_search_result = self.lowestCommonAncestor(root.right, p, q)

    #case 1: both p and q found in different subtrees
    if left_search_result and right_search_result:
        return root
    #case 2: only one or both in left subtree
    elif left_search_result:
        return left_search_result
    elif right_search_result:
        return right_search_result
    else:
        return None
