from Euclid import extend_euclid


def calc_sig(p, q, alpha, d, h, ke, dbg=False):
    r = pow(alpha, ke, p) % q
    s = ((h+d*r) * extend_euclid(ke, q)) % q
    if dbg:
        print(f'r = (alpha^(k_e) mod p) mod q = ({alpha}^({ke}) mod {p}) mod {q} = {r}')
        print(f's = (h + d*r) * k_e^-1 mod q = ({h} + {d}*{r}) * {extend_euclid(ke, q)} mod {q} = {s}')
    return r, s


def verify_sig(p, q, alpha, beta, h, r, s, dbg=False):
    w = extend_euclid(s, q)
    u1 = (w * h) % q
    u2 = (w * r) % q
    v = ((alpha ** u1) * (beta ** u2) % p) % q
    if dbg:
        print(f'w = s^-1 mod q = {s}^-1 mod {q} = {w}')
        print(f'u1 = (w * h) mod q = ({w} * {h}) mod {q} = {u1}')
        print(f'u2 = (w * r) mod q = ({w} * {r}) mod {q} = {u2}')
        print(f'v = (alpha^u1 * beta^u2 mod p) mod q = ({alpha}^{u1} * {beta}^{u2} mod {p}) mod {q} = {v}')
        print(f'Signature {"" if v == (r % q) else "NOT "}verified!')
    return v == (r % q)


P, Q, ALPHA, D, H, KE, BETA = 59, 29, 3, 23, 21, 8, 45
R, S = calc_sig(P, Q, ALPHA, D, H, KE, True)
verify_sig(P, Q, ALPHA, BETA, H, R, S, True)
