import numpy as np

def naive_polynomial_multiply(A, B):
    n, m = len(A), len(B)
    result = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    return result

def fft_polynomial_multiply(A, B):
    n = len(A) + len(B) - 1
    size = 2**np.ceil(np.log2(n)).astype(int)
    A_extended = np.pad(A, (0, size - len(A)), mode='constant')
    B_extended = np.pad(B, (0, size - len(B)), mode='constant')
    A_fft = np.fft.fft(A_extended)
    B_fft = np.fft.fft(B_extended)
    C_fft = A_fft * B_fft
    C = np.fft.ifft(C_fft)
    return np.round(C.real).astype(int)[:n]
