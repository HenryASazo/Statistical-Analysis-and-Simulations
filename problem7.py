import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Parameters for the normal distribution
mu = 10
sigma = np.sqrt(0.20)   # Standard deviation is the square root of variance

# Theoretical expectation of th elog-normal variable
theoretical_EY = np.exp(mu + sigma**2 / 2)

# Generating 10000 samples of X1
X1_samples = np.random.normal(mu, sigma, 10000)

# Converting to log-normal samples
Y1_samples = np.exp(X1_samples)

# Estimating E[Y] using the samples
estimated_EY = np.mean(Y1_samples)

# Plotting the histogram of the log-normal samples
plt.figure(figsize=(10,6))
plt.hist(Y1_samples, bins=50, color='blue', alpha=0.7)
plt.title('Histogram of Log-Normal Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Print the theoretical and estimated values
print(f"Theoretical E[Y1]: {theoretical_EY:.4f}")