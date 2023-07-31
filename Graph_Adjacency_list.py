class GraphAdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest, weight=1):
        self.adj_list.setdefault(src, []).append((dest, weight))
        # If the graph is undirected, uncomment the following line:
        # self.adj_list.setdefault(dest, []).append((src, weight))

    def remove_edge(self, src, dest):
        if src in self.adj_list:
            self.adj_list[src] = [(v, w) for v, w in self.adj_list[src] if v != dest]
            # If the graph is undirected, uncomment the following line:
            # if dest in self.adj_list:
            #     self.adj_list[dest] = [(v, w) for v, w in self.adj_list[dest] if v != src]

    def has_edge(self, src, dest):
        return dest in [v for v, _ in self.adj_list.get(src, [])]

    def get_weight(self, src, dest):
        for v, w in self.adj_list.get(src, []):
            if v == dest:
                return w
        return None

    def print_adj_list(self):
        for src, neighbors in self.adj_list.items():
            print(f"{src} -> {neighbors}")


# Example usage:
graph = GraphAdjacencyList()

graph.add_edge(0, 1, 5)  # Edge from vertex 0 to vertex 1 with weight 5
graph.add_edge(0, 2, 3)  # Edge from vertex 0 to vertex 2 with weight 3
graph.add_edge(1, 2, 2)  # Edge from vertex 1 to vertex 2 with weight 2
graph.add_edge(2, 3, 7)  # Edge from vertex 2 to vertex 3 with weight 7

graph.print_adj_list()
