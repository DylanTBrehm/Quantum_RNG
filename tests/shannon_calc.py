import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke
import os


upper_int = 256
lower_int = 0
num_samples = 100

rand_values = [qrand.randint(lower_int, upper_int) for i in range(0,num_samples)]
labels, counts = np.unique(rand_values, return_counts=True)

shannon_entropy = 0
for count in counts:
    print(count)
    shannon_entropy += (count/upper_int) / np.log2(1/(count/upper_int))

print(f"Shannon Entropy is {shannon_entropy}")

shannon_file = open(os.getcwd() + "/data/shannon_calcs.csv", "w+")
shannon_file.write(str(shannon_entropy))