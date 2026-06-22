class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Input:  n       - number of nodes in the undirected graph
                edges   - list of adjacencies
        
        Output: True    - if all nodes are reachable and there is no cycle 
                False   - if a node isn't reachable or if there is a cycle
        """
        if len(edges) > (n - 1):
            return False

        adjacencies = [[] for node in range(n)]
        visited = set()

        for v1, v2 in edges:
            adjacencies[v1].append(v2)
            adjacencies[v2].append(v1)
        
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)    

            for v in adjacencies[node]:
                if v not in visited and not dfs(v):
                    return False
            return True
        
        return dfs(0) and len(visited) == n