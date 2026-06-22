# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            level_res = []
            level_q = collections.deque()
            while q:
                pop = q.popleft()
                level_res.append(pop.val)
                if pop.left:
                    level_q.append(pop.left)
                if pop.right:
                    level_q.append(pop.right)
            q = level_q
            res.append(level_res)
        return res
        