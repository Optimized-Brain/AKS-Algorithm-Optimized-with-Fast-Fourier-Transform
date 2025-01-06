import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import benchmark_aks from benchmarks
from benchmarks import benchmark_aks

if __name__ == "__main__":
    ns = [1000, 2000, 5000, 10000, 20000] 
    benchmark_aks(ns)
