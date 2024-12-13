import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

# Project Random Number Generator
def project_rng(seed=1, a=75, c=0, m=2**31-1, size=10000):
    numbers = np.zeros(size)
    numbers[0] = seed
    for i in range(1, size):
        numbers[i] = (a * numbers[i-1] + c) % m
    return numbers / m

# Problem 1a: Project Random Number Generator
def simulate_price_fluctuations(random_values, size=10000):
    fluctations = np.zeros(size)
    for i in range(size):
        r = random_values[i]
        if r < .45:     # 45% probability to increase by 100
            fluctations[i] = 100
        elif r < .70:   # 25% probability ot descrease by 200
            fluctations[i] = -200
        else:   # 30% probability to stay the same
            fluctations[i] = 0
    return fluctations

# Generate random numbers and plot histogram
random_numbers_lcg = project_rng()
random_numbers_builtin = np.random.uniform(0, 1, 10000)

price_fluctuations = simulate_price_fluctuations(random_numbers_lcg)
plt.hist(price_fluctuations, bins=(-250, -150, -50, 50, 150), color="red", label ='Price Fluctuations Histogram (Project)')
plt.title("Historgram of Price FLuctuations (Project RNG)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Problem 1b: Built-in RNG
price_fluctuations = simulate_price_fluctuations(random_numbers_builtin)
plt.hist(price_fluctuations, bins=(-250, -150, -50, 50, 150), color="blue", label ='Price Fluctuations Histogram (Built-In)')
plt.title("Historgram of Price Fluctuations (Built-in RNG)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()