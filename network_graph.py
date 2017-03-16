import networkx as nx

def network_graph(nodelist,edgelist,column):

	"""Generates a network graph from a list of
	   nodes and edges.

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
	G.add_nodes_from(nodelist)
	G.add_edges_from(edgelist)

	pos = nx.spring_layout(G)
	nx.set_node_attributes(G,'pos',pos)
	clusters = dict(zip(nodelist, column))
	nx.set_node_attributes(G, 'cluster', clusters)
	return G, clusters
