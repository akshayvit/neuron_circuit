from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector,plot_histogram
from math import *
def x_measurement(qc, qubit, cbit):
    qc.h(qubit)
    qc.measure(qubit, cbit)
    return qc
circuit=QuantumCircuit(2,2)
circuit.x(0)
circuit.y(0)
circuit.z(0)
circuit.cx(0,1)
initial_state = [1/sqrt(2), -1/sqrt(2)]
circuit.initialize(initial_state,0)
simulator=Aer.get_backend('statevector_simulator')
result=execute(circuit,backend=simulator).result()
sv=result.get_statevector()
print(sv)
%matplotlib inline
circuit.draw(output='mpl')
plot_bloch_multivector(sv)
x_measurement(circuit,0,0)
circuit.draw()
qobj = assemble(circuit)  # Assemble circuit into a Qobj that can be run
counts = simulator.run(qobj).result().get_counts()
plot_histogram(counts)
