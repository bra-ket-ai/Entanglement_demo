from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second qubit as target
qc.cx(0, 1)

# The circuit now creates an entangled state between the two qubits

# To visualize the circuit
print(qc)

# To execute the circuit and see the result, additional code is required to set up a quantum simulator or quantum computer.