class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node.val in visited:
                return visited[node.val]
            
            new_node = Node(node.val)
            visited[node.val] = new_node
            for nei in node.neighbors:
                new_node_nei = dfs(nei)
                if new_node_nei:
                    new_node.neighbors.append(new_node_nei)
            
            return new_node
        
        copy = dfs(node)

        return copy