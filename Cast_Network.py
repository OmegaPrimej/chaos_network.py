import qiskit
from qiskit import QuantumCircuit, execute

qc = QuantumCircuit(5)
qc.h(range(5))
qc.measure(range(5), range(5))

job = execute(qc, backend='qasm_simulator')
result = job.result()

print(result.get_counts())
```

This script simulates a quantum circuit with 5 qubits, applies a Hadamard gate, measures the qubits, and prints the results.
