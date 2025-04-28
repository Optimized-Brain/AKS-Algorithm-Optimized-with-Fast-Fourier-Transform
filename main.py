import sys
import os
import time
from src.aks import normal_aks_primality_test, fft_aks_primality_test

def run_tests_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as f:
        lines = f.readlines()

    header = ("Number", "Normal AKS", "FFT AKS", "Normal Time (s)", "FFT Time (s)", "Improvement (%)")
    print("{:<10} {:<12} {:<10} {:<18} {:<14} {:<16}".format(*header))
    print("-" * 80)

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            n = int(line)
        except ValueError:
            print(f"Skipping non-numeric line: {line}")
            continue

        # Measure time for normal AKS test
        start_normal = time.perf_counter()
        res_normal = normal_aks_primality_test(n)
        end_normal = time.perf_counter()
        normal_time = end_normal - start_normal

        # Measure time for FFT-optimized AKS test
        start_fft = time.perf_counter()
        res_fft = fft_aks_primality_test(n)
        end_fft = time.perf_counter()
        fft_time = end_fft - start_fft

        # Calculate improvement percentage as the absolute value (always positive)
        improvement = abs((normal_time - fft_time) / normal_time * 100) if normal_time > 0 else 0

        print("{:<10} {:<12} {:<10} {:<18.6f} {:<14.6f} {:<16.2f}".format(
            n,
            "Prime" if res_normal else "Not Prime",
            "Prime" if res_fft else "Not Prime",
            normal_time,
            fft_time,
            improvement
        ))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    run_tests_from_file(input_file)
