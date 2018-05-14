import numpy as np
import altair as alt

from .core import to_pandas_edges, to_pandas_nodes
from ._utils import is_arraylike

def draw_networkx_edges(
    G,
    pos,
    edgelist=None,
    width=1,
    alpha=1.0,
    edge_color='black',
    edge_cmap=None):
    """Draw the edges of the graph G.

    This draws only the edges of the graph G.

    Parameters
    ----------
    G : graph
       A networkx graph

    pos : dictionary
       A dictionary with nodes as keys and positions as values.
       Positions should be sequences of length 2.

    edgelist : collection of edge tuples
       Draw only specified edges(default=G.edges())

    width : float, or array of floats
       Line width of edges (default=1.0)

    edge_color : color string, or array of floats
       Edge color. Can be a single color format string (default='r'),
       or a sequence of colors with the same length as edgelist.
       If numeric values are specified they will be mapped to
       colors using the edge_cmap and edge_vmin,edge_vmax parameters.

    alpha : float
       The edge transparency (default=1.0)

    edge_cmap : Matplotlib colormap
       Colormap for mapping intensities of edges (default=None)

    Returns
    -------
    viz: ``altair.Chart`` object
    """

    # Pandas dataframe of edges
    df_edges = to_pandas_edges(G, pos)

    marker_attrs = {}
    encoded_attrs = {}

    # ---------- Handle arguments ------------

    ###### node list argument
    if isinstance(edgelist, list):
        # Subset dataframe.
        df_edges = df_edges.loc[df['pair'].isin(edgelist)]

    elif edgelist is not None:
        raise Exception("nodelist must be a list or None.")


    ###### Node size
    if isinstance(width, str):
        encoded_attrs["size"] = width

    elif isinstance(width, float) or isinstance(width, int):
        marker_attrs["strokeWidth"] = width

    else:
        raise Exception("width must be a string or int.")

    ###### node_color
    if not isinstance(edge_color, str):
        raise Exception("edge_color must be a string.")

    elif edge_color in df_edges.columns:
        encoded_attrs["color"] = edge_color

    else:
        marker_attrs["color"] = edge_color

    ##### alpha
    if isinstance(alpha, str):
        encoded_attrs["opacity"] = alpha

    elif isinstance(alpha, int) or isinstance(alpha, float):
        marker_attrs["opacity"] = alpha

    elif alpha is not None:
        raise Exception("alpha must be a string or None.")

    ##### alpha
    if isinstance(edge_cmap, str):
        encoded_attrs["color"] = alt.Color(
            edge_color,
            scale=alt.Scale(scheme=edge_cmap))

    elif edge_cmap is not None:
        raise Exception("edge_cmap must be a string (colormap name) or None.")


    # ---------- Construct visualization ------------


    # Draw edges
    viz  = alt.Chart(df_edges).mark_line(
        **marker_attrs
    ).encode(
        alt.X('x', axis=alt.Axis(title='')),
        alt.Y('y', axis=alt.Axis(title='')),
        detail='edge',
        **encoded_attrs
    )

    return viz

