# AKS Algorithm Optimized with Fast Fourier Transform (FFT)

This repository implements the **AKS Primality Test** optimized using **Fast Fourier Transform (FFT)** to improve polynomial multiplication performance. The AKS Primality Test is a deterministic primality test that determines whether a given number is prime. This implementation leverages FFT to speed up the polynomial multiplication step, making the algorithm more efficient for large numbers.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Benchmarking](#benchmarking)
- [Detailed Explanation](#detailed-explanation)
  - [What is the AKS Primality Test?](#what-is-the-aks-primality-test)
  - [Optimization with FFT](#optimization-with-fft)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **AKS Primality Test** is a famous primality test developed by Agrawal, Kayal, and Saxena in 2002. It is notable for being a deterministic polynomial-time algorithm to determine if a number is prime. This implementation uses the **Fast Fourier Transform (FFT)** to optimize polynomial multiplication, which is a crucial step in the AKS algorithm.

By using FFT for polynomial multiplication, we reduce the time complexity involved in this operation from O(n^2) to O(n log n), which helps the AKS test scale to larger numbers more efficiently.

### What is the AKS Primality Test?

The AKS Primality Test is a deterministic test that checks whether a given number \( n \) is prime. Before this test, primality tests like the Miller-Rabin test were probabilistic, which meant they might not always provide the correct answer. The AKS test, however, is deterministic and runs in polynomial time.

The AKS test consists of several steps:

**Perfect Power Check**  
   Verify if \( n \) is a perfect power. If \( n = a^b \) for integers \( a > 1 \) and \( b > 1 \), then \( n \) is **not prime**.

2. **Smallest \( r \) Calculation**  
   Find the smallest integer \( r \) such that the order of \( n \mod r \), denoted as \( \text{ord}_r(n) \), satisfies:  
   \[
   \text{ord}_r(n) > \log^2(n)
   \]

3. **GCD Check**  
   Check if \( \gcd(a, n) = 1 \) for all integers \( a \) where \( 1 \leq a \leq r \). If \( \gcd(a, n) > 1 \) for any \( a \), \( n \) is **not prime**.

4. **Polynomial Congruence**  
   Verify the following polynomial congruence:  
   \[
   (x + a)^n \equiv x^n + a \pmod{n, x^r - 1} \quad \text{for all } 1 \leq a \leq \lfloor \sqrt{\phi(r)} \log(n) \rfloor
   \]  
   If the congruence holds, \( n \) is **prime**; otherwise, it is **composite**.
The main computational challenge in the AKS test comes from the polynomial multiplication used in the congruence checks. This is where the **FFT** optimization comes in.

## Features

- **Primality Testing**: Checks if a given number is prime using the AKS algorithm.
- **FFT Optimization**: Polynomial multiplication is optimized using FFT for faster computation.
- **Benchmarking**: Includes a benchmarking tool to compare the performance of the normal AKS algorithm versus the FFT-optimized version.
- **Python Implementation**: Written in Python for easy understanding and modification.

## Installation

To run this project on your local machine, follow these steps:

### Prerequisites
Make sure you have **Python 3.x** installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

### Install Required Libraries

Clone the repository:

```bash
git clone https://github.com/Optimized-Brain/AKS-Algorithm-Optimized-with-Fast-Fourier-Transform.git
cd AKS-Algorithm-Optimized-with-Fast-Fourier-Transform

## Usage

This project implements the AKS Primality Test, both in its original form and an optimized version using Fast Fourier Transform (FFT). Follow the steps below to use and explore the functionality.

### Running the Benchmark

To compare the performance of the normal AKS algorithm and the FFT-optimized version, simply run the `main.py` file:
```bash
python main.py

