import random
from Euclid import extend_euclid


def square_and_multiply(base, power, mod):
    bits = bin(power)
    val = 1
    for bit in bits:
        val = val**2 % mod
        if bit == '1':
            val = val * base % mod
    return val


def is_likely_prime(p, s=10):
    for _ in range(s):
        a = random.randint(2, p-2)
        if square_and_multiply(a, p-1, p) != 1:
            return False
    return True


def get_random_prime(mn, mx, s=10):
    i = 0
    while True:
        n = random.randint(mn, mx)
        if is_likely_prime(n, s):
            return n
        if i := i + 1 > 1000000:
            raise ValueError("Failed to generate withing range!")


def make_rsa_key(p_bits):
    p = get_random_prime(1 << p_bits, 1 << (p_bits+1))
    q = get_random_prime(1 << p_bits, 1 << (p_bits+1))
    n = p * q
    phi = (p-1) * (q-1)
    e = get_random_prime(1000, 10000)
    d = extend_euclid(e, phi)
    if check_rsa(e, d, n, p, q) != 'Passed!':
        print(f'Failed with: e: {e}, d: {d}, n: {n}, p: {p}, q: {q}')
        raise ValueError(check_rsa(e, d, n, p, q))
    return e, d, n, p, q


def check_rsa(e, d, n, p=None, q=None):
    if p is not None and q is not None:
        if n != p*q:
            return "Failed! n != p*q"
        if (e*d) % ((p-1) * (q-1)) != 1:
            return "Failed! e and d are not inverses"
    else:
        print('Skipping inverse check')
    if pow(pow(1337, e, n), d, n) != 1337:
        return "Failed! The encrypt/decrypt did not work"
    return 'Passed!'


