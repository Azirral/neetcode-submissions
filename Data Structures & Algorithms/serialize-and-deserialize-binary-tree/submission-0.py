# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        q = collections.deque([root])

        res = []

        while q:
            pop = q.popleft()
            if not pop:
                res.append("N")
            else:
                res.append(str(pop.val)) 
                q.append(pop.left)
                q.append(pop.right)
                
        return ";".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        res = data.split(sep=";")
        if res[0] == "N":
            return None

        root = TreeNode(int(res[0]))
        q = collections.deque([root])

        index = 1
        while q:
            node = q.popleft()

            if res[index] != "N":
                node.left = TreeNode(int(res[index]))
                q.append(node.left)
            index += 1

            if res[index] != "N":
                node.right = TreeNode(int(res[index]))
                q.append(node.right)
            index += 1
        
        return root
            




        


