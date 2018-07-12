.. nx_altair documentation master file, created by
   sphinx-quickstart on Fri Jun  8 15:11:20 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nx_altair
=========

.. altair-plot::
  :hide-code:

  import networkx as nx
  import altair as alt
  import nx_altair as nxa
  import numpy as np

  # Generate a random graph
  G = nx.fast_gnp_random_graph(n=20, p=0.25)

  # Compute positions for viz.
  pos = nx.spring_layout(G)

  chart = nxa.core.to_chart(G, pos)

  # Add weights
  for n in G.nodes():
      G.nodes[n]['weight'] = np.random.randn()
      G.nodes[n]['name'] = np.random.randint(1000)
      G.nodes[n]['z'] = 'hello'

  for e in G.edges():
      G.edges[(e[0],e[1])]['weight'] = np.random.uniform(1, 10)


  chart = nxa.core.to_chart(G, pos)
  nxa.draw_networkx_nodes(
      chart=chart,
      node_color='weight',
      cmap='viridis',
      tooltip=['weight', 'name', 'z']
  )

  nxa.draw_networkx_edges(
      chart=chart,
      width='weight',
      tooltip=['weight']
  )

  chart.interactive()

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
