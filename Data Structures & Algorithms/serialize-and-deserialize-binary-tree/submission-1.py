# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ";".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(";")

        if vals[0] == "N":
            return None
        
        r = 0

        def dfs(index):
            nonlocal r, vals
            if vals[index] == "N":
                r += 1
                return None
            node = TreeNode(int(vals[index]))
            r += 1

            node.left = dfs(index + 1) if (index + 1) < len(vals) else None
            node.right = dfs(r) if r < len(vals) else None


            return node
        root = dfs(r)

        return root

