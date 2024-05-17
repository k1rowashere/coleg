import networkx as nx
import matplotlib.pyplot as plt


class UndirectedGraph:

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.network = [[0 for _ in range(vertex_count)]
                        for _ in range(vertex_count)]

    def display_mst(self, vertex_parent):
        print("Edge \tWeight")
        for i in range(1, self.vertex_count):
            print(vertex_parent[i], "-", i, "\t",
                  self.network[i][vertex_parent[i]])

    def find_min_key(self, key, mstIncluded):
        min_val = float('inf')
        for v in range(self.vertex_count):
            if key[v] < min_val and not mstIncluded[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def create_mst(self):
        key = [float('inf')] * self.vertex_count
        vertex_parent = [None] * self.vertex_count
        key[0] = 0
        mstIncluded = [False] * self.vertex_count
        vertex_parent[0] = -1
        for _ in range(self.vertex_count):
            u = self.find_min_key(key, mstIncluded)
            mstIncluded[u] = True
            for v in range(self.vertex_count):
                if self.network[u][v] > 0 and not mstIncluded[v] and key[v] > self.network[u][v]:
                    key[v] = self.network[u][v]
                    vertex_parent[v] = u
        self.display_mst(vertex_parent)
        return vertex_parent

    def visualize_mst(self, vertex_parent):
        # Visualize the whole graph
        G = nx.Graph()
        for i in range(self.vertex_count):
            for j in range(i, self.vertex_count):
                if self.network[i][j] != 0:
                    G.add_edge(i, j, weight=self.network[i][j])

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=300)
        nx.draw_networkx_edges(G, pos, width=20, edge_color='grey')

        # Highlight the MST edges
        for i in range(1, self.vertex_count):
            nx.draw_networkx_edges(
                G, pos, edgelist=[(vertex_parent[i], i)], width=6, edge_color='r')

        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()


class DirectedGraph:

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.network = [[0 for _ in range(vertex_count)]
                        for _ in range(vertex_count)]
        self.vertex_data = [''] * vertex_count

    def add_edge(self, u, v, weight):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.network[u][v] = weight  # For directed graph

    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.vertex_count:
            self.vertex_data[vertex] = data

    def shortest_path(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.vertex_count
        distances[start_vertex] = 0
        visited = [False] * self.vertex_count
        predecessors = [-1] * self.vertex_count  # Add this line

        for _ in range(self.vertex_count):
            min_distance = float('inf')
            u = None
            for i in range(self.vertex_count):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.vertex_count):
                if self.network[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.network[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u  # Update the predecessor of v

        return distances, predecessors  # Return both distances and predecessors

    def shortest_path_visual(self, start_vertex_data, end_vertex_data):
        _, predecessors = self.shortest_path(start_vertex_data)
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)

        # Construct the shortest path
        path = []
        i = end_vertex
        while i != start_vertex:
            path.append(i)
            i = predecessors[i]
        path.append(start_vertex)
        path = path[::-1]

        # Visualize the whole graph
        G = nx.DiGraph()
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                if self.network[i][j] != 0:
                    G.add_edge(
                        self.vertex_data[i], self.vertex_data[j], weight=self.network[i][j])

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, width=6, edge_color='grey')

        # Highlight the shortest path edges
        for i in range(len(path) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(self.vertex_data[path[i]], self.vertex_data[path[i + 1]])],
                                   width=6, edge_color='r')

        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()


graph = UndirectedGraph(5)

# Add edges to the graph
graph.network[0][1] = 2
graph.network[1][0] = 2

graph.network[1][2] = 3
graph.network[2][1] = 3

graph.network[0][3] = 6
graph.network[3][0] = 6

graph.network[1][3] = 8
graph.network[3][1] = 8

graph.network[1][4] = 5
graph.network[4][1] = 5

graph.network[2][4] = 7
graph.network[4][2] = 7

graph.network[3][4] = 9
graph.network[4][3] = 9

# Create a Minimum Spanning Tree (MST)
vertex_parent = graph.create_mst()

# Visualize the MST
graph.visualize_mst(vertex_parent)
network = DirectedGraph(7)

network.add_vertex(0, 'A')
network.add_vertex(1, 'B')
network.add_vertex(2, 'C')
network.add_vertex(3, 'D')
network.add_vertex(4, 'E')
network.add_vertex(5, 'F')
network.add_vertex(6, 'G')

network.add_edge(3, 0, 4)  # D - A, weight 4
network.add_edge(3, 4, 2)  # D - E, weight 2
network.add_edge(0, 2, 3)  # A - C, weight 3
network.add_edge(0, 4, 4)  # A - E, weight 4
network.add_edge(4, 2, 4)  # E - C, weight 4
network.add_edge(4, 6, 5)  # E - G, weight 5
network.add_edge(2, 5, 5)  # C - F, weight 5
network.add_edge(2, 1, 2)  # C - B, weight 2
network.add_edge(1, 5, 2)  # B - F, weight 2
network.add_edge(6, 5, 5)  # G - F, weight 5

# Visualize the shortest path from D to F
network.shortest_path_visual('D', 'F')
