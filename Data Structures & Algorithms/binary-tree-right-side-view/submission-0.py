# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        res = collections.deque()
        def dfs(root, level):
            if not root:
                return
            if not res or res[0][1] < level:
                res.appendleft([root.val, level])
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
            return
        dfs(root, level)
        res.reverse()
        return [x[0] for x in res]
