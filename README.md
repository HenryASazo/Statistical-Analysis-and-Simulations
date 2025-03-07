﻿### **Repository: Mathematical Modeling and Simulation**

#### **Description**:

This repository contains a collection of Python-based simulations and analyses aimed at exploring various mathematical and statistical problems. Each problem involves the generation of random numbers, statistical modeling, and data visualization, with a particular focus on probability distributions, random processes, and Monte Carlo methods. The results are presented through histograms, which illustrate the distributions of the simulated data.

Each problem is described below along with the corresponding code functionality:

---

#### **Problem 1**: **Random Number Generation and Comparison**

- **1a**: Implementation of a Linear Congruential Generator (LCG) for generating 1000 uniformly distributed random numbers on the interval [0, 1]. The code simulates random number generation using the formula:  
  \[
  x*n = (a x*{n-1} + c) \mod m
  \]
  where \( a = 75 \), \( c = 0 \), and \( m = 2^{31} - 1 \). A histogram is generated to visualize the distribution of the generated numbers.

- **1b**: Comparison of the manually implemented LCG with Python’s built-in random number generator (`np.random.uniform`) by generating the same number of uniformly distributed random numbers and plotting their histograms.

The code generates histograms for the frequency of different values within the generated dataset, helping analyze the differences between the custom and built-in random number generators.

---

#### **Problem 2**: **Simulating Financial Price Fluctuations**

This problem uses the uniformly distributed random numbers from **Problem 1b** to simulate the daily price fluctuation of a financial asset. The asset’s price can either:

- Increase by 100 with a probability of 0.45,
- Decrease by 200 with a probability of 0.25, or
- Stay the same with a probability of 0.30.

The simulated price changes are displayed using a histogram, which helps visualize the distribution of possible price movements.

---

#### **Problem 3**: **Binomial Distribution Simulation**

Simulating 5000 binomially distributed random variables (X ~ Bin(70, 0.7)) using Bernoulli trials. A histogram is generated to show the distribution of successes in 70 trials, each with a success probability of 0.7. The probability of the random variable being less than 50 is also calculated, and the simulated value is compared to the theoretical probability.

---

#### **Problem 4**: **Normal Distribution Simulation**

Generating 1000 random variables from a normal distribution \( X \sim N(1.5, 4) \) (mean = 1.5, standard deviation = 2). A histogram is plotted to visualize the distribution of the values. The simulated probability that a random variable is greater than 0 is compared to the theoretical probability.

---

#### **Problem 5**: **Sampling Distribution of the Mean**

Simulating the sampling distribution by taking the mean of 20 normal variables (with mean = 1.5 and standard deviation = 2) for 100 samples. A histogram is plotted to visualize the distribution of the sample means, and the probability that the sample mean is greater than 0 is compared between the simulated and theoretical values.

---

#### **Problem 6**: **Estimating Expected Value Using Uniform Random Variables**

This problem simulates the estimation of the expected value \( E[N] \), where \( N \) is the number of trials until a uniform random variable exceeds 1. The code estimates \( E[N] \) by generating uniform random variables and organizing the results in a table, then comparing the simulated value with the theoretical value \( e \).

---

#### **Problem 7**: **Log-Normal Distribution Simulation**

Simulating 10,000 log-normal random variables by exponentiating normally distributed random variables with a mean of 10 and variance of 0.202. A histogram is plotted to visualize the distribution, and the expected value \( E[Y_1] \) is compared with the theoretical value \( e^{10.02} \).

---

#### **Problem 8**: **Monte Carlo Estimation of an Integral**

Using Monte Carlo methods to estimate the integral \( I = \int_0^1 \int_0^1 e^{x+y} \, dx \, dy \). The simulated estimate of the integral is compared to the theoretical value \( (e - 1)^2 \).

---

#### **Problem 9**: **Normal Approximation of the Binomial Distribution**

Verifying and sketching the normal approximation of the binomial distribution and proving that the sum of two normal random variables is itself normally distributed. The code also verifies that the sum of two uniform [0, 1] random variables follows a triangular distribution, and that the distribution of sums of fair die rolls approximates a normal distribution as the number of rolls increases.

---

### **Code Functionality Overview**:

The Python code in this repository includes implementations for various mathematical simulations and statistical analyses. Specifically, it:

1. Implements custom random number generators (LCG) and compares them to built-in generators.
2. Simulates different types of random variables (uniform, binomial, normal, log-normal) and their respective distributions.
3. Uses Monte Carlo methods to estimate integrals and expected values.
4. Plots histograms to visualize the distributions of simulated data.

The code leverages popular libraries such as `numpy`, `scipy`, `matplotlib`, and `tabulate` to facilitate random number generation, statistical modeling, plotting, and presenting results in a clear and organized manner.
