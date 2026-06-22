class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        oldToNew = {}
        if not node:
            return None
        oldToNew[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            pop = q.popleft()
            for nei in pop.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[pop].neighbors.append(oldToNew[nei])

        return oldToNew[node]