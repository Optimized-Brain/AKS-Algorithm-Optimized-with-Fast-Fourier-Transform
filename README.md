# AKS Algorithm Optimized with Fast Fourier Transform (FFT)

This repository implements the **AKS Primality Test** optimized using **Fast Fourier Transform (FFT)** to improve polynomial multiplication performance. The AKS Primality Test is a deterministic primality test that determines whether a given number is prime. This implementation leverages FFT to speed up the polynomial multiplication step, making the algorithm more efficient for large numbers.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Detailed Explanation](#detailed-explanation)
  - [What is the AKS Primality Test?](#what-is-the-aks-primality-test)
  - [Optimization with FFT](#optimization-with-fft)

## Introduction

The **AKS Primality Test** is a famous primality test developed by Agrawal, Kayal, and Saxena in 2002. It is notable for being a deterministic polynomial-time algorithm to determine if a number is prime. This implementation uses the **Fast Fourier Transform (FFT)** to optimize polynomial multiplication, which is a crucial step in the AKS algorithm.

By using FFT for polynomial multiplication, we reduce the time complexity involved in this operation from $\( O(n^2) \)$ to $\( O(n \log n) \)$, which helps the AKS test scale to larger numbers more efficiently.


## Features

- **Primality Testing**: Checks if a given number is prime using the AKS algorithm.
- **FFT Optimization**: Polynomial multiplication is optimized using FFT for faster computation.
- **Benchmarking**: Includes a benchmarking tool to compare the performance of the normal AKS algorithm versus the FFT-optimized version.
- **Python Implementation**: Written in Python for easy understanding and modification.

## Installation

To run this project on your local machine, follow these steps:


1. **Clone the Repository**  
   Clone the repository using Git and navigate to the project directory:  
   ```bash
   git clone https://github.com/YourUsername/AKS-Algorithm-Optimized-with-Fast-Fourier-Transform.git
   cd AKS-Algorithm-Optimized-with-Fast-Fourier-Transform
2. **Create a Virtual Environment** (optional but recommended)

Create and activate a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```
3. **Install Dependencies**
Use the requirements.txt file to install the necessary Python libraries:
```bash
pip install -r requirements.txt
```
4. **Verify Installation**
Run the project to ensure it is set up correctly:
```bash
python main.py
```

This will execute the benchmarking script and display a comparison of the normal AKS algorithm and the FFT-optimized version.


### Prerequisites
Make sure you have **Python 3.x** installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

### Install Required Libraries

Clone the repository:

```
git clone https://github.com/Optimized-Brain/AKS-Algorithm-Optimized-with-Fast-Fourier-Transform.git
cd AKS-Algorithm-Optimized-with-Fast-Fourier-Transform

```


## Usage

This project provides an implementation of the AKS (Agrawal-Kayal-Saxena) Primality Test, both in its original form and optimized using Fast Fourier Transform (FFT). Below are the steps to use the project, including running benchmarks, testing primality of numbers, and customizing the input for performance evaluation.

1. ### Running the Benchmark

The benchmarking script compares the performance of the normal AKS algorithm and the FFT-optimized version across various input sizes.

To run the benchmark, simply execute the `main.py` file:

   ```
   python main.py
```

The script will display a table comparing the execution time of both implementations for different input sizes. Here's an example of the output:


      Input |  Normal AKS Time (s) |     FFT AKS Time (s) |      Improvement (%)
----------------------------------------------------------------------------
        100 |             0.012345 |             0.005678 |              54.05%
        200 |             0.045678 |             0.015678 |              65.69%

This output allows you to see the time improvement achieved by using FFT over the traditional AKS algorithm.

2. **Customizing the Input Sizes for Benchmarking**

The benchmarking input sizes are specified in the `benchmark_aks()` function, located in the `src/benchmarks.py` file. By default, it tests against numbers like 1000, 2000, 5000, 10000 and 20000.

To modify the input sizes, you can change the values in the ns list. For example:

```python
ns = [1000, 2000, 5000, 10000, 20000]  # Adjust the numbers to test
```
After making changes, save the file and rerun the benchmark using the following command:
```bash
python main.py
```

### Testing Primality of a Single Number

To test whether a given number is prime using the AKS primality test (either the standard version or the optimized FFT version), you can use the following code.

1. **Test Primality with Normal AKS Algorithm**

You can test the primality of a number using the standard AKS primality test by importing and calling the normal_aks_primality_test() function from the src/aks.py file.

Example usage:
```python from src.aks import normal_aks_primality_test

number = 101

# Test primality using the normal AKS algorithm
is_prime = normal_aks_primality_test(number)

print(f"{number} is {'prime' if is_prime else 'not prime'}.")
```

**Sample Output:**
```
101 is prime.
```
2. **Test Primality with FFT-Optimized AKS Algorithm**

You can also test primality using the FFT-optimized AKS algorithm by calling the fft_aks_primality_test() function in a similar manner.

Example usage:
```python
from src.aks import fft_aks_primality_test

number = 101

# Test primality using the FFT-optimized AKS algorithm
is_prime_fft = fft_aks_primality_test(number)

print(f"{number} is {'prime' if is_prime_fft else 'not prime'}.")
```

**Sample Output:**
```
101 is prime.
```
### Extending the Project ###

This project is designed to be modular and extensible. You can easily add new features or optimize the existing ones by modifying the following files:

`src/fft.py`: This performs polynomial multiplication using both naive and FFT-based approach, which can also be used to implement any other algorithm for polynomial multiplication. 

`src/aks.py`: This contains implementation of standard AKS algorithm as well as FFT-based implementation of AKS algorithm, which can be used for other primality tests. 

`src/benchmarks.py`: Customize the benchmarking script by changing the input sizes or adding new profiling configurations.

### Example Use Cases ###
* **Simple Primality Testing**: Quickly check if a number is prime using either the normal AKS algorithm or the FFT-optimized version.
* **Performance Comparison**: Use the benchmarking tools to compare the runtime of the normal and FFT-based AKS algorithms.
* **Optimization**: Extend the project by implementing advanced optimizations for AKS or integrating other primality testing algorithms.

## Detailed Explanation
### What is the AKS Primality Test?

The AKS Primality Test is a deterministic test that checks whether a given number $\( n \)$ is prime. Before this test, primality tests like the Miller-Rabin test were probabilistic, which meant they might not always provide the correct answer. The AKS test, however, is deterministic and runs in polynomial time.

The AKS test consists of several steps:

**Perfect Power Check**  
   Verify if $\( n \)$ is a perfect power. If $\( n = a^b \)$ for integers $\( a > 1 \)$ and $\( b > 1 \)$, then $\( n \)$ is **not prime**.

2. **Smallest \( r \) Calculation**  
   Find the smallest integer \( r \) such that the order of \( n \mod r \), denoted as \( \text{ord}_r(n) \), satisfies:  
   $\[
   \text{ord}_r(n) > \log^2(n)
   \]$

3. **GCD Check**  
   Check if $\( \gcd(a, n) = 1 \)$ for all integers $\( a \)$ where $\( 1 \leq a \leq r \)$. If $\( \gcd(a, n) > 1 \)$ for any $\( a \)$, $\( n \)$ is **not prime**.

4. **Polynomial Congruence**  
   Verify the following polynomial congruence:  
   $\[
   (x + a)^n \equiv x^n + a \pmod{n, x^r - 1} \quad \text{for all } 1 \leq a \leq \lfloor \sqrt{\phi(r)} \log(n) \rfloor
   \] $ 
   If the congruence holds, $\( n \)$ is **prime**; otherwise, it is **composite**.
The main computational challenge in the AKS test comes from the polynomial multiplication used in the congruence checks. This is where the **FFT** optimization comes in.

### Optimization with FFT


In this project, we optimize the AKS (Agrawal-Kayal-Saxena) primality test by incorporating the Fast Fourier Transform (FFT) to speed up the polynomial multiplication steps. The standard AKS algorithm involves polynomial arithmetic, which is the most computationally expensive part of the algorithm. By using FFT, we can perform these polynomial multiplications much faster, thus improving the overall performance of the primality test.

#### The Role of FFT in AKS

The main computational cost of the AKS primality test comes from polynomial multiplication, which is involved in checking certain conditions related to the order of elements and congruence relations. In the standard AKS algorithm, polynomial multiplication is performed naively, which has a time complexity of $\( O(n^2) \)$, where $\( n \)$ is the degree of the polynomials.

FFT, on the other hand, provides a way to multiply polynomials in $\( O(n \log n) \)$ time. This drastic improvement in time complexity is due to the fact that FFT allows us to evaluate polynomials at certain points in a highly efficient manner, enabling us to perform pointwise multiplication and inverse FFT to obtain the product of two polynomials.

#### Polynomial Multiplication Using FFT

Let $\( A(x) \)$ and $\( B(x) \)$ be two polynomials of degree $\( n \)$:

$\[
A(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_{n-1} x^{n-1}
\]
\[
B(x) = b_0 + b_1 x + b_2 x^2 + \cdots + b_{n-1} x^{n-1}
\]$

The naive polynomial multiplication requires $\( O(n^2) \)$ operations, where we compute each coefficient of the resulting polynomial by multiplying terms of $\( A(x) \)$ and $\( B(x) \)$. However, with FFT, we transform the polynomials to the frequency domain, multiply the corresponding coefficients, and then transform them back to the coefficient domain.

#### Steps for Polynomial Multiplication with FFT:

1. **Transform the polynomials**: Apply the FFT to both polynomials $\( A(x) \)$ and $\( B(x) \)$, which converts the polynomials into their evaluations at specific points (the roots of unity).
   
   $\[
   A(\omega^k) \quad \text{and} \quad B(\omega^k) \quad \text{for} \quad k = 0, 1, 2, \dots, n-1
   \]$
   where $\( \omega \)$ is a primitive $\( n \)$-th root of unity.

2. **Pointwise multiplication**: Multiply the transformed values pointwise:

   $\[
   C(\omega^k) = A(\omega^k) \cdot B(\omega^k)
   \]$

3. **Inverse Transform**: Apply the inverse FFT to $\( C(\omega^k) \)$ to obtain the coefficients of the resulting polynomial $\( C(x) \)$.

4. **Recover the result**: The coefficients of the resulting polynomial are the values obtained from the inverse FFT. We round them to integers to remove any imaginary components introduced by the numerical methods in FFT.

#### Equations Involved

Given the polynomials $\( A(x) \)$ and $\( B(x) \)$, their FFT-based multiplication involves the following equations:

1. **FFT Transformation**:
   
   $\[
   A(\omega^k) = \sum_{i=0}^{n-1} a_i \omega^{ik}
   \]$
   $\[
   B(\omega^k) = \sum_{i=0}^{n-1} b_i \omega^{ik}
   \]$

2. **Pointwise Multiplication**:
   
   $\[
   C(\omega^k) = A(\omega^k) \cdot B(\omega^k)
   \]$

3. **Inverse FFT**:
   
   $\[
   C(x) = \frac{1}{n} \sum_{k=0}^{n-1} C(\omega^k) \omega^{-ik}
   \]$

The result $\( C(x) \)$ gives the product of the polynomials $\( A(x) \)$ and $\( B(x) \)$.

#### Time Complexity

- **Naive Polynomial Multiplication**: The naive approach to polynomial multiplication has a time complexity of $\( O(n^2) \)$, where $\( n \)$ is the degree of the resulting polynomial.
  
- **FFT-based Polynomial Multiplication**: By using FFT, we reduce the time complexity to $\( O(n \log n) \)$, where $\( n \)$ is the number of coefficients. This provides a significant speedup, especially for large polynomials.

#### Benefit in AKS Primality Test

By replacing the naive polynomial multiplication with FFT-based multiplication, the overall time complexity of the AKS primality test is reduced, especially for larger numbers. FFT reduces the time taken for the polynomial multiplications that occur during the polynomial congruence check, allowing the test to scale better with larger input numbers.

### Summary

- **Naive polynomial multiplication**: $\( O(n^2) \)$
- **FFT-based polynomial multiplication**: $\( O(n \log n) \)$
- **Improvement in AKS**: FFT optimization speeds up polynomial multiplication, improving the overall runtime of the AKS primality test for large inputs.

By leveraging FFT, this project significantly enhances the performance of the AKS primality test, enabling it to handle larger numbers efficiently, making it more practical for use in real-world applications.
