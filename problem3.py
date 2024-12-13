import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Problem 3: Generate Binomial Distributed Numbers
n = 70  # number of trials
p = .7 # probability of success in each trial
size = 5000 # number of random variables to generate
 
# Generating the Binomial distributed random numbers
binomial_data = np.random.binomial(n, p, size)

# Plotting the histogram of the Binomial distribution
plt.hist(binomial_data, bins=range(min(binomial_data), max(binomial_data) + 1), color="blue", alpha=.7, label="Binomial Histogram")
plt.title("Historgram of Binomial Distribution")
plt.xlabel("Number of Success")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Calculating the probability that the variable is less than 50
probability_less_than_50 = np.mean(binomial_data < 50)
print(f"Simulated Probability that the variable is less than 50: {probability_less_than_50:.4f}")