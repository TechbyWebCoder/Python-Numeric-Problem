# 🔢 Number Theory & Mathematical Algorithms

> A curated collection of 50 classic number theory, combinatorics, and algorithmic problems — from perfect numbers to segmented sieves. Built for coding interview prep, competitive programming practice, and CS coursework.
<br>

# Python 50 Problems — Playlist

<p align="center">
  <a href="https://www.youtube.com/playlist?list=PLOIBhXPA6R_8">
    <img src="https://img.shields.io/badge/▶%20Watch%20Playlist-Python%2050%20Problems-red?style=for-the-badge&logo=youtube" alt="Watch Playlist">
  </a>
</p>

<br>
This repo works through 50 problems in seven stages: number-property checks, range-based generators, prime and divisor theory, factorials and combinatorics, the Fibonacci sequence, digit/root operations, and sieve algorithms. Each problem below lists a suggested approach and difficulty. Less common number types — sunny, spy, duck, neon, fascinating, and more.

**Language:** the folder layout and run commands below assume Python 3 (standard library only, no dependencies) — swap the file extension and run command to adapt to any other language.

## Number Classification Reference

Definitions for every number type used across the problem set below.

| Term | Definition | Example |
|---|---|---|
| **Perfect** | Equal to the sum of its own proper divisors | `6` → 1+2+3 = 6 |
| **Strong** | Sum of the factorials of its digits equals the number | `145` → 1!+4!+5! = 145 |
| **Armstrong (Narcissistic)** | Sum of its digits, each raised to the power of the digit count, equals the number | `153` → 1³+5³+3³ = 153 |
| **Automorphic** | Its square ends with the number itself | `25² = 625` (ends in 25) |
| **Harshad (Niven)** | Divisible by the sum of its own digits | `18` → digit sum 9, 18 ÷ 9 = 2 |
| **Neon** | The digit sum of its square equals the number itself | `9` → 9² = 81 → 8+1 = 9 |
| **Sunny** | `n + 1` is a perfect square | `3` → 3+1 = 4 = 2² |
| **Spy** | Sum of its digits equals the product of its digits | `123` → 1+2+3 = 6, 1×2×3 = 6 |
| **Duck** | Contains a `0` digit, but not as the leading digit | `3021` (zero appears, not first) |
| **Fascinating** | For a 3+ digit number, concatenating `n`, `2n`, `3n` yields a string containing every digit 1–9 | `192` → 192,384,576 → `192384576` |
| **Prime** | Greater than 1 with no divisors other than 1 and itself | `7` |
| **Twin primes** | A pair of primes that differ by exactly 2 | `(11, 13)` |
| **Emirp** | A prime that becomes a *different* prime when its digits are reversed | `13` ↔ `31` |
| **Palindromic prime** | A prime that reads the same forwards and backwards | `131` |
| **Happy** | Repeatedly summing the squares of its digits eventually reaches 1 | `19` → 82 → 68 → 100 → 1 |
| **Abundant** | Sum of proper divisors exceeds the number | `12` → 1+2+3+4+6 = 16 > 12 |
| **Deficient** | Sum of proper divisors is less than the number | `8` → 1+2+4 = 7 < 8 |
| **Fibonacci** | Appears in the sequence where each term is the sum of the two before it | `0, 1, 1, 2, 3, 5, 8, 13…` |

**Difficulty legend:** 🟢 Easy 🟡 Medium 🔴 Hard

## 1. Number Property Checks

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 1 | Perfect number | Sum proper divisors up to `√n`, compare to `n` | 🟢 Easy |
| 2 | Strong number | Sum the factorial of each digit, compare to `n` | 🟢 Easy |
| 3 | Armstrong number | Sum `digit ^ digit_count` for each digit, compare to `n` | 🟢 Easy |
| 4 | Automorphic number | Check that `n²` ends with `n` | 🟢 Easy |
| 5 | Harshad (Niven) number | Check `n % digit_sum == 0` | 🟢 Easy |
| 6 | Neon number | Sum the digits of `n²`, compare to `n` | 🟢 Easy |
| 7 | Sunny number | Check whether `n + 1` is a perfect square | 🟢 Easy |
| 8 | Spy number | Compare digit sum to digit product | 🟢 Easy |
| 9 | Duck number | Look for a `0` digit that isn't the leading digit | 🟢 Easy |
| 10 | Fascinating number | Concatenate `n, 2n, 3n`; check all digits 1–9 appear | 🟡 Medium |

## 2. Range-Based Generators

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 11 | Armstrong numbers in a range | Apply the Armstrong check to each value | 🟢 Easy |
| 12 | Perfect numbers in a range | Apply the perfect-number check to each value | 🟡 Medium |
| 13 | Strong numbers in a range | Apply the strong-number check to each value | 🟢 Easy |
| 14 | Prime numbers in a range | Trial division per value, or sieve the whole range | 🟢 Easy |
| 15 | Twin prime pairs in a range | Find consecutive primes `p` and `p + 2` | 🟡 Medium |
| 16 | Emirp numbers in a range | Prime, reverse is prime, and reverse ≠ original | 🟡 Medium |
| 17 | Palindromic primes in a range | Prime and equal to its own reverse | 🟡 Medium |
| 18 | Happy numbers in a range | Iterate the sum-of-squares-of-digits cycle | 🟡 Medium |
| 19 | Abundant numbers in a range | Sum of divisors greater than `n` | 🟢 Easy |
| 20 | Deficient numbers in a range | Sum of divisors less than `n` | 🟢 Easy |

## 3. Prime and Divisor Theory

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 21 | nth prime number | Sieve with an estimated upper bound, or incremental search | 🟡 Medium |
| 22 | Largest prime factor | Divide out factors from 2 upward, keep the last one | 🟢 Easy |
| 23 | Prime factorization | Trial division, collecting prime/exponent pairs | 🟢 Easy |
| 24 | Count total divisors | Count divisor pairs up to `√n` | 🟢 Easy |
| 25 | Sum of all divisors | Sum divisor pairs up to `√n` | 🟢 Easy |
| 26 | GCD (Euclidean algorithm) | `gcd(a, b) = gcd(b, a % b)` | 🟢 Easy |
| 27 | LCM using GCD | `lcm(a, b) = a * b / gcd(a, b)` | 🟢 Easy |
| 28 | Euler's Totient φ(n) | Multiply `n` by `(1 − 1/p)` for each distinct prime factor | 🟡 Medium |
| 29 | Coprime check | `gcd(a, b) == 1` | 🟢 Easy |
| 30 | Modular inverse | Extended Euclidean algorithm, or Fermat's little theorem | 🟡 Medium |
| 31 | `a^b mod m` (fast exponentiation) | Binary exponentiation, reducing mod `m` at each step | 🟡 Medium |
| 32 | Binary exponentiation | Square-and-multiply in `O(log n)` | 🟡 Medium |

## 4. Factorials and Combinatorics

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 33 | Large factorials (100!, 500!, 1000!) | Arbitrary-precision (big-integer) multiplication | 🟡 Medium |
| 34 | Trailing zeros in a factorial | Count factors of 5: `⌊n/5⌋ + ⌊n/25⌋ + …` | 🟡 Medium |
| 35 | Binomial coefficient (nCr) | `n! / (r!(n−r)!)`, or Pascal's triangle DP | 🟡 Medium |
| 36 | Permutations (nPr) | `n! / (n−r)!` | 🟢 Easy |
| 37 | Pascal's Triangle (N rows) | Each entry is the sum of the two entries above it | 🟢 Easy |
| 38 | Catalan numbers | `Cₙ = (2n)! / ((n+1)! n!)`, or the recurrence relation | 🟡 Medium |
| 39 | Bell numbers | Build the Bell triangle row by row | 🔴 Hard |
| 40 | Stirling numbers (2nd kind) | DP recurrence `S(n,k) = k·S(n−1,k) + S(n−1,k−1)` | 🔴 Hard |

## 5. Fibonacci Sequence

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 41 | Fibonacci check | `n` is Fibonacci iff `5n² + 4` or `5n² − 4` is a perfect square | 🟢 Easy |
| 42 | nth Fibonacci (DP) | Bottom-up iteration in `O(n)` | 🟢 Easy |
| 43 | nth Fibonacci (matrix exponentiation) | Raise `[[1,1],[1,0]]` to the nth power in `O(log n)` | 🔴 Hard |
| 44 | Sum of Fibonacci numbers in a range | Accumulate while generating, or use the identity `Σ = F(n+2) − 1` | 🟡 Medium |

## 6. Digit and Root Operations

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 45 | Digital root | Repeated digit sum, or the formula `1 + (n−1) % 9` | 🟢 Easy |
| 46 | Multiplicative persistence | Repeatedly multiply digits together; count steps to a single digit | 🟢 Easy |
| 47 | Integer square root (no `math.sqrt`) | Binary search for `⌊√n⌋` | 🟡 Medium |
| 48 | Cube root (binary search) | Binary search for `⌊n^(1/3)⌋` | 🟡 Medium |

## 7. Sieve Algorithms

| # | Problem | Approach | Difficulty |
|---|---|---|---|
| 49 | Sieve of Eratosthenes | Mark off multiples of each prime up to `N` | 🟡 Medium |
| 50 | Segmented Sieve | Sieve small primes first, then sieve each block of the range | 🔴 Hard |
