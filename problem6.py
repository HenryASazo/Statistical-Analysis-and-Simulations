import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.special import factorial
from scipy.integrate import dblquad
from tabulate import tabulate

def estimate_E_N(trials):
    # This function estimates E[N] for a given number of trials
    N_values = []

    for _ in range(trials):
        sum_u = 0   # Sum of uniform random variables
        n = 0   # Counter for the number of terms
        while sum_u <= 1:
            sum_u += np.random.uniform(0, 1)
            n += 1
        N_values.append(n)
    
    return np.mean(N_values)    # Return the average of N values as an estimate of E[N]

# Estimated values of E[N] for different numbers of trials
trials_list = [10, 100, 1000, 10000, 100000, 1000000]
estimates = {trial: estimate_E_N(trial) for trial in trials_list}

# Displaying the table of estimates
table = [(trial, estimates[trial]) for trial in trials_list]
print(tabulate(table, headers=["Number of Trials", "Estimated E[N]"], tablefmt='grid'))

# Theoretical calculation of E[N]
# For uniform random variables on [0,1], E[N] is known to converge to e (Euler's number)
theoretical_value = np.e

# Plotting the convergence of estimates
plt.figure(figsize=(10, 6))
plt.plot(trials_list, [estimates[trial] for trial in trials_list], marker='o', linestyle='-', color='b')
plt.axhline(y=theoretical_value, color='r', linestyle='--', label=f'Theoretical E[N] = {theoretical_value:.4f}')
plt.xscale('log')
plt.xlabel('Number of Trials')
plt.ylabel('Estimated E[N]')
plt.title('Convergence of Estimates for E[N]')
plt.legend()
plt.grid(True)
plt.show()

# Print the theoretical value and the simulated convergence value
print(f"Theoretical value of E[N]: {theoretical_value:.4f}")
print(f"Simulated value of E[N] converging towards: {estimates[1000000]:.4f}")
