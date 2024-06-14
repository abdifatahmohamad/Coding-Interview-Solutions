# Topological Sort & Kahn’s Algorithm 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle, visited = set(), set()
        catalog = {i:[] for i in range(numCourses)}
        for pre, course in prerequisites:
            catalog[pre].append(course)
        
        def topological_sort(course: int):
            if course in cycle:
                return False
            if course in visited:
                return True 
            cycle.add(course)
            for pre in catalog[course]:
                if not topological_sort(pre):
                    return False 
            cycle.remove(course)
            visited.add(course)
						
            return True 
            
        for i in range(numCourses):
            if not topological_sort(i):
                return False 
        return True 
    
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm
        catalog = {i:[] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]
        
        for pre, course in prerequisites:
            catalog[pre].append(course)
            indegree[course] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # Indicates that there's a cycle, all courses have prerequisites
        if not queue: 
            return False 
        
        while queue: 
            pre = queue.popleft()
            for course in catalog[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            numCourses -= 1
        
        return numCourses == 0
    
