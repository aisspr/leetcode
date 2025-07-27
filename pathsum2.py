def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    all_paths = []
    current_path = []

    def dfs(node, current_sum):
        #base case 1
        if not node:
            return
        #action
        current_path.append(node.val)
        current_sum += node.val
        #base case 2
        if not node.left and not node.right:
            if current_sum == targetSum:
                all_paths.append(current_path[:]) #it must be a copy
        else:
            #recursive calls
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        current_path.pop() #backtracking step
    dfs(root, 0)
    return all_paths
