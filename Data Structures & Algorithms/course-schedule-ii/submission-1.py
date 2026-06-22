class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Input: numCourses - number of courses required to take (the required courses are labeled from 0 to numCourses - 1)
        
        # Output: paths - a list of all valid, possible traversals, if there are none return empty list
        
        # Course states:
        #                   outputted - course added to output
        #                   visited   - course not added to output, but added to path
        #                   unvisited - course not added to output or path

        preqs = {i: [] for i in range(numCourses)}
        res = []
        outputted, visited = set(), set()

        def dfs(crs):
            if crs in visited:
                return False
            if crs in outputted:
                return True

            visited.add(crs)
            for preq in preqs[crs]:
                if not dfs(preq):
                    return False

            visited.remove(crs)
            outputted.add(crs)
            res.append(crs)

            return True
        
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res    
        