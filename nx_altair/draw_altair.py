import altair as alt

from .core import to_pandas_edges, to_pandas_nodes

def draw_networkx_edges(G, pos):
    # Pandas dataframe of edges
    df_edges = to_pandas_edges(G, pos)

    # Draw edges
    viz  = alt.Chart(df_edges).mark_line(
        color='black',
        opacity=1
    ).encode(
        alt.X('x', axis=alt.Axis(title='')),
        alt.Y('y', axis=alt.Axis(title='')),
        detail='edge'
    )

    viz.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False,
    )
    return viz

def draw_networkx_nodes(G, pos):
    # Pandas dataframe of nodes
    df_nodes = to_pandas_nodes(G, pos)

    viz = alt.Chart(df_nodes).mark_point(
        size=600,
        opacity=1,
        fill='red',
        color='black'
    ).encode(
        x='x',
        y='y',
    )

    viz.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False,
    )
    return viz

def draw(G, pos):
    """Draw networkx graph using Altair.
    """
    # Plot the nodes

    edges = draw_networkx_edges(G, pos)
    nodes = draw_networkx_nodes(G, pos)

    viz = edges + nodes

    viz = viz.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False,
    )
    return viz