def draw_networkx_nodes(
    G,
    pos,
    nodelist=None,
    node_size=300,
    node_color='red',
    alpha=1,
    cmap=None,
    ):
    """Draw the nodes of the graph G.

    This draws only the nodes of the graph G.

    Parameters
    ----------
    G : graph
       A networkx graph

    pos : dictionary
       A dictionary with nodes as keys and positions as values.
       Positions should be sequences of length 2.

    nodelist : list, optional
       Draw only specified nodes (default G.nodes())

    node_size : scalar or string
       Size of nodes (default=300).  If an array is specified it must be the
       same length as nodelist.

    node_color : color string, or array of floats
       Node color. Can be a single color format string (default='r'),
       or a  sequence of colors with the same length as nodelist.
       If numeric values are specified they will be mapped to
       colors using the cmap and vmin,vmax parameters.  See
       matplotlib.scatter for more details.

    node_shape :  string
       The shape of the node.  Specification is as matplotlib.scatter
       marker, one of 'so^>v<dph8' (default='o').

    alpha : float or array of floats
       The node transparency.  This can be a single alpha value (default=1.0),
       in which case it will be applied to all the nodes of color. Otherwise,
       if it is an array, the elements of alpha will be applied to the colors
       in order (cycling through alpha multiple times if necessary).

    cmap : Matplotlib colormap
       Colormap for mapping intensities of nodes (default=None)

    Returns
    -------
    viz: ``altair.Chart`` object
    """
    # Pandas dataframe of nodes
    df_nodes = to_pandas_nodes(G, pos)

    marker_attrs = {}
    encoded_attrs = {}

    # ---------- Handle arguments ------------

    ###### node list argument
    if isinstance(nodelist, list):
        # Subset dataframe.
        df_nodes = df_nodes.loc[nodelist]

    elif nodelist is not None:
        raise Exception("nodelist must be a list or None.")


    ###### Node size
    if isinstance(node_size, str):
        encoded_attrs["size"] = node_size

    elif isinstance(node_size, int):
        marker_attrs["size"] = node_size

    else:
        raise Exception("node_size must be a string or int.")

    ###### node_color
    if not isinstance(node_color, str):
       raise Exception("node_color must be a string.")

    if node_color in df_nodes.columns:
        encoded_attrs["fill"] = node_color

    else:
        marker_attrs["fill"] = node_color

    ##### alpha
    if isinstance(alpha, str):
        encoded_attrs["opacity"] = alpha

    elif isinstance(alpha, int) or isinstance(alpha, float):
        marker_attrs["opacity"] = alpha

    elif alpha is not None:
        raise Exception("alpha must be a string or None.")

    ##### alpha
    if isinstance(cmap, str):
        encoded_attrs["fill"] = alt.Color(
            node_color,
            scale=alt.Scale(scheme=cmap))

    elif cmap is not None:
        raise Exception("cmap must be a string (colormap name) or None.")


    # ---------- Construct visualization ------------

    viz = alt.Chart(df_nodes).mark_point(
        **marker_attrs
    ).encode(
        x='x',
        y='y',
        **encoded_attrs
    )

    return viz

def draw_networkx(
    G,
    pos=None,
    nodelist=None,
    edgelist=None,
    node_size=300,
    node_color='red',
    alpha=1,
    cmap=None,
    width=1,
    edge_color='black',
    edge_cmap=None):
    """Draw the graph G using Altair.

    nodelist : list, optional (default G.nodes())
       Draw only specified nodes

    edgelist : list, optional (default=G.edges())
       Draw only specified edges

    node_size : scalar or array, optional (default=300)
       Size of nodes.  If an array is specified it must be the
       same length as nodelist.

    node_color : color string, or array of floats, (default='r')
       Node color. Can be a single color format string,
       or a  sequence of colors with the same length as nodelist.
       If numeric values are specified they will be mapped to
       colors using the cmap and vmin,vmax parameters.  See
       matplotlib.scatter for more details.

    alpha : float, optional (default=1.0)
       The node and edge transparency

    cmap : Matplotlib colormap, optional (default=None)
       Colormap for mapping intensities of nodes

    width : float, optional (default=1.0)
       Line width of edges

    edge_color : color string, or array of floats (default='r')
       Edge color. Can be a single color format string,
       or a sequence of colors with the same length as edgelist.
       If numeric values are specified they will be mapped to
       colors using the edge_cmap and edge_vmin,edge_vmax parameters.

    edge_cmap : Matplotlib colormap, optional (default=None)
       Colormap for mapping intensities of edges
    """
    # Draw edges
    edges = draw_networkx_edges(
        G,
        pos,
        edgelist=edgelist,
        alpha=alpha,
        width=width,
        edge_color=edge_color,
        edge_cmap=edge_cmap)

    # Draw nodes
    nodes = draw_networkx_nodes(
        G,
        pos,
        nodelist=nodelist,
        node_size=node_size,
        node_color=node_color,
        alpha=alpha,
        cmap=cmap)

    # Layer the chart
    viz = edges + nodes

    # Remove ticks, axis, labels, etc.
    viz = viz.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False,
    )
    return viz
