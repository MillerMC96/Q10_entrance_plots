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

#moving standard deviation
dist_pd = pd.Series(dist)
std = dist_pd.std()

#Avogadro number
Na = 6.0221409 * 10 ** 23

#Boltzmann constant (J/K)
k_b = 1.380649 * 10 ** (-23)

#temperature 310 K
Temp = 310

#formula
k_therm = k_b * Temp * Na / 1000 / (std ** 2)

#result
print("k_thermal is " + str(k_therm) + " kJ/mol/A^2")
