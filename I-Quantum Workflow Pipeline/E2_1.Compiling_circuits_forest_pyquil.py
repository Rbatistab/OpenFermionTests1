from openfermion.ops import QubitOperator
from forestopenfermion import pyquilpauli_to_qubitop, qubitop_to_pyquilpauli

hubbard_term_generator = jordan_wigner(hubbard_hamiltonian)
pyquil_hubbard_generator = qubito_to_pyquilpauli(hubbard_term_generator)

from pyquil.quil import Program
from pyquil.gates import X
from pyquil.paulis import exponentiate

localized_electrons_program = Program()
localized_electrons_program.inst([X(0) , X(1)])
pyquil_program = Program()
for term in pyquil_hubbard
