#from openfermion.ops import QubitOperator
#from forestopenfermion import pyquilpauli_to_qubitop, qubitop_to_pyquilpauli
from openfermion.transforms import jordan_wigner
from openfermion.ops import FermionOperator, hermitian_conjugated

hubbard_hamiltonian = FermionOperator()
spatial_orbitals = 4
for i in range(spatial_orbitals):
    electron_hop_alpha = FermionOperator( ( (2*i, 1), (2*((i+1) % spatial_orbitals), 0 ) ) )
    electron_hop_beta = FermionOperator( ( (2*i + 1, 1), ( (2*((i + 1) % spatial_orbitals ) + 1), 0  ) ) )
    hubbard_hamiltonian += -1 * (electron_hop_alpha + hermitian_conjugated(electron_hop_alpha) )
    hubbard_hamiltonian += -1 * (electron_hop_beta + hermitian_conjugated(electron_hop_beta) )
    hubbard_hamiltonian += FermionOperator( (  (2 * i, 1), (2 * i, 0)
                                                (2 * i + 1, 1), (2 * i + 1, 0) ), 0.4)

print(hubbard_hamiltonian)
