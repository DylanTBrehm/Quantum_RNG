import qrand
import matplotlib.pyplot as plt
import numpy as np

rand_values = qrand.randbits(100000)

labels, counts = np.unique(rand_values, return_counts=True)

plot = plt.figure()
plt.bar(labels, counts, align="center")
plt.xticks(range(0, 1, 2))
plt.xlabel("Random Bit")
plt.ylabel("Bit Count")

plt.show()