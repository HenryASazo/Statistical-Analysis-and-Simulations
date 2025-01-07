import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Monte Carlo Integration Function 
def monte_carlo_integration(samples, runs=10):
    estimates = []
    for _ in range(runs):
        x = np.random.uniform(0, 1, samples)
        y = np.random.uniform(0, 1, samples)
        z = np.exp(x + y)
        estimates.append(np.mean(z))
    return np.mean(estimates)   # Average over multiple runs for stability

# Theoretical calculations using double integration
def theoretical_integral():
    result, _ = dblquad(lambda x, y: np.exp(x+y), 0, 1, lambda x: 0, lambda x: 1)
    return result

# Using a larger number of samples and mutliple runs
samples_list = [1000, 10000, 100000, 1000000]
estimates = [monte_carlo_integration(samples, runs=30) for samples in samples_list]

# Theoretical calculation of the integral
theoretical_value = theoretical_integral()

# Plotting the estimates
plt.figure(figsize=(10, 6))
plt.plot(samples_list, estimates, marker='o', linestyle='-', color='b', label='Monte Carlo Estimates')
plt.axhline(y=theoretical_value, color='r', linestyle='--', label=f'Theoretical Value = {theoretical_value:.4f}')
plt.xscale('log')
plt.xlabel('Number of Samples')
plt.ylabel('Estimated Integral')
plt.title('Monte Carlo Integration Estimates for I')
plt.legend()
plt.grid(True)
plt.show()

# Print the theoretical value and the latest estimate for direct compariosn
print(f"Theoretical value of the integral I: {theoretical_value:.4f}")

