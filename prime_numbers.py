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

# Efficient code downloaded from https://web.archive.org/web/20071011180805/http://krenzel.info/static/atkin.py

from math import sqrt, ceil, floor, log

def sieveOfAtkin(end):
    end += 1
    lng = int((end/2)-1+end%2)
    sieve = [False]*(lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max**2, (y_max << 1) - 1
        if n%2 == 0:
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n%12
            if (m == 1 or m == 5):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n -= d
                
    x_max, x2, xd = int(sqrt((end-1)/3.0)), 0, 3
    for xd in range(3, 6*x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max**2, (y_max << 1) - 1
        if n%2 == 0:
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if (n%12 == 7):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n -= d
                
    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x**2 + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if (n%12 == 11):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n += d

    primes = [2,3]
    if end <= 3 : return primes[:max(0,end-2)]
    
    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            for k in range(((n << 1) + 1)**2, end, 2*((n << 1) + 1)**2):
                sieve[k >> 1] = False

    s  = int(sqrt(end)) + 1
    if s%2 == 0: s += 1
    primes.extend([ i for i in range(s, end, 2) if sieve[i >> 1]])
    
    return primes

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
    assert primes_sieve_atkin(i) == sieveOfAtkin(i)


# Approach 1: Bad approach
print ('Bad approach takes ', round(timeit.timeit('primes_bad(10000)',
       globals=globals(), number=5), 4), ' seconds.')

# Approach 2: Naive approach
print ('Naive approach takes ',
       round(timeit.timeit('primes_naive(10000)', globals=globals(),
       number=5), 4), ' seconds.')

# Approach 3: Eratosthenes sieve algorithm
print ('Eratosthenes sieve algorithm takes ',
       round(timeit.timeit('primes_sieve_eratosthenes(10000)',
       globals=globals(), number=5), 4), ' seconds.')

# Approach 4: Atkin sieve algorithm
print ('My Atkin sieve algorithm takes ',
       round(timeit.timeit('primes_sieve_atkin(10000)',
       globals=globals(), number=5), 4), ' seconds.')

print ('Efficient Atkin sieve algorithm takes ',
       round(timeit.timeit('sieveOfAtkin(10000)',
       globals=globals(), number=5), 4), ' seconds.')
       
# ------------------------------------

time_bad = []
time_naive = []
time_hera = []
time_atkin = []
range_ = range(1000, 11000, 1000)

for c in range_:
    str_ = 'primes_bad(' + str(c) + ')'
    time_bad.append(timeit.timeit(str_, globals=globals(), number=5))

    str_ = 'primes_naive(' + str(c) + ')'
    time_naive.append(timeit.timeit(str_, globals=globals(), number=5))

    str_ = 'primes_sieve_eratosthenes(' + str(c) + ')'
    time_hera.append(timeit.timeit(str_, globals=globals(), number=5))

    str_ = 'primes_sieve_atkin(' + str(c) + ')'
    time_atkin.append(timeit.timeit(str_, globals=globals(), number=5))

plt.figure(0)
plt.plot(range_, time_bad, 'b-s', label='Bad')
plt.plot(range_, time_naive, 'g-^', label='Naive')
plt.plot(range_, time_atkin, 'k-*', label='My Atkin')
plt.plot(range_, time_hera, 'r-o', label='Heratosthenes')

plt.ylabel('Execution time')
plt.xlabel('n')
plt.legend(loc='upper left')
plt.show()

# ------------------------------------

time_naive = []
time_hera = []
time_atkin = []
time_atkin2 = []
range_ = range(5000, 105000, 5000)

for c in range_:
    str_ = 'primes_naive(' + str(c) + ')'
    time_naive.append(timeit.timeit(str_, globals=globals(), number=5))

    str_ = 'primes_sieve_eratosthenes(' + str(c) + ')'
    time_hera.append(timeit.timeit(str_, globals=globals(), number=5))

    str_ = 'primes_sieve_atkin(' + str(c) + ')'
    time_atkin.append(timeit.timeit(str_, globals=globals(), number=5))
    
    str_ = 'sieveOfAtkin(' + str(c) + ')'
    time_atkin2.append(timeit.timeit(str_, globals=globals(), number=5))    

plt.figure(1)
plt.plot(range_, time_naive, 'g-^', label='Naive')
plt.plot(range_, time_atkin, 'k-*', label='My Atkin')
plt.plot(range_, time_hera, 'r-o', label='Heratosthenes')
plt.plot(range_, time_atkin2, 'm-+', label='Efficient Atkin')
plt.ylabel('Execution time')
plt.xlabel('n')
plt.legend(loc='upper left')
plt.show()
