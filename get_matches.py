def get_matches(data):
    """Takes dataframe and generates list of edges for people who matched.

    Parameters
    ----------
    data: DataFrame with data. Should have the following columns:
        - iid- ID or participant
        - pid- partner ID
        - match- column indicating whether they matched

    Returns
    -------
    matched_data: Dataframe with entries only for participants who matched_data
    edges: A list of (id, partner_id) for people who matched. Note this list
           likely has reciprocals i.e. (id, partner_id), (partner_id, id).
    """

    if all(x in data.columns for x in ['iid', 'pid', 'match']):
        data_subset = data.drop_duplicates(subset='iid')
        matches = data[['iid','pid','match']]
        matches = matches[matches.match==1]
        matches['pid'] = matches['pid'].astype(int)
        matches = matches[matches.iid.isin(data_subset.iid)&
                          matches.pid.isin(data_subset.iid)]
        edges = list(zip(matches.iid, matches.pid))
        return matches, edges
    else:
        raise NameError("Columns 'iid', 'pid', and 'match' not found in data")
