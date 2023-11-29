
def euclid(a, b):
    (a, b) = (b, a) if b > a else (a, b)
    return b if a % b == 0 else euclid(b, a % b)


def _extend_euclid_rec(a, b):
    if a == 1 and b == 0:
        return 1, 0
    x_p, y_p = _extend_euclid_rec(b, a % b)  # a % b = r
    x = y_p
    y = x_p - y_p * (a // b)  # a // b = q
    return x, y


def extend_euclid(a, b, both=False, dbg=False):
    """
    Find the multiplicative inverses using the extended euclidean algorithm
    :param a:
    :param b:
    :param both: return both inverses instead of just a % b
    :param dbg:
    :return:
    """
    if b > a:
        y, x = _extend_euclid_rec(b, a)
    else:
        x, y = _extend_euclid_rec(a, b)
    x = x + b if x < 0 else x
    y = y + a if y < 0 else y
    if dbg:
        print(f'{a}^-1 mod {b} ≡ {x if x >=0 else x + b}\n'
              f'{b}^-1 mod {a} ≡ {y if y >=0 else y + a}')
    return (x, y) if both else x
