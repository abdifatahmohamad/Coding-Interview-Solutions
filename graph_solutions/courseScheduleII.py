# Course Schedule II
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses, prerequisites):
        # topological sort DFS
        visited, cycle, topsort = set(), set(), []
        catalog = {i:[] for i in range(numCourses)}
        
        for pre, course in prerequisites:
            catalog[pre].append(course)
        
        def topo_sort(course):
            if course in cycle:
                return False 
            if course in visited:
                return True 
            cycle.add(course)
            for pre in catalog[course]:
                if not topo_sort(pre):
                    return False 
            cycle.remove(course)
            visited.add(course)
            topsort.append(course)
            return True 
            
        for i in range(numCourses):
            if not topo_sort(i):
                return []
        
        return topsort
        
    
    def find_Order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm
        catalog = {i:[] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]
        
        for pre, course in prerequisites:
            catalog[pre].append(course)
            indegree[course] += 1
        
        queue, topsort, nodes = collections.deque(), collections.deque(), 0
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue: 
            pre = queue.popleft()
            nodes += 1
            for course in catalog[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            topsort.appendleft(pre)
        
        # Indicates that there's a cycle
        if nodes != numCourses:
            return []
        
        return topsort