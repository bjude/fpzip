import pytest

import numpy as np
import fpzip

def test_doubles():

  x = np.random.random_sample(size=(128, 128, 128, 3)).astype(np.float64)
  y = fpzip.compress(x)
  z = fpzip.decompress(y)

  assert np.all(x == z)

  x = np.random.random_sample(size=(0, 0, 0, 0)).astype(np.float64)
  y = fpzip.compress(x)
  z = fpzip.decompress(y)

  assert np.all(x == z)  

def test_floats():
  x = np.random.random_sample(size=(128, 128, 128, 3)).astype(np.float32)
  y = fpzip.compress(x)
  z = fpzip.decompress(y)

  assert np.all(x == z)

  x = np.random.random_sample(size=(128, 128, 128)).astype(np.float32)
  y = fpzip.compress(x)
  z = fpzip.decompress(y)
  z = np.squeeze(z, axis=3)

  assert np.all(x == z)

  x = np.random.random_sample(size=(0, 0, 0, 0)).astype(np.float32)
  y = fpzip.compress(x)
  z = fpzip.decompress(y)

  assert np.all(x == z)
