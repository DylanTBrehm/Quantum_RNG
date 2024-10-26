from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)

qc.h(0)

qc.cx(0, 1)

qc.draw("mpl")

plt.show()