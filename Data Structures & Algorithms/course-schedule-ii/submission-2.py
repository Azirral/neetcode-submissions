class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Input: numCourses - number of courses required to take (the required courses are labeled from 0 to numCourses - 1)
        
        # Output: paths - a list of all valid, possible traversals, if there are none return empty list
        
        # Course states:
        #                   seen - course added to output
        #                   cycle   - course not added to output, but added to traversal path
        #                   unvisited - course not added to seen or cycle (output or traversal path)

        preqs = {i: [] for i in range(numCourses)}
        res = []
        seen, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True

            cycle.add(crs)
            for preq in preqs[crs]:
                if not dfs(preq):
                    return False

            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)

            return True
        
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res    
        