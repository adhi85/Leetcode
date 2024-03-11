class Solution:
    def findOrder(self, numCourses: int, prerequisites) ->int:
        
        preMap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
                
        ans = []
        visited, cycle = set(),set()
        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
                
            cycle.remove(course)
            visited.add(course)
            ans.append(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return ans
            
            