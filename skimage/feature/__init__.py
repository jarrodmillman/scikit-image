from .._shared.utils import deprecated
from ._basic_features import multiscale_basic_features
from ._canny import canny
from ._cascade import Cascade
from ._daisy import daisy
from ._hog import hog
from .blob import blob_dog, blob_doh, blob_log
from .brief import BRIEF
from .censure import CENSURE
from .corner import (corner_fast, corner_foerstner, corner_harris,
                     corner_kitchen_rosenfeld, corner_moravec,
                     corner_orientations, corner_peaks, corner_shi_tomasi,
                     corner_subpix, hessian_matrix, hessian_matrix_det,
                     hessian_matrix_eigvals, shape_index, structure_tensor,
                     structure_tensor_eigenvalues)
from .haar import (draw_haar_like_feature, haar_like_feature,
                   haar_like_feature_coord)
from .match import match_descriptors
from .orb import ORB
from .peak import peak_local_max
from .sift import SIFT
from .template import match_template
from .texture import (draw_multiblock_lbp, graycomatrix, graycoprops,
                      local_binary_pattern, multiblock_lbp)
from .util import plot_matches


@deprecated(alt_func='skimage.feature.graycomatrix',
            removed_version='1.0')
def greycomatrix(image, distances, angles, levels=None, symmetric=False,
                 normed=False):
    return graycomatrix(image, distances, angles, levels, symmetric, normed)


@deprecated(alt_func='skimage.feature.graycoprops',
            removed_version='1.0')
def greycoprops(P, prop='contrast'):
    return graycoprops(P, prop)


__all__ = ['canny',
           'Cascade',
           'daisy',
           'hog',
           'graycomatrix',
           'graycoprops',
           'greycomatrix',
           'greycoprops',
           'local_binary_pattern',
           'multiblock_lbp',
           'draw_multiblock_lbp',
           'peak_local_max',
           'structure_tensor',
           'structure_tensor_eigenvalues',
           'hessian_matrix',
           'hessian_matrix_det',
           'hessian_matrix_eigvals',
           'shape_index',
           'corner_kitchen_rosenfeld',
           'corner_harris',
           'corner_shi_tomasi',
           'corner_foerstner',
           'corner_subpix',
           'corner_peaks',
           'corner_moravec',
           'corner_fast',
           'corner_orientations',
           'match_template',
           'BRIEF',
           'CENSURE',
           'ORB',
           'SIFT',
           'match_descriptors',
           'plot_matches',
           'blob_dog',
           'blob_doh',
           'blob_log',
           'haar_like_feature',
           'haar_like_feature_coord',
           'draw_haar_like_feature',
           'multiscale_basic_features',
           ]
