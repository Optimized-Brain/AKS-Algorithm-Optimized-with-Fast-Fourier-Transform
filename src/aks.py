from math import isqrt, gcd, log2
from src.poly import poly_mult_mod, poly_pow_mod, poly_xn, poly_add
from src.fft import poly_mult_mod_fft

def is_perfect_power(n):
    for b in range(2, int(log2(n)) + 2):
        a = int(round(n ** (1 / b)))
        if a ** b == n:
            return True
    return False

def find_smallest_r(n):
    max_k = log2(n) ** 2
    for r in range(2, n):
        all_good = True
        for k in range(1, int(max_k) + 1):
            if pow(n, k, r) == 0:
                break
            if pow(n, k, r) == 1 and k < r - 1:
                all_good = False
                break
        if all_good:
            return r
    return n

def normal_aks_primality_test(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if is_perfect_power(n):
        return False

    r = find_smallest_r(n)
    for a in range(1, r + 1):
        if 1 < gcd(a, n) < n:
            return False
    if n <= r:
        return True

    # Polynomial congruence test: Check if (x + a)^n ≡ x^n + a mod (n, x^r - 1)
    limit = isqrt(r) * int(log2(n))
    for a in range(1, limit + 1):
        # Compute (x + a)^n modulo (x^r - 1, n)
        poly_base = [a, 1]  # Represents a + x
        left = poly_pow_mod(poly_base, n, r, n)
        # Compute right-hand side: x^n + a mod (x^r - 1, n)
        right = poly_add(poly_xn(n, r), [a] + [0]*(r-1), n)
        if left != right:
            return False
    return True

def fft_aks_primality_test(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if is_perfect_power(n):
        return False

    r = find_smallest_r(n)
    for a in range(1, r + 1):
        if 1 < gcd(a, n) < n:
            return False
    if n <= r:
        return True

    limit = isqrt(r) * int(log2(n))
    for a in range(1, limit + 1):
        poly_base = [a, 1]  # Represents a + x
        # Use FFT-based polynomial exponentiation:
        left = poly_pow_mod_fft(poly_base, n, r, n)
        right = poly_add(poly_xn(n, r), [a] + [0]*(r-1), n)
        if left != right:
            return False
    return True

def poly_pow_mod_fft(P, exp, r, n):
    """Exponentiation using FFT-based multiplication."""
    result = [0] * r
    result[0] = 1
    base = P[:]
    while exp:
        if exp % 2 == 1:
            result = poly_mult_mod_fft(result, base, r, n)
        base = poly_mult_mod_fft(base, base, r, n)
        exp //= 2
    return result
