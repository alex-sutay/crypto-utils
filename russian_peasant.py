import math


def mod(x, poly='100011011'):
    """
    mod a polynomial by another polynomial
    :param x: the int representing the bitstring of the polynomial
    :param poly: the polynomial to mod by. Defaults to AES irreducible
    :return: the int representing the bitstring of the polynomial
    """
    poly = int(poly, 2)
    digits = math.floor(math.log2(x)) - math.floor(math.log2(poly))
    while digits >= 0:  # repeat for as long as the given poly is the same length or longer than the mod poly
        x = x ^ (poly << digits)  # multiply the polynomial by x to get to the highest power, xor by it
        digits = math.floor(math.log2(x)) - math.floor(math.log2(poly))
    return x


def _russian_peasant(a, b):
    """
    Uses the russian peasant algorithm for multiplying 2 numbers. Specifically, it's designed to multiply polynomials
    in a galois field. Uses the default mod poly, which is AES irreducible
    :param a: the number representing the first polynomial
    :param b: the number representing the second polynomial
    :return: the integer representing the bit string representing the result polynomial
    """
    if a == 1:
        return b  # base case once it's 1
    elif a % 2 == 0:
        return _russian_peasant(mod(a >> 1), mod(b << 1))  # multiply by 2, mod by P(x), don't add it if it's even
    else:
        return b ^ _russian_peasant(mod(a >> 1), mod(b << 1))  # divide by 2, mod by P(x), adding is the same as xor


def poly_multiply(a, b):
    """
    multiply 2 polynomials togethers, given 2 hex numbers representing the bit strings representing the polynomials
    :param a: str hex for the first polynomial
    :param b: str hex for the second polynomial
    :return: str hex of the result polynomial
    """
    return hex(_russian_peasant(int(a, 16), int(b, 16)))


def sum_hex(hexes):
    """
    Find the sum of hex numbers, given that addition is the same as xoring
    :param hexes: iterable of str hexes
    :return: str hex of total
    """
    total = 0
    for num in hexes:
        total = total ^ int(num, 16)
    return hex(total)
