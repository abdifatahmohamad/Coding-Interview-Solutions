class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency = defaultdict(list)
        for edge in edges:
            src, des = edge
            adjacency[src].append(des)
            adjacency[des].append(src)
        
        queue = deque([source])
        visited = {source}
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in adjacency.get(node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        # No path found
        return False
        