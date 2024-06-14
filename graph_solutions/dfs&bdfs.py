# https://gray-gold-666.notion.site/Python-Graph-Algorithms-61a9fb233ff0436c9482a48f7b684198

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # if graph is bi-directional 
        # add src to des and des to src 
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for node in self.graph:
            print(f'{node} -> {self.graph[node]}')

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        while queue:
            v = queue.popleft()
            print(v, end=" ")
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # DFS iterative 
    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            for w in self.graph[v]:
                if w not in visited:
                    stack.append(w)

    # DFS recursive
def dfs_util(n: int):
    visited = set()

    def dfs(adjacency, i: int) -> None:
        visited.add(i)
        for neighbor in adjacency[i]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)