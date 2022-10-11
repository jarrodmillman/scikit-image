"""Image restoration module.

"""

from ._cycle_spin import cycle_spin
from ._denoise import (denoise_bilateral, denoise_tv_bregman,
                       denoise_tv_chambolle, denoise_wavelet, estimate_sigma)
from .deconvolution import richardson_lucy, unsupervised_wiener, wiener
from .inpaint import inpaint_biharmonic
from .j_invariant import calibrate_denoiser
from .non_local_means import denoise_nl_means
from .rolling_ball import ball_kernel, ellipsoid_kernel, rolling_ball
from .unwrap import unwrap_phase

__all__ = ['wiener',
           'unsupervised_wiener',
           'richardson_lucy',
           'unwrap_phase',
           'denoise_tv_bregman',
           'denoise_tv_chambolle',
           'denoise_bilateral',
           'denoise_wavelet',
           'denoise_nl_means',
           'estimate_sigma',
           'inpaint_biharmonic',
           'cycle_spin',
           'calibrate_denoiser',
           'rolling_ball',
           'ellipsoid_kernel',
           'ball_kernel',
           ]
