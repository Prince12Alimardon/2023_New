# Adjacency Matrix List (Qo'shilish matritsa ro'yxati)
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices:
            self.matrix[source][destination] = 1
            self.matrix[destination][source] = 1

    def adjacency_list(self):
        adj_list = {}
        for i in range(self.num_vertices):
            neighbors = []
            for j in range(self.num_vertices):
                if self.matrix[i][j] == 1:
                    neighbors.append(j)
            adj_list[i] = neighbors
        return adj_list

    def print_graph(self):
        for vertex, neighbors in self.adjacency_list().items():
            print(f"Vertex {vertex}: {neighbors}")


# Graph obyektini yaratish
graph = Graph(5)

# Aloqalarni qo'shish
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Graphni chop etish
graph.print_graph()
