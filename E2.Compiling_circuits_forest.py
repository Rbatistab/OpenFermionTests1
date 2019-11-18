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

# C. Mapping to qubits: 

from openfermion.transforms import get_fermion_operator, jordan_wigner

h2_qubit_hamiltonian = jordan_wigner(get_fermion_operator(h2_molecule.get_molecular_hamiltonian() ) )


# E. Compiling circuits for quantum algorithms, cirq:

import cirq
import openfermioncirq as ofc

hamiltonian = h2_molecule.get_molecular_hamiltonian()
qubits = cirq.LineQubit.range(4)
circuit = cirq.Circuit.from_ops(
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

cirq.merge_single_qubit_gates_into_phased_x_z(circuit)
print(circuit.to_text_diagram(use_unicode_characters=False))
