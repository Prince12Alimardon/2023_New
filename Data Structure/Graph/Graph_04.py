# Dictionary of Sets (Himoya ornatilgan lug'at)         
class Graph:
    def __init__(self):
        self.adj_dict = {}

    def add_edge(self, source, destination):
        if source in self.adj_dict:
            self.adj_dict[source].add(destination)
        else:
            self.adj_dict[source] = {destination}

        if destination in self.adj_dict:
            self.adj_dict[destination].add(source)
        else:
            self.adj_dict[destination] = {source}

    def print_graph(self):
        for vertex, neighbors in self.adj_dict.items():
            print(f"Vertex {vertex}: {neighbors}")


# Graph obyektini yaratish
graph = Graph()

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
