#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
Simple Python module for the time analysis of different possible 
approaches to primes list computation
"""

import timeit


# Approach 1: worst possible algorithm
# Algorithm time complexity: O(n^2)

def list_primes_bad(n):
    n = int(n)  # in case some float slips in
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False

                # break............# intentionally not breaking the loop

        if isPrime:
            primes.append(i)
    return primes


# ------------------------------------

# Approach 2: Better but still naive algorithm
# Algorithm time complexity: O(n * sqrt(n))

def is_prime(n):
    if n <= 1:
        return False
    if (n == 2) | (n == 3):  # simple case
        return True
    if n % 2 == 0:  # if n is even
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def list_primes_naive(n):
    n = int(n)  # in case some float slips in
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


# ------------------------------------

# Approach 3: Sieve of Eratosthenes
# Algorithm time complexity: O(n * log(log(n)))

def list_primes_up_to(n):
    n = int(n)
    primes = []
    sieve = [True] * (n + 1)  # boolean vector of length n
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False  # flag all multiples of i as non primes
    return primes


# ------------------------------------

# Other functions:

def list_primes_from_to(i, j):
    primes = []
    i = int(i)
    j = int(j)
    if j - i < 10000:  # if the interval is small enough use naive approach
        for n in range(i, j + 1):
            if is_prime(n):
                primes.append(n)
    else:
        all_primes = list_primes_up_to(j)
        index = next(y for (y, x) in enumerate(all_primes) if i - 1 < x)
        primes = all_primes[index:]
    return primes


# ------------------------------------

# Approach 1: Bad approach

print ('Bad approach takes ',
       round(timeit.timeit('list_primes_bad(10000)', globals=globals(),
       number=1), 4), ' seconds.')

# Approach 2: Naive approach

print ('Naive approach takes ',
       round(timeit.timeit('list_primes_naive(10000)',
       globals=globals(), number=1), 4), ' seconds.')

# Approach 3: Sieve algorithm

print ('Sieve algorithm takes ',
       round(timeit.timeit('list_primes_up_to(10000)',
       globals=globals(), number=1), 4), ' seconds.')
