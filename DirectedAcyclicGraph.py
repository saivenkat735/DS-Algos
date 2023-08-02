def has_cycle(graph):
    # Helper function for DFS traversal
    def dfs_visit(node):
        visited[node] = "processing"  # Mark the current node as being processed
        for neighbor in graph.get(node, []):
            if visited.get(neighbor) == "processing":  # If the neighbor is in processing state, cycle found
                return True
            if visited.get(neighbor) is None:  # If the neighbor is unvisited, recursively visit it
                if dfs_visit(neighbor):
                    return True
        visited[node] = "processed"  # Mark the current node as processed (DFS is complete for this node)
        return False

    visited = {}  # Dictionary to keep track of node states: "unvisited", "processing", "processed"

    # Perform DFS from every unvisited node in the graph
    for node in graph:
        if visited.get(node) is None:  # If the node is unvisited
            if dfs_visit(node):
                return True  # Cycle found, return True

    return False  # If no cycle is found after DFS from all nodes, return False

# Example graph representation (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Check if the graph has a cycle
print(has_cycle(graph))  # Output: False (The given graph is a DAG and doesn't have a cycle)
