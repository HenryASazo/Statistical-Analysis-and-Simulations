import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Problem 4a: Generate random normal variables
mean = 1.5
std_dev = 2
size = 1000

# Generating the random normal variables
normal_data = np.random.normal(mean, std_dev, size)

# Generate random numbers and plot histogram
plt.hist(normal_data, bins=30, color="purple", alpha=.7, label ='Normal Distribution')
plt.title("Historgram of Normal Variables")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Problem 4b: Calculate the proportion greater than 0
count_above_zero = np.sum(normal_data > 0)
proportion_above_zero = count_above_zero / size
print(f"Proportion of variables greater than 0: {proportion_above_zero:.4f}")