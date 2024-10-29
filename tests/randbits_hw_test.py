import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit import IBMQ

IBMQ.load_account()
IBMQ.providers()
num_bits = 100000

rand_values = qrand.randbits(num_bits)

labels, counts = np.unique(rand_values, return_counts=True)

plt.figure(1)
plt.bar(labels, counts, align="center")
plt.xticks(range(0, 1, 2))
plt.xlabel("Random Bit")
plt.ylabel("Bit Count")
plt.title(f"Sampling of {num_bits} bits on AerSimulator")
plt.show()