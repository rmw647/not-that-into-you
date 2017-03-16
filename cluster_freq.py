"""Functions for performing analysis on clusters."""

import pandas as pd
import matplotlib.pyplot as plt

def cluster_freq(clusters, matches):
    """Creates bar chart showing number of matches within clusters

    Parameters
    ----------
    cluster: dictionary with cluster (id, cluster_id)
    matches: list of matches (id, partner_id)

    Returns
    -------
    None
    """

    new = pd.DataFrame.from_dict(clusters, orient='index').reset_index()
    new.rename(columns={'index': 'iid', 0: 'cluster'}, inplace=True)
    together = pd.merge(new,matches,left_on=new.iid,right_on=matches.iid,
                        how='right')
    together2 = pd.merge(together,new,left_on=together.pid,right_on=new.iid,
                        how='left')
    together2 = together2.groupby(['iid_x', 'iid']).last()
    together2['same cluster'] = together2.cluster_x-together2.cluster_y
    together2[together2['same cluster'] != 0] = 'Different Clusters'
    together2[together2['same cluster'] == 0] = 'Same Cluster'
    together2['same cluster'].value_counts().plot(kind='bar')
    
    plt.show()


def get_cluster_size(data):
    num_clusters = len(data.cluster_assignment.unique())
    sizes = {}
    for num in range(num_clusters):
        sizes.setdefault('cluster'+str(num), len(data[data.cluster_assignment == num]))
    return sizes
