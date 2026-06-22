# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, res = True):
        self.res = res
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = float("-inf")
        maximum = float("inf")
        def isBetweenBoundaries(minimum, root, maximum):
            if not root:
                return True
            return isBetweenBoundaries(minimum, root.left, root.val) \
            and (root.val > minimum and root.val < maximum) \
            and isBetweenBoundaries(root.val, root.right, maximum)
        return isBetweenBoundaries(minimum, root, maximum)
        

            
