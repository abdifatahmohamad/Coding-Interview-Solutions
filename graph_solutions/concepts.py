# Directed Acyclic Graph (DAG):
"""
    DAG means a graph that is directed and contains no cycles.
    Example from Leetcode - 97. All Paths From Source to Target:
    graph = [[1,2],[3],[3],[]]
    adjacency = {i: node for i, node in enumerate(graph)}
    Example 2 from Leetcode - 1557. Minimum Number of Vertices to Reach All Nodes
    n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    adjacency = {i: [] for i in range(n)}
    for edge in edges:
        src, dest = edge
        adjacency[src].append(dest)
"""

# Undirected Graph: If the graph bi-directional means graph in undirected

"""
undirected = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]

adjacency = {}
for i in range(len(undirected)):
    adjacency[i] = undirected[i]

Adjacency List:

{
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

Theory:

An Undirected Graph is a graph where edges have no direction. This means that if there is an edge between nodes u and v, it can be traversed in both directions. Undirected graphs are used to represent bi-directional relationships, such as social networks, where connections do not have a direction.

In this example:

    Node 0 is connected to nodes 1 and 2.
    Node 1 is connected to nodes 0, 2, and 3.
    Node 2 is connected to nodes 0, 1, and 3.
    Node 3 is connected to nodes 1 and 2.

*********************************************************
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
Create the adjacency list from the matrix
adjacency = {i : [] for i in range(n)}
for edge in edges:
    u, v = edge
    adjacency[u].append(v)
    adjacency[u].append(u) # If the graph is undirected, add this line, remove if not

# Using defaultdict list collections
adjacency = defaultdict(list)
for src, des in edges:
    adjacency[src].append(des)
    adjacency[des].append(src) # If the graph is undirected, add this line, remove if not
"""

# Directed Graph with a Cycle

"""
directed = [[1], [2], [0, 3], []]

adjacency = {}
for i in range(len(directed)):
    adjacency[i] = directed[i]

Adjacency List:

{
    0: [1],
    1: [2],
    2: [0, 3],
    3: []
}

Theory:

A Directed Graph (or Digraph) is a graph where edges have a direction, indicated by an arrow. A directed graph with a cycle means that it is possible to start at a node and follow a sequence of directed edges that eventually loop back to the starting node.

In this example:

    Node 0 points to node 1.
    Node 1 points to node 2.
    Node 2 points to nodes 0 and 3.
    Node 3 has no outgoing edges.
    There is a cycle: 0 -> 1 -> 2 -> 0.
"""

# Weighted directed graph:

"""
weighted = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (3, 5)], []]

adjacency = {}
for i, node in enumerate(weighted):
    adjacency[i] = node

Adjacency List:

{
    0: [(1, 2), (2, 1)],  # The second value in each tuple is the weight of the edge.
    1: [(2, 3)],
    2: [(0, 4), (3, 5)],
    3: []
}

Theory:

A Weighted Directed Graph is a graph where edges have both direction and weight. The weight of an edge can represent various metrics such as distance, cost, or time. These graphs are often used in applications like routing algorithms (e.g., finding the shortest path).

In this example:

    Node 0 has edges pointing to node 1 with weight 2 and node 2 with weight 1.
    Node 1 has an edge pointing to node 2 with weight 3.
    Node 2 has edges pointing to node 0 with weight 4 and node 3 with weight 5.
    Node 3 has no outgoing edges.
"""