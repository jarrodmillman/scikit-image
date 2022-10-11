__all__ = ['imread', 'imsave']

from functools import wraps

import numpy as np

try:
    # Try using the v2 API directly to avoid a warning from imageio >= 2.16.2
    from imageio.v2 import imread as imageio_imread
    from imageio.v2 import imsave
except ImportError:
    from imageio import imread as imageio_imread
    from imageio import imsave


@wraps(imageio_imread)
def imread(*args, **kwargs):
    return np.asarray(imageio_imread(*args, **kwargs))
