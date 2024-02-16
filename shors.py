import random
from math import gcd
from time import time


def shors(n, dbg=False):
    if dbg:
        t = time()
        print(f'Finding the factors of {n}\t\t| t={time()-t}')
    while True:
        # pick a random x < n
        x = random.randint(1, n-1)
        if dbg:
            print(f'Picked random number {x}\t\t| t={time()-t}')
        # compute GCD
        d = gcd(x, n)
        # if GCD isn't 1, we win, we got incredibly lucky
        if d != 1:
            if dbg:
                print(f'We got a gcd={d} with x={x} and n={n}; the factors should be ({d}, {n//d})\t\t| t={time()-t}')
            return d, n // d
        # find s = period of x**r (not efficient classically)
        s = 2
        while pow(x, s, n) != x:
            s += 1
        s -= 1  # We are counting both the first and last, remove the last
        if dbg:
            print(f'Found the period to be {s}\t\t| t={time()-t}')
        # if s is odd, we're sad :(
        if s & 1 == 1:
            if dbg:
                print('The period is odd, we are sad :(')
            continue
        # calc (x**(s//2)+1) and (x**(s//2)-1), gcd them with n, hope they're not trivial
        factor1 = pow(x, (s >> 1))+1
        if dbg:
            print(f'Exponentiation of first factor\t\t| t={time()-t}')
        factor1 = gcd(factor1, n)
        if dbg:
            print(f'GCD of first factor\t\t\t\t\t| t={time()-t}')
        factor2 = pow(x, (s >> 1))-1
        if dbg:
            print(f'Exponentiation of second factor\t\t| t={time()-t}')
        factor2 = gcd(factor2, n)
        if dbg:
            print(f'GCD of second factor\t\t\t\t| t={time()-t}')
        factors = factor1, factor2
        # factors = gcd(pow(x, (s//2))+1, n), gcd(pow(x, (s//2))-1, n)
        if dbg:
            print(f'The factors should be: {factors}\t| t={time()-t}')
        if 1 in factors:
            if dbg:
                print("Whoopsies, that's a trivial solution. try again...")
            continue
        return factors


def hw_shors(n):
    print(f'Finding the factors of {n}\t\t')
    vals = {'rel_prime': [], 'not_rel_prime': [], 'orders': dict()}
    for x in range(1, n):
        # compute GCD
        d = gcd(x, n)
        # if GCD isn't 1, not relatively prime
        if d != 1:
            vals['not_rel_prime'].append(x)
            continue
            # return d, n // d
        vals['rel_prime'].append(x)
        # find s = period of x**r (not efficient classically)
        s = 2
        while pow(x, s, n) != x:
            s += 1
        s -= 1  # We are counting both the first and last, remove the last
        # the orders is a dict of orders to x values that got them
        vals['orders'][s] = vals['orders'].get(s, []) + [x]
    print(len(vals['rel_prime']), vals)
    for s in vals['orders']:
        print(f'There are {len(vals["orders"][s])} values with order {s}')
        if s & 1 == 1:
            continue
        for x in vals['orders'][s]:
            print(f'Calculating factors from order {s} with val {x}')
            # calc (x**(s//2)+1) and (x**(s//2)-1), gcd them with n, hope they're not trivial
            factor1 = pow(x, (s >> 1))+1
            # factor1 = gcd(factor1, n)
            factor2 = pow(x, (s >> 1))-1
            # factor2 = gcd(factor2, n)
            factors = gcd(factor1, n), gcd(factor2, n)
            # factors = gcd(pow(x, (s//2))+1, n), gcd(pow(x, (s//2))-1, n)
            print(f'\tThe factors are {factor1, factor2}')
            if 1 not in factors:
                break


def main():
    from RSA import get_random_prime

    (p, q) = (get_random_prime(5000, 10000), get_random_prime(5000, 10000))
    print(f'p={p}; q={q}')
    shors(p*q, True)


if __name__ == '__main__':
    # main()
    hw_shors(143)
