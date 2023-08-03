def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node,end=" ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph representation (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
dfs(graph, 'A', visited)  # Output: A B D E F C
