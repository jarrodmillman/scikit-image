import numpy as np

cimport numpy as cnp

from .fast_exp cimport _fast_exp_floats
from .fused_numerics cimport np_floats

cnp.import_array()

def fast_exp(np_floats x):
    return _fast_exp_floats(x)
