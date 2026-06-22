class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Input:    numCourses      - amount of courses to complete (labeled from 0 index to numCourses - 1)
        #           prerequisites   - an array of course relations [[a, b]], 
        #                             where in order to finish course a you must first finish course b
        
        # Output:   True            - if it is possible to complete this many (numCourses) courses
        #           False           - if it isn't possible to complete
        
        # Approach: 1. Construct a hashMap of prerequisites (adjacencies) by looping through the array
        #           2. Run dfs on prerequisites for (numCourses - 1) times
        #           3. Maintain a hashSet of visited nodes in dfs
        #              which allows us to know if we run into a previously visited node
        #           4. If we run into a previously visited node, then there is a cycle -> return FALSE
        #              We only need to know if the cycle is in the part of the graph we need
        #              CASE A:  If the numCourses is 4
        #                       and there is a cycle for node 5, which isn't a prerequisite in itself to any other courses
        #                       then this cycle doesn't concern us and the output is still TRUE
        #              CASE B:  If the numCourses is 4
        #                       and there is a cycle for node 5
        #                       But node 5 is a prerequisite to any of the nodes from 0 -> 3 then the output is False
        #
        preq_map = defaultdict(list)
        for crs, preq in prerequisites:
            preq_map[crs].append(preq)
        
        def isCycle(crs, visited):
            if crs in visited:
                return True
            if not preq_map[crs]:
                return False
            visited.add(crs)
            preqs = preq_map[crs]
            for p in preqs:
                if isCycle(p, visited):
                    return True
            
            return False
        
        for crs in range(numCourses):
            if isCycle(crs, set()):
                return False
        
        return True