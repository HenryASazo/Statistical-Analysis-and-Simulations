import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Problem 1a: Project Random Number Generator
def project_rng(seed=1, a=75, c=0, m=2**31-1, size=10000):
    numbers = np.zeros(size)
    numbers[0] = seed
    for i in range(1, size):
        numbers[i] = (a * numbers[i-1] + c) % m
    return numbers / m

# Generate random numbers and plot histogram
random_numbers_lcg = project_rng()
plt.hist(random_numbers_lcg, bins=20, alpha=.7, label ='Project RNG Histogram')
plt.title("Historgram of Uniformaly Distrubted Random Numbers (Project)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Problem 1b: Built-in RNG
random_numbers_builtin = np.random.uniform(0, 1, 10000)
plt.hist(random_numbers_builtin, bins=20, alpha=.7, color="green", label ='Built-in RNG Histogram')
plt.title("Historgram of Uniformaly Distrubted Random Numbers (Built-in)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Problem 1a
# In problem 1a, we were tasked with building a random number generator 
# 𝒙n ≡ (𝒂𝒙n-1 + 𝒄) 𝒎𝒐𝒅(𝒎) with 𝒂 = 𝟕5 , 𝒄 = 𝟎 𝒂𝒏𝒅 𝒎 = 𝟐31 − 𝟏 
# and generating 1000 uniformly distributed numbers on [0, 1]. 
# The histogram obtained from this method is below.

# Problem 1b
# In 1b, we used the built in function in Python to also generate 
# 1000 uniformly distributed numbers on [0, 1]. The histogram 
# obtained from this method is below. The histogram obtained 
# from the random number generator that we built and the 
# histogram obtained from the built-in Python function have 
# a minimum frequency of about 450, a maximum frequency 
# of about 550, and an average frequency of about 500. 
# However, the histogram obtained from the random number 
# generator we built has a greater number of values that 
# take a range of frequencies, whereas the histogram obtained 
# from the built-in random number generator has a greater 
# number of values that take the average frequency. 
# Our biggest takeaway from this is that random 
# number generators are not truly random, and that they 
# must be given some sort of seed values in order to function. 
