import qrand
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke
import os
import scipy

#This python file is a WIP and does not work

upper_int = 2**8
lower_int = 0
num_samples = 2**12

rand_values = [qrand.randint(lower_int, upper_int) for i in range(0,num_samples)]
labels, counts = np.unique(rand_values, return_counts=True)

shannon_entropy = 0
for count in counts:
    print(count)
    shannon_entropy += (count/upper_int) * np.log2(1/(count/upper_int))

print(scipy.stats.entropy(counts))

print(f"Shannon Entropy is {shannon_entropy}")

shannon_file = open(os.getcwd() + "/data/shannon_calcs.csv", "w+")
shannon_file.write(str(shannon_entropy))