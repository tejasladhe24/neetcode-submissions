# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bruteForce(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def maxHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            return 1 + max(maxHeight(root.left), maxHeight(root.right))

        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)
        dia = leftHeight + rightHeight
        sub = max(self.bruteForce(root.left), self.bruteForce(root.right))
        return max(dia, sub)
    
    def dfs_op(self, root:Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.bruteForce(root)
        # return self.dfs_op(root)