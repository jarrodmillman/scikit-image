import unittest
from tempfile import NamedTemporaryFile

import numpy as np
from pytest import fixture, importorskip, raises

from skimage._shared import testing
from skimage.io import imread, imsave, reset_plugins, use_plugin

importorskip('SimpleITK')

np.random.seed(0)


def teardown():
    reset_plugins()


@fixture(autouse=True)
def setup_plugin():
    """This ensures that `use_plugin` is directly called before all tests to
    ensure that SimpleITK is used.
    """
    use_plugin('simpleitk')
    yield


def test_imread_as_gray():
    img = imread(testing.fetch('data/color.png'), as_gray=True)
    assert img.ndim == 2
    assert img.dtype == np.float64
    img = imread(testing.fetch('data/camera.png'), as_gray=True)
    # check that conversion does not happen for a gray image
    assert np.sctype2char(img.dtype) in np.typecodes['AllInteger']


def test_bilevel():
    expected = np.zeros((10, 10))
    expected[::2] = 255

    img = imread(testing.fetch('data/checker_bilevel.png'))
    np.testing.assert_array_equal(img, expected)


def test_imread_truncated_jpg():
    with raises(RuntimeError):
        imread(testing.fetch('data/truncated.jpg'))


def test_imread_uint16():
    expected = np.load(testing.fetch('data/chessboard_GRAY_U8.npy'))
    img = imread(testing.fetch('data/chessboard_GRAY_U16.tif'))
    assert np.issubdtype(img.dtype, np.uint16)
    np.testing.assert_array_almost_equal(img, expected)


def test_imread_uint16_big_endian():
    expected = np.load(testing.fetch('data/chessboard_GRAY_U8.npy'))
    img = imread(testing.fetch('data/chessboard_GRAY_U16B.tif'))
    np.testing.assert_array_almost_equal(img, expected)


class TestSave(unittest.TestCase):
    def roundtrip(self, dtype, x):
        with NamedTemporaryFile(suffix='.mha') as f:
            fname = f.name

        imsave(fname, x)
        y = imread(fname)

        np.testing.assert_array_almost_equal(x, y)

    def test_imsave_roundtrip(self):
        for shape in [(10, 10), (10, 10, 3), (10, 10, 4)]:
            for dtype in (np.uint8, np.uint16, np.float32, np.float64):
                x = np.ones(shape, dtype=dtype) * np.random.rand(*shape)

                if np.issubdtype(dtype, np.floating):
                    yield self.roundtrip, dtype, x
                else:
                    x = (x * 255).astype(dtype)
                    yield self.roundtrip, dtype, x
