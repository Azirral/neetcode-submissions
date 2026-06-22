# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDepth(self, root, depth, max_depth) -> int:
        if not root.left and not root.right:
            return depth
        
        if root.left:
            max_depth = max(max_depth, self.findDepth(root.left, depth + 1, max_depth))
        if root.right:
            max_depth = max(max_depth, self.findDepth(root.right, depth + 1, max_depth))
        
        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        max_depth = float("-inf")
        if root.left:
            max_depth = max(max_depth, self.findDepth(root.left, 2, max_depth))
        if root.right:
            max_depth = max(max_depth, self.findDepth(root.right, 2, max_depth))
        return max_depth