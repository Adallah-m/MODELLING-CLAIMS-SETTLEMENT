import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
lambda_ = 0.2  # Arrival rate of claims
mu = 1000     # Mean claim size
sigma = 200   # Standard deviation of claim size
T = 365       # Time horizon (in days)

# Generate inter-arrival times from exponential distribution
inter_arrivals = np.random.exponential(scale=1/lambda_, size=T)

# Generate claim sizes from a normal distribution
claim_sizes = np.random.normal(loc=mu, scale=sigma, size=T)

# Calculate the cumulative claim amounts over time
claim_amounts = np.cumsum(claim_sizes)

# Generate a standard Wiener process (Brownian motion)
dt = 1
n = int(T / dt)
increments = np.random.normal(scale=np.sqrt(dt), size=n)
increments[0] = 0
wiener_process = np.cumsum(increments)

# Combine the compound Poisson process and the Wiener process
claims = np.zeros(T)
arrival_times = np.cumsum(inter_arrivals)
for i in range(n):
    if i == 0:
        continue
    index = np.searchsorted(arrival_times, i*dt, side='right')
    if index > 0:
        claims[i*dt] = claim_amounts[index-1]

# Plot the compound Poisson process and the Wiener process
time = np.arange(T)
plt.plot(time, claims, label='Claim Amount')
plt.plot(time[:n], wiener_process, label='Wiener Process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

