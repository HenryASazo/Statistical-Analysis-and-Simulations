import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Problem 5: Generate sample means from normal variables
mean = 1.5
std_dev = 2
samples = 100
observations_per_sample = 20

# Generating the sample means
sample_means = [np.mean(np.random.normal(mean, std_dev, observations_per_sample, )) for _ in range(samples)]

# Plotting the histogram of sample means
plt.hist(sample_means, bins=np.arange(-4, 10.5, 0.5), color="orange", alpha=0.7, label='Sample Means Distributions')
plt.title("Historgram of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Calculating the proportion of sample means greater than 0
proportion_above_zero = np.mean(np.array(sample_means) > 0)
print(f"Proportion of sample means greater than 0: {proportion_above_zero:.4f}")