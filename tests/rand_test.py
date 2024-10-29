import qrand
import matplotlib.pyplot as plt
import numpy as np

print(qrand.rand())
num_rands = 20000
num_bins = 15

rand_values = [qrand.rand() for i in range(0, num_rands)]

plt.hist(rand_values, num_bins, edgecolor="black")
plt.show()