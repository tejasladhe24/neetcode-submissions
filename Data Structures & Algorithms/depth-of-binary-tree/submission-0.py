# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_rec(self,root: Optional[TreeNode])-> int:
        if not root:
            return 0

        return 1 + max(self.dfs_rec(root.left), self.dfs_rec(root.right))

    def dfs_itr(self,root: Optional[TreeNode])-> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.dfs_rec(root)
        return self.dfs_itr(root)