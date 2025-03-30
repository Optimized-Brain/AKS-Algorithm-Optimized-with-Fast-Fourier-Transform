# poly.py: Polynomial arithmetic modulo (x^r - 1) and coefficient modulus n.

def poly_mult_mod(P, Q, r, n):
    """Naive polynomial multiplication modulo (x^r - 1) and coefficients mod n.
       P and Q are lists of coefficients (lowest degree first).
       The result is a list of length r."""
    result = [0] * r
    for i, a in enumerate(P):
        for j, b in enumerate(Q):
            index = (i + j) % r  # because x^r ≡ 1 (mod x^r - 1)
            result[index] = (result[index] + a * b) % n
    return result

def poly_pow_mod(P, exp, r, n):
    """Exponentiation of polynomial P to power exp modulo (x^r - 1) and coefficient mod n."""
    # Initialize result as polynomial '1'
    result = [0] * r
    result[0] = 1
    base = P[:]
    while exp:
        if exp % 2 == 1:
            result = poly_mult_mod(result, base, r, n)
        base = poly_mult_mod(base, base, r, n)
        exp //= 2
    return result

def poly_xn(n, r):
    """Return polynomial representing x^(n mod r) with degree < r."""
    poly = [0] * r
    poly[n % r] = 1
    return poly

def poly_add(P, Q, n):
    """Add two polynomials coefficient-wise mod n (assumes same length)."""
    return [(a + b) % n for a, b in zip(P, Q)]
