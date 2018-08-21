# PrimesList


This python script analyzes and compares three different approaches to calculating the list of primes up to a given number:

1. The simplest and possibly worst algorithm
2. A polished and more efficient version of the previous algorithm, but still naive
3. The sieve of Eratosthenes algorithm
4. The sieve of Atkin, which has a theoretical better performance than the other algorithms, but actually depends on the implementation used. See [here](https://web.archive.org/web/20071011180805/http://krenzel.info/static/atkin.py) for an efficient code implementation

the list of primes up to 10000 is computed 5 times for each algorithm and the execution time is measured and printed

<p align="center">
  <img src="https://github.com/dario-marvin/PrimesList/blob/master/prime0.png">
</p>

Some profiling of the execution time is then computed and plotted with the help of `matplotlib`

<p align="center">
  <img src="https://github.com/dario-marvin/PrimesList/blob/master/prime1.png">
</p>

<p align="center">
  <img src="https://github.com/dario-marvin/PrimesList/blob/master/prime2.png">
</p>
