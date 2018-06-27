Example Gallery
===============

test

.. altair-plot::

    from altair import *
    import pandas as pd
    data = pd.DataFrame({'a': list('CCCDDDEEE'),
                         'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

    Chart(data).mark_point().encode(
        x='a',
        y='b'
    )
