import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, fake_provider
from qiskit_aer import AerSimulator

runtime_service = QiskitRuntimeService()
backend = runtime_service.least_busy(min_num_qubits=1)
# backend = fake_provider.FakeSherbrooke()
# backend = AerSimulator()

num_bits = 100000

qrand.init(backend=backend)
rand_values = qrand.randbits(num_bits)

labels, counts = np.unique(rand_values, return_counts=True)

plt.figure(0)
plt.bar(labels, counts, align="center")
plt.xticks(range(0, 1, 2))
plt.xlabel("Random Bit")
plt.ylabel("Bit Count")
plt.title(f"Sampling of {num_bits} bits on {str(backend.name)}")
plt.show()

# upper_int = 16
# lower_int = 0
# num_samples = 10000

# rand_values = [qrand.randint(lower_int, upper_int) for i in range(0, num_samples)]

# labels, counts = np.unique(rand_values, return_counts=True)

# counts = counts / num_samples

# plt.figure(1)
# plt.bar(labels, counts, align="center")
# plt.xlabel("Random Number")
# plt.ylabel("Random Number Count")
# plt.title(f"Sampling of {num_samples} integers on {backend.name}")

# plt.show(block=False)

# num_rands = 20000
# num_bins = 15

# rand_values = [qrand.rand() for i in range(0, num_rands)]

# plt.figure(2)
# plt.hist(rand_values, num_bins, edgecolor="black")
# plt.xlabel("Bit Value")
# plt.ylabel("Bit Count")
# plt.title(f"Sampling of {num_rands} floats on {backend.name}")
# plt.show()