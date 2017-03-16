#import plotly
import plotly.plotly as py
from plotly.graph_objs import Scatter, Figure, XAxis, YAxis, Layout, \
     Data, Line, Marker


def generate_plotly(G, clusters):
    """ Generates a network graph using plotly

    Parameters
    ----------
    graph: networkx graph object
    clusters: dictionary of node:cluster assignments

    Returns
    -------
    plotly plot
    """

    edge_trace = Scatter(
        x=[],
        y=[],
        line=Line(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=True,
            colorscale='YIGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'),
            line=dict(width=2)))

    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)
        node_trace['marker']['color'].append(clusters[node])
        node_info = 'Cluster: '+str(clusters[node])
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                     title='<br>Network graph made with Python',
                     titlefont=dict(size=16),
                     showlegend=False,
                     width=650,
                     height=650,
                     hovermode='closest',
                     margin=dict(b=20, l=5, r=5, t=40),
                     annotations=[dict(
                         text="Python code:<a href='https://plot.ly/ipython-notebooks/network-graphs/'> 'https://plot.ly/ipython-notebooks/network-graphs/</a>",
                         showarrow=False,
                         xref="paper",
                         yref="paper",
                         x=0.005,
                         y=-0.002)],
                     xaxis=XAxis(showgrid=False, zeroline=False,
                                 showticklabels=False),
                     yaxis=YAxis(showgrid=False, zeroline=False,
                                 showticklabels=False)))

    return py.iplot(fig, filename='networkx')
