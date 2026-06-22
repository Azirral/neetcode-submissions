class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0
        adjacencies = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adjacencies[n1].add(n2)
            adjacencies[n2].add(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adjacencies[node]:
                if n not in visited:
                    dfs(n)
        

        for n1, n2 in edges:
            if n1 not in visited and n2 not in visited:
                total += 1
                dfs(n1)
        
        return total + (n - len(visited))