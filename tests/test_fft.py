import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from fft import fft_polynomial_multiply, naive_polynomial_multiply

def test_fft_vs_naive():
    A = [1, 2, 3]
    B = [4, 5, 6]
    assert (fft_polynomial_multiply(A, B) == naive_polynomial_multiply(A, B)).all()
