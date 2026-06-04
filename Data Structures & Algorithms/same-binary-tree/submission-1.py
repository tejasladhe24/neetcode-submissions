# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.rec(p.left, q.left) and self.rec(p.right, q.right)
        else:
            return False
    
    def stk(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return self.rec(p,q)
        return self.stk(p,q)
