import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()

# to do: node and edge generator that links adjacent nodes
G.add_nodes_from(((0, {'weight': 0}), (1, {'weight': math.inf}), (2, {'weight': math.inf}), (3, {'weight': math.inf}), (4, {'weight': math.inf}), (5, {'weight': math.inf}), (6, {'weight': math.inf})))

G.add_edges_from(((0,1, {'weight': 2}), (1,2,{'weight': 1}), (2,3,{'weight': 5}), (3,4,{'weight': 3}), (4,5,{'weight': 2}), (5,0,{'weight': 2}), (0,6,{'weight': 3}), (6,2,{'weight': 1}), (6,4,{'weight': 3})))

pos = nx.spring_layout(G, weight='weight', seed=42)

pre_post = {0:None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}

def update_node(pre, post, edge_weight):
    # G.nodes[n]['weight']\
    print(pre)
    print (post)
    distance = G.nodes[pre]['weight'] + edge_weight #add edge weight
    if (distance < G.nodes[post]['weight']):
        G.nodes[post]['weight'] = distance
        pre_post[post] = pre

for n in G.nodes:
    adjacent = list(G.adj[n])
    adjacent_node_edges = {}
    for node in adjacent:
        adjacent_node_edges[node] = G.edges[n, node]['weight']
    # print(adjacent_node_edges)

    for a in adjacent_node_edges:
    #     if adjacent_node_edges[a] == lowest:
        update_node(n, a, adjacent_node_edges[a])

print(pre_post)

labels = {n: str(n) + '; ' + str(G.nodes[n]['weight']) for n in G.nodes}
nx.draw(G, with_labels=True, labels=labels, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.show()