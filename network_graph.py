def network_graph(nodelist,edgelist,column):

	G=nx.Graph()
	G.add_nodes_from(nodelist)
	G.add_edges_from(edgelist)

	pos=nx.spring_layout(G)
	nx.set_node_attributes(G,'pos',pos)
	cluster=dict(zip(nodelist, column))
	nx.set_node_attributes(G, 'cluster', cluster)
	return G