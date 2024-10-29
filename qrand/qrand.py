from typing import List
from qiskit import QuantumCircuit
from qiskit.providers.backend import Backend
from qiskit.primitives import BackendSamplerV2
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

_backend = AerSimulator()
_num_sample_bits = 64

def init(backend : Backend = AerSimulator(), num_sample_bits : int = 64):
    """
    Sets the qrand settings if the defaults are not desirable

    Args:
        backend (Backend, optional): Qiskit backend to use. Defaults to AerSimulator().
        samples (int, optional): Number of samples from the hadamard gate for bit generation. Defaults to 64.
    """

    _set_backend(backend)
    _set_samples(num_sample_bits)

def randbits(num_sample_bits : int = _num_sample_bits)-> List[int]:
    """
    Generates a list of random bits

    Returns:
        List[int]: List of random bits
    """

    circuit = QuantumCircuit(1)

    circuit.h(0)

    circuit.measure_all()

    pub = [(circuit)]
    sampler = BackendSamplerV2(backend=_backend)

    job = sampler.run(pub,shots=num_sample_bits)
    result = job.result()[0]
    rand_bits = result.data.meas.bitcount()

    return rand_bits

def randint(low : int, high : int) -> int:
    """
    Generates a random integer between low(inclusive) and high (exclusive)

    Args:
        low (int): lowest possible value(inclusive)
        high (int): highest possible value(exclusive)

    Returns:
        int: Random integer
    """

    rand_bits = randbits()

    rand_int = 0
    i = 0
    for bit in rand_bits:

        rand_int |= bit << i
        i += 1

    rand_int = int(_map_value(low, high, rand_int))

    return rand_int

def rand() -> float:
    """
    Creates a random float between 0 and 1

    Returns:
        float: Random float between 0 and 1
    """

    divider = 2**_num_sample_bits

    rand_float = float(randint(0, 2**_num_sample_bits) / divider)

    return rand_float

def _map_value(low : float, high : float, value : float) -> float:
    """
    Maps a 2**_num_sample_bits bit random number to a range of values

    Args:
        low (float): Low end of the range (Inclusive)
        high (float): High end of the range (Exclusive)
        value (float): The 2**_num_sample_bits bit random value to be mapped

    Returns:
        float: The mapped value
    """
    num_buckets = high - low

    mapping = num_buckets / (2**_num_sample_bits)

    mapped_value = mapping * value + low

    return mapped_value

def _set_backend(backend : Backend):
    """
    Set the backend for the circuit

    Args:
        backend (Backend): backend for circuit to use
    """

    global _backend
    _backend = backend

def _set_samples(samples : int):
    """
    Set the number of bits/samples used to generate randint and randfloat

    Args:
        samples (int): number of bits/samples to generate randint and randfloat
    """

    global _num_sample_bits

    _num_sample_bits = samples