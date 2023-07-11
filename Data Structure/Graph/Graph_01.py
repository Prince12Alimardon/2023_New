import networkx as nx
import matplotlib.pyplot as plt

# Graph yaratish
G = nx.Graph()

# Vertexlarni qo'shish
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Edge'lar bilan aloqalarni qo'shish
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Graphni vizualizatsiya qilish
nx.draw(G, with_labels=True)
plt.show()
