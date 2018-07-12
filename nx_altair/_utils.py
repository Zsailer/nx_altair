import numpy as np
import pandas as pd

def is_arraylike(obj):
    """Return True if array-like (accepts lists, pandas.Series
    pandas.DataFrame, numpy.ndarray).
    """
    if isinstance(obj, list):
        return True
    elif isinstance(obj, np.ndarray):
        return True
    elif isinstance(obj, pd.Series):
        return True
    elif isinstance(obj, pd.DataFrame):
        return True
    return False


def despine(chart):
    """Despine altair chart.
    """
    chart = chart.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False)
    return chart
