import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

num_rands = 20000
num_bins = 15

rand_values = [qrand.rand() for i in range(0, num_rands)]

plt.figure(1)
plt.hist(rand_values, num_bins, edgecolor="black")
plt.xlabel("Bit Value")
plt.ylabel("Bit Count")
plt.title(f"Sampling of {num_rands} floats on AerSimulator")
plt.show()

qrand.init(backend=FakeSherbrooke())
rand_values = [qrand.rand() for i in range(0, num_rands)]

plt.figure(2)
plt.hist(rand_values, num_bins, edgecolor="black")
plt.xlabel("Bit Value")
plt.ylabel("Bit Count")
plt.title(f"Sampling of {num_rands} floats on FakeSherbrooke")
plt.show()