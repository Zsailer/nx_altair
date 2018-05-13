# Networkx in Altair

*Draw NetworkX graphs with Altair*

This library is still under heavy maintenance! I'm currently working on adding
all the functionality in NetworkX's draw functions. Stay tuned.

```python
import networkx as nx
import nx_altair as nxa

# Generate a random graph
G = nx.fast_gnp_random_graph(n=20, p=0.25)

# Compute positions for viz.
pos = nx.spring_layout(G)

# Draw the graph using Altair
viz = nxa.draw(G, pos=pos)

# Show it as an interactive plot!
viz.interactive()
```

![Altair networkx](docs/_img/readme.png)
