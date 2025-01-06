import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from aks import normal_aks_primality_test, fft_aks_primality_test

def test_normal_aks():
    assert normal_aks_primality_test(2) == True
    assert normal_aks_primality_test(4) == False

def test_fft_aks():
    assert fft_aks_primality_test(2) == True
    assert fft_aks_primality_test(4) == False
