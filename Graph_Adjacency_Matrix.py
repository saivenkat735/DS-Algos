class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, src, dest, weight=1):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.matrix[src][dest] = weight
            # If the graph is undirected, uncomment the following line:
            # self.matrix[dest][src] = weight

    def remove_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.matrix[src][dest] = 0
            # If the graph is undirected, uncomment the following line:
            # self.matrix[dest][src] = 0

    def has_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            return self.matrix[src][dest] != 0
        return False

    def get_weight(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            return self.matrix[src][dest]
        return None

    def print_matrix(self):
        for row in self.matrix:
            print(row)


# Example usage:
# Create a graph with 4 vertices (0, 1, 2, 3)
graph = GraphAdjacencyMatrix(4)

# Add edges to the graph
graph.add_edge(0, 1, 5)  # Edge from vertex 0 to vertex 1 with weight 5
graph.add_edge(0, 2, 3)  # Edge from vertex 0 to vertex 2 with weight 3
graph.add_edge(1, 2, 2)  # Edge from vertex 1 to vertex 2 with weight 2
graph.add_edge(2, 3, 7)  # Edge from vertex 2 to vertex 3 with weight 7

# Print the adjacency matrix
graph.print_matrix()
