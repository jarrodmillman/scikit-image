import warnings

from .footprints import (ball, cube, diamond, disk, octagon, octahedron,
                         rectangle, square, star)

warnings.warn(
    "The `skimage.morphology.selem` module is deprecated and will be removed "
    "in scikit-image 1.0 (`skimage.morphology.selem` has been moved to "
    "`skimage.morphology.footprints`).",
    FutureWarning, stacklevel=2
)
