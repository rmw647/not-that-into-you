import pandas as pd
import network_graph
import networkx
import generate_clusters
import get_matches

def test_network_graph():
    """tests that network_graph.py is working as expected"""

    filepath = 'https://raw.githubusercontent.com/rmw647/not-that-into-you/master/Speed%20Dating%20Data.csv'
    data = pd.read_csv(filepath, encoding='latin1')
    keep_columns = ['iid', 'pid', 'match', 'age', 'sports', 'dining', 'art',
                    'hiking', 'reading', 'theater',  'music', 'exphappy']
    test_data = data[keep_columns].dropna(how='any')
    test_people = test_data.drop_duplicates(subset='iid')
    num_clusters = 3

    cluster_columns = ['sports', 'dining', 'art', 'hiking', 'reading',
                       'theater',  'music', 'exphappy']
    test_people = generate_clusters.generate_clusters(test_people,
                                                      cluster_columns,
                                                      num_clusters,
                                                      'cluster_assignment')
    matches, edges = get_matches.get_matches(test_data)
    G, clusters = network_graph.network_graph(test_people, edges, "circles",
                                              num_clusters)

    assert type(G) == networkx.classes.graph.Graph
    assert G.number_of_edges() == 671
    assert G.number_of_nodes() == 542
    assert len(clusters) == 542
