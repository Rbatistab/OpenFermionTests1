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

print(h2_qubit_hamiltonian)

# D. Numerical Testing:

from openfermion.transforms import get_sparse_operator
from scipy.linalg import eigh

h2_matrix = get_sparse_operator(h2_qubit_hamiltonian).todense()
eigenvalues, eigenvectors = eigh(h2_matrix)

print("\nH_2 Matrix:\n")
print(h2_matrix)
print("Eigen values: ")
print(eigenvalues)
print("Eigen vectors: ")
print(eigenvectors)
