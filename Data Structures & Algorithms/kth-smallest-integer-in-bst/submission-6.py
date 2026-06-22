# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inOrderTraverse(root):
            if not root:
                return
            
            inOrderTraverse(root.left)

            res.append(root.val)

            inOrderTraverse(root.right)

        inOrderTraverse(root)

        return res[k-1]