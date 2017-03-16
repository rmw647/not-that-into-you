import networkx as nx

def network_graph(data, edgelist, layout, number_of_clusters):

    """Generates a network graph from a list of nodes and edges.

    Parameters
    ----------
    nodelist: list of nodes
    edgelist: list of 0's or 1's indicating existence of connection between
              nodes
    column: column from dataframe indicating cluster assignment

    Returns
    -------
    G: a netwworkx graph object
    cluster: dictionary of node:cluster assignments
    """

    G = nx.Graph()
    G.add_nodes_from(data.iid)
    G.add_edges_from(edgelist)
    clusters = dict(zip(data.iid, data.cluster_assignment))
    shell = {}

    if layout == 'circles':
        for num in range(0, number_of_clusters):
            shell['cluster'+str(num)] = list(data[data.cluster_assignment == num]['iid'])
            shells = list(shell.values())
            pos = nx.shell_layout(G, nlist=shells)

    if layout == 'matches':
        pos = nx.fruchterman_reingold_layout(G, dim=2, k=None,
                                             iterations=50,
                                             scale=1.0,
                                             center=None)

    nx.set_node_attributes(G, 'pos', pos)
    nx.set_node_attributes(G, 'cluster', clusters)
    return G, clusters
