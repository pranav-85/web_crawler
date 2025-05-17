import networkx as nx
import matplotlib.pyplot as plt

def build_graph(edges):
    """
    Build a directed graph from a list of edges.

    Args:
        edges (list of tuples): A list of tuples where each tuple represents an edge (source, target).

    Returns:
        networkx.DiGraph: A directed graph constructed from the provided edges.
    """
    G = nx.DiGraph()
    G.add_edges_from(edges)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.5)  # Better spacing
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1000)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="monospace")

    plt.title("Crawl Graph")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("data/crawl_graph.png")
    plt.show()