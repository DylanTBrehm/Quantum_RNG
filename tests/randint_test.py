import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

upper_int = 10
lower_int = 0
num_samples = 10000

# rand_values = [qrand.randint(lower_int, upper_int) for i in range(0, num_samples)]

# labels, counts = np.unique(rand_values, return_counts=True)

# plt.figure(1)
# plt.bar(labels, counts, align="center")
# plt.xlabel("Random Number")
# plt.ylabel("Random Number Count")
# plt.title(f"Sampling of {num_samples} integers on AerSimulator")

# plt.show()

qrand.init(backend=FakeSherbrooke())
rand_values = [qrand.randint(lower_int, upper_int) for i in range(0, num_samples)]

labels, counts = np.unique(rand_values, return_counts=True)

plt.figure(2)
plt.bar(labels, counts, align="center")
plt.xlabel("Random Number")
plt.ylabel("Random Number Count")
plt.title(f"Sampling of {num_samples} integers on FakeSherbrooke")
plt.show()