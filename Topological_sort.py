# Step 1: Represent the graph using an adjacency list.
# Here, we assume the graph is given as a dictionary where keys are nodes and values are lists of neighboring nodes.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Step 2: Initialize data structures.
visited = {}  # Dictionary to keep track of visited nodes during DFS.
topological_order = []  # List to store the final topological ordering.

# Step 3: Implement the DFS function to visit nodes and perform topological sorting.
def dfs(node):
    visited[node] = True  # Mark the current node as visited.
    for neighbor in graph.get(node, []):
        if not visited.get(neighbor, False):  # If the neighbor is not visited yet.
            dfs(neighbor)
    topological_order.insert(0, node)  # Insert the current node at the beginning of the list.

# Step 4: Perform DFS starting from all unvisited nodes to cover the entire graph.
for node in graph:
    if not visited.get(node, False):  # If the node is not visited yet.
        dfs(node)

# Step 5: The topological_order list now contains the topological sorting of the graph.
print("Topological Order:", topological_order)
