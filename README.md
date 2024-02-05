# crypto-utils
This is a repository for generic cryptography tools in python.
I feel like I'm regularly rewriting most of these in one way or another, so now I have them for easy access.

## Euclid.py
This is the file with euclidean algorithms.
The function `euclid` is the standard euclidean algorithm and finds the GCD of the two numbers passed to it.
The function `extended_euclid` is the extended euclidean algorithm and finds the multiplicative inverse of one or both numbers

## RSA.py
This file has basic RSA utilities, including checking for primality, generating primes, square and multiply for exponentiation,
a function to generate an RSA key, and a function to double check if an RSA key is valid. 

## modtabs.py
This is a neat little program to make modular arithmetic tables.
Think like a multiplication table, but it's all modulo a given value.
It can do addition tables, multiplication tables, and even expoenential tables.

## russian_peasant.py
This has some galois field polynomial functions.
I'm pretty sure there are libraries that do this better, but this was a quick little thing I wrote.
Used for simulating some internal AES functions.  

## LFSR.py
This file has some very basic LFSR functionality.
The `lfsr` function actually has a set of all of the possible values from an LFSR with given prefixes and starting point.
The point being to see if it was a complete set I believe.

## DSA.py
Basic implementation of the DSA algorithm.
Given all the variables, it will do the math to calculate or verify a signature.
It doesn't generate a key or do the hashing of a message, it's just the math.
