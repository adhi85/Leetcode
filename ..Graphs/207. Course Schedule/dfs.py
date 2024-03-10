class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        
        # Prerequisites are mapped.
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        # visited set ==>all nodes for current dfs path
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            if preMap[course] ==[]:
                return True
            
            # Add the course to the visited set to avoid cycles in the graph 
            visited.add(course)
            
            # Going through all the prerequisites of the course and checking if they are visited or not
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            # Remove the course from the visited set after the dfs path is completed for the course 
            visited.remove(course)
            
            preMap[course] = []
            
            return True
            
        # LOOP BECAUSE ==> What If the graph is not fully connected. 1==2,3==4. So if a
        # any false return False
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True