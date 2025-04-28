import numpy as np

def fft_polynomial_multiply(P, Q):
    """Multiply two polynomials P and Q using FFT (over integers, then round).
       Returns the full coefficient list (without modulo reduction)."""
    n = len(P) + len(Q) - 1
    size = 2 ** int(np.ceil(np.log2(n)))
    P_extended = np.pad(P, (0, size - len(P)), mode='constant')
    Q_extended = np.pad(Q, (0, size - len(Q)), mode='constant')
    P_fft = np.fft.fft(P_extended)
    Q_fft = np.fft.fft(Q_extended)
    C_fft = P_fft * Q_fft
    C = np.fft.ifft(C_fft)
    return np.round(C.real).astype(int)[:n]

def poly_mult_mod_fft(P, Q, r, n):
    """Multiply polynomials P and Q using FFT, then reduce modulo (x^r - 1)
       and reduce coefficients modulo n."""
    # Multiply using FFT (this returns a polynomial of degree len(P)+len(Q)-1)
    full_product = fft_polynomial_multiply(P, Q).tolist()
    # Fold the coefficients mod r (because x^r ≡ 1)
    result = [0] * r
    for i, coeff in enumerate(full_product):
        result[i % r] = (result[i % r] + coeff) % n
    return result
