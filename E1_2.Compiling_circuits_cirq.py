# E. Compiling circuits for quantum algorithms, cirq:

import cirq
import openfermion
import openfermioncirq as ofc

hubbard_model = openfermion.fermi_hubbard(2, 2, 1.0, 4.0)
quad_ham = openfermion.get_quadratic_hamiltonian(hubbard_model, ignore_incompatible_terms = True)

qubits = cirq.LineQubit.range(8)
circuit =cirq.Circuit( ofc.prepare_gaussian_state( qubits, quad_ham) ) # change: cirq.Circuit.from_ops(args) ---> cirq.Circuit(args)
    # Reason:
    # The function Circuit.from_ops was used but is deprecated.
    # It will be removed in cirq v0.8.0.
    # use `cirq.Circuit(*ops)` instead.

print( circuit.to_text_diagram( transpose = True, use_unicode_characters = False) )
