def cluster_freq(cluster,matches):

    new = pd.DataFrame.from_dict(cluster, orient='index').reset_index()
    new.rename(columns={'index': 'iid', 0: 'cluster'}, inplace=True)
    together=pd.merge(new,matches,left_on=new.iid,right_on=matches.iid,how='right')
    together2=pd.merge(together,new,left_on=together.pid,right_on=new.iid,how='left')
    together2=together2.groupby(['iid_x', 'iid']).last()
    together2['same cluster']=together2.cluster_x-together2.cluster_y
    together2[together2['same cluster'] != 0] = 1
    together2['same cluster'].value_counts().plot( kind='bar')
    plt.show()
    
    
    