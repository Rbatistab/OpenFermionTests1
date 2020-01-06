# A. Molecule specification and input generation:

from openfermion.hamiltonians import MolecularData

geometry = [['H', [0,0,0] ],
            ['H', [0,0,0.74] ]]

basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)


# B. Integral generation:

from openfermionpyscf import run_pyscf

h2_molecule = run_pyscf( h2_molecule,
                        run_mp2=True,
                        run_cisd=True,
                        run_ccsd=True,
                        run_fci=True)

h2_filename = h2_molecule.filename
h2_molecule.save()


# E. Compiling circuits for quantum algorithms, cirq:

import cirq
import openfermioncirq as ofc

hamiltonian = h2_molecule.get_molecular_hamiltonian()
qubits = cirq.LineQubit.range(4)
circuit = cirq.Circuit(         # change by deprications: cirq.Circuit_from ops ---> cirq.Circuit, reasons bellow 
        ofc.simulate_trotter(
            qubits,
            hamiltonian,
            time = 1.0,
            n_steps = 1,
            order = 0,
            algorithm = ofc.trotter.LOW_RANK,
            omit_final_swaps = True
        )
    )
# WARNING:root:DEPRECATION
# The function Circuit.from_ops was used but is deprecated.
# It will be removed in cirq v0.8.0.
# use `cirq.Circuit(*ops)` instead.

cirq.merge_single_qubit_gates_into_phased_x_z(circuit)
print("Evolution of molecular Hamiltonian for H2")
output_string = circuit.to_text_diagram(use_unicode_characters=False)
print(output_string)

# output file generation for further and more contable use
output_file = open("E1_1.Compiling_circuits_cirq_OUTPUT.txt", "w")
output_file.write(output_string)
output_file.close()


