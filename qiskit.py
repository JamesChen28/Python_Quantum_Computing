
# https://github.com/Qiskit/qiskit
# https://qiskit.org/documentation/tutorials/circuits/1_getting_started_with_qiskit.html


import numpy as np
from qiskit import __version__, QuantumCircuit
from qiskit.tools.visualization import circuit_drawer

qiskit.__version__


## A quantum circuit for preparing the quantum state |000> + i |111>
qc = QuantumCircuit(3)
circuit_drawer(qc)

# generate superpostion
qc.h(0)
circuit_drawer(qc)

# add quantum phase
qc.p(np.pi/2, 0)
circuit_drawer(qc)

# 0th-qubit-Controlled-NOT gate on 1st qubit
qc.cx(0, 1)
circuit_drawer(qc)

# 0th-qubit-Controlled-NOT gate on 2nd qubit
qc.cx(0, 2)
circuit_drawer(qc)

# visualize circuit
qc.draw()
qc.draw('mpl')


## Simulating circuits using Qiskit Aer

from qiskit import Aer

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')

# Create a Quantum Program for execution
job = backend.run(qc)

result = job.result()
status = job.status()

# Return state vector for the quantum circuit
outputstate = result.get_statevector(qc, decimals = 3)

# Use the visualization function to plot the real and imaginary components of the state density matrix
from qiskit.visualization import plot_state_city
plot_state_city(outputstate)




## transpile
# Create a Quantum Circuit
meas = QuantumCircuit(3, 3)
circuit_drawer(meas)

meas.barrier(range(3))
circuit_drawer(meas)

# map the quantum measurement to the classical bits
meas.measure(range(3), range(3))
circuit_drawer(meas)

# The Qiskit circuit object supports composition using
# the compose method.
qc.add_register(meas.cregs[0])
qc = qc.compose(meas)
circuit_drawer(qc)

#drawing the circuit
qc.draw()

# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
from qiskit.compiler import transpile
job_sim = backend_sim.run(transpile(qc, backend_sim), shots = 1024)

# Grab the results from the job.
result_sim = job_sim.result()

counts = result_sim.get_counts(qc)



