#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
Simple Python module for the time analysis of different possible 
approaches to primes list computation
"""

import timeit
import matplotlib.pyplot as plt


# Approach 1: bad algorithm
# Algorithm time complexity: O(n^2)

def primes_bad(n):
    n = int(n)  # in case some float slips in
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break  # don't break the loop for even worse efficiency
        if isPrime:
            primes.append(i)
    return primes


# ------------------------------------

# Approach 2: Better but still naive algorithm
# Algorithm time complexity: O(n * sqrt(n))

def is_prime(n):
    if n <= 1:
        return False
    if (n == 2) | (n == 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_naive(n):
    n = int(n)  # in case some float slips in
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


# ------------------------------------

# Approach 3: Sieve of Eratosthenes
# Algorithm time complexity: O(sqrt(n) * log log n)))

def primes_sieve_eratosthenes(n):
    n = int(n)
    sieve = [True] * (n + 1)  # boolean vector of length n
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False  # flag all multiples of i as non primes
    return [i for (i, p) in enumerate(sieve) if p & (i > 1)]


# ------------------------------------

# Approach 4: Sieve of Atkin
# Theoretical algorithm time complexity: O(n / (log log n)), but really
# depends on the implementation.

def primes_sieve_atkin(n):
    n = int(n)
    sieve = [False] * (n + 1)

    x = 1
    while x * x < n:
        y = 1
        while y * y < n:
            temp = 4 * x * x + y * y
            if (temp <= n) & (temp % 60 in [1, 13, 17, 29, 37, 41, 49, 53]):
                sieve[temp] = not sieve[temp]
            temp = 3 * x * x + y * y
            if (temp <= n) & (temp % 60 in [7, 19, 31, 43]):
                sieve[temp] = not sieve[temp]
            if x > y:
                temp = 3 * x * x - y * y
                if (temp <= n) & (temp % 60 in [11, 23, 47, 59]):
                    sieve[temp] = not sieve[temp]
            y += 1
        x += 1

    for i in range(5, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i * i):
                sieve[j] = False

    return [2, 3, 5] + [i for (i, p) in enumerate(sieve) if p]


# ------------------------------------

# Other functions:

def primes_from_to(i, j):
    primes = []
    i = int(i)
    j = int(j)
    if j - i < 10000:  # if the interval is small enough use naive approach
        for n in range(i, j + 1):
            if is_prime(n):
                primes.append(n)
    else:
        all_primes = primes_sieve_eratosthenes(j)
        index = next(y for (y, x) in enumerate(all_primes) if i - 1 < x)
        primes = all_primes[index:]
    return primes


# ------------------------------------

for i in range(5, 100):
    assert primes_bad(i) == primes_naive(i)
    assert primes_naive(i) == primes_sieve_eratosthenes(i)
    assert primes_sieve_eratosthenes(i) == primes_sieve_atkin(i)

# Approach 1: Bad approach
print ('Bad approach takes ', round(timeit.timeit('primes_bad(10000)',
       globals=globals(), number=1), 4), ' seconds.')

# Approach 2: Naive approach
print ('Naive approach takes ',
       round(timeit.timeit('primes_naive(10000)', globals=globals(),
       number=1), 4), ' seconds.')

# Approach 3: Eratosthenes sieve algorithm
print ('Eratosthenes sieve algorithm takes ',
       round(timeit.timeit('primes_sieve_eratosthenes(10000)',
       globals=globals(), number=1), 4), ' seconds.')

# Approach 4: Atkin sieve algorithm
print ('Atkin sieve algorithm takes ',
       round(timeit.timeit('primes_sieve_atkin(10000)',
       globals=globals(), number=1), 4), ' seconds.')

# ------------------------------------

time_bad = []
time_naive = []
time_hera = []
time_atkin = []
range_ = range(1000, 11000, 1000)

for c in range_:
    str_ = 'primes_bad(' + str(c) + ')'
    time_bad.append(timeit.timeit(str_, globals=globals(), number=1))

    str_ = 'primes_naive(' + str(c) + ')'
    time_naive.append(timeit.timeit(str_, globals=globals(), number=1))

    str_ = 'primes_sieve_eratosthenes(' + str(c) + ')'
    time_hera.append(timeit.timeit(str_, globals=globals(), number=1))

    str_ = 'primes_sieve_atkin(' + str(c) + ')'
    time_atkin.append(timeit.timeit(str_, globals=globals(), number=1))

plt.figure(0)
plt.plot(range_, time_bad, 'b-s', label='Bad')
plt.plot(range_, time_naive, 'g-^', label='Naive')
plt.plot(range_, time_hera, 'r-o', label='Heratosthenes')
plt.plot(range_, time_atkin, 'k-*', label='Atkin')
plt.ylabel('Execution time')
plt.xlabel('n')
plt.legend(loc='upper left')
plt.show()

# ------------------------------------

time_naive = []
time_hera = []
time_atkin = []
range_ = range(5000, 105000, 5000)

for c in range_:

    str_ = 'primes_naive(' + str(c) + ')'
    time_naive.append(timeit.timeit(str_, globals=globals(), number=1))

    str_ = 'primes_sieve_eratosthenes(' + str(c) + ')'
    time_hera.append(timeit.timeit(str_, globals=globals(), number=1))

    str_ = 'primes_sieve_atkin(' + str(c) + ')'
    time_atkin.append(timeit.timeit(str_, globals=globals(), number=1))

plt.figure(1)
plt.plot(range_, time_naive, 'g-^', label='Naive')
plt.plot(range_, time_hera, 'r-o', label='Heratosthenes')
plt.plot(range_, time_atkin, 'k-*', label='Atkin')
plt.ylabel('Execution time')
plt.xlabel('n')
plt.legend(loc='upper left')
plt.show()
