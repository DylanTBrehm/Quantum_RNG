import qrand
import matplotlib.pyplot as plt
import numpy as np

upper_int = 10
lower_int = 0

rand_values = [qrand.randint(lower_int, upper_int) for i in range(0,10000)]
# rand_values = qrand.randbits(100000)

labels, counts = np.unique(rand_values, return_counts=True)

plot = plt.figure()
plt.bar(labels, counts, align="center")
plt.xticks(range(0, 10, 1))
plt.xlabel("Random Number")
plt.ylabel("Random Number Count")

plt.show()