import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

dist = list()
time = list()

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
N = 20

#moving mean
move_mean = np.convolve(dist, np.ones((N,))/N, mode = 'same')

#moving standard deviation
dist_pd = pd.Series(dist)
move_std = dist_pd.rolling(N).std()

plt.scatter(time, dist, s = 2)
#plt.hlines(6.525666667, time[0], time[-1], colors = 'k', linestyles = '--', label = "crystal structure")

#plotting moving mean
plt.plot(time[N-1:-N], move_mean[N-1:-N], 'r', label = "moving average over " + str(N) + " ps")

#plotting moving std
dist_upper_bound = list()
dist_lower_bound = list()

for dist_point, std in zip(move_mean, move_std):
    dist_upper_bound.append(dist_point + std)
    dist_lower_bound.append(dist_point - std)

plt.fill_between(time[N-1:-N], dist_upper_bound[N-1:-N], dist_lower_bound[N-1:-N], alpha = 0.4, label = "error band")

plt.xlabel("time [ps]")
#plt.ylabel("distance [Å]")
plt.title("2nd trajectory relative energy of entrance expansion over time")
plt.legend(loc = 'best')
plt.show()

