from math import isqrt, gcd, log2
from fft import naive_polynomial_multiply, fft_polynomial_multiply

def is_perfect_power(n):
    for b in range(2, int(log2(n)) + 2):
        a = int(round(n**(1/b)))
        if a**b == n:
            return True
    return False

def find_smallest_r(n):
    max_k = log2(n)**2
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

    limit = isqrt(r) * int(log2(n))
    for a in range(1, limit + 1):
        left = naive_polynomial_multiply([a + n], [n])
        right = naive_polynomial_multiply([a], [n])
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
        left = fft_polynomial_multiply([a + n], [n])
        right = fft_polynomial_multiply([a], [n])
        if left != right:
            return False

    return True
