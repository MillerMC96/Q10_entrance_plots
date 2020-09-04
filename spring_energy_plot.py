import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

dist = list()
time = list()
energy = list()

def get_energy(distance, k):
    return (distance * distance * k / 2)

fp = open(sys.argv[1])

#read file
while fp:
    line = fp.readline()
    if line:
        x, y = line.split()
        time.append(float(x))
        dist.append(float(y))
    else:
        break

#window
N = 4

#k constant (kJ/mol/A^2)
k_spring = 8.6745212210116

#energy
for distance in dist:
    energy.append(get_energy(distance, k_spring))

#moving mean
move_mean = np.convolve(energy, np.ones((N,))/N, mode = 'same')

#moving standard deviation
energy_pd = pd.Series(energy)
move_std = energy_pd.rolling(N).std()

#raw energy data
plt.scatter(time, energy, s = 2)

#plotting moving mean
plt.plot(time, move_mean, 'r', label = "moving average over " + str(N) + " ps")

#plotting moving std
dist_upper_bound = list()
dist_lower_bound = list()

for energy_point, std in zip(move_mean, move_std):
    dist_upper_bound.append(energy_point + std)
    dist_lower_bound.append(energy_point - std)

plt.fill_between(time, dist_upper_bound, dist_lower_bound, alpha = 0.4, label = "error band")

plt.ylim(energy_pd.min() - 200, energy_pd.max() + 200)
plt.xlabel("time [ps]")
plt.ylabel("energy [kJ/mol]")
plt.title("energy of the short axis expansion over time")
plt.legend(loc = 'best')
plt.show()

