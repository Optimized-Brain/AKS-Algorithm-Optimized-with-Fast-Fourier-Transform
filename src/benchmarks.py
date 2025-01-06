import time
from aks import normal_aks_primality_test, fft_aks_primality_test


# Benchmarking Function with higher precision time
def benchmark_aks(ns):
    
    print(f"{'Input':>10} | {'Normal AKS Time (s)':>20} | {'FFT AKS Time (s)':>20} | {'Improvement (%)':>20}")
    print("-" * 72)
    for n in ns:
        start_normal = time.perf_counter()
        normal_aks_primality_test(n)
        end_normal = time.perf_counter()

        start_fft = time.perf_counter()
        fft_aks_primality_test(n)
        end_fft = time.perf_counter()

        normal_time = end_normal - start_normal
        fft_time = end_fft - start_fft

        # Avoid division by zero in case of extremely fast tests
        improvement = 100 * (normal_time - fft_time) / normal_time if normal_time > 0 else 0

        print(f"{n:>10} | {normal_time:>20.6f} | {fft_time:>20.6f} | {improvement:>20.2f}%")
