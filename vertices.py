import networkx as nx
import matplotlib.pyplot as plt

while True:
    num_vertices = int(input("Enter the number of vertices (must be greater than 3): "))
    if num_vertices > 3:
        break
    print("Number of vertices must be greater than 3. Try again.")

G = nx.Graph()

G.add_nodes_from(range(1, num_vertices + 1))

print("Now, define edges. Enter edges as pairs of vertices (e.g., 1 2). Type 'done' to finish:")
while True:
    edge_input = input("Enter an edge: ")
    if edge_input.lower() == 'done':
        break
    try:
        u, v = map(int, edge_input.split())
        if u in G.nodes and v in G.nodes:
            G.add_edge(u, v)
        else:
            print("One or both vertices are not valid.")
    except:
        print("Invalid input. Enter two vertex numbers separated by a space.")


nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800)
plt.title(f"Graph with {num_vertices} vertices")
plt.show()
