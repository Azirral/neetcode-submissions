# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(p_root, q_root):
            if (p_root and q_root and p_root.val != q_root.val) or (p_root == None and q_root != None) or (p_root != None and q_root == None):
                self.res = False
                return
            if (p_root):
                left = dfs(p_root.left, q_root.left)
            if (q_root):
                right = dfs(p_root.right, q_root.right)
            return 
        dfs(p, q)
        return self.res
