import numpy as np

# Parameters for compound Poisson process
arrival_rate = 0.1  # Example arrival rate
mean_claim_size = 5000  # Example mean claim size

# Parameters for standard Wiener process
volatility = 0.2  # Example volatility

# Time parameters
num_periods = 100  # Number of periods to forecast
time_interval = 1  # Time interval for each period

# Simulating compound Poisson process for claim arrivals
num_arrivals = np.random.poisson(arrival_rate * num_periods)
arrival_times = np.sort(np.random.uniform(0, num_periods, num_arrivals))

# Simulating standard Wiener process for claim sizes
normal_samples = np.random.normal(0, 1, num_arrivals)
claim_sizes = mean_claim_size * np.exp(volatility * normal_samples)

# Simulating total claim amounts for each period
total_claim_amounts = np.zeros(num_periods)
for i in range(num_arrivals):
    period_idx = int(arrival_times[i])
    total_claim_amounts[period_idx:] += claim_sizes[i]

# Print the simulated claim amounts for each period
for period, claim_amount in enumerate(total_claim_amounts):
    print(f"Period {period+1}: Expected Claim Amount = {claim_amount:.2f}")
