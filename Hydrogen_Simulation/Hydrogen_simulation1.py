# Molecule specification 
from openfermion.hamiltonians import MolecularData

geometry = [['H', [0, 0, 0]],
            ['H', [0, 0, 0.74]]]

basis = 'sto-3g'
multiplicity = 1
charge = 0

h2_molecule = MolecularData(geometry, basis, multiplicity, charge)
print(h2_molecule.get_molecular_hamiltonian())
print("Current simulation state:\n")
print("Geometry: H [0, 0, 0] - H[0, 0, 0.74]")
print("Basis: Slater-type orbitals, with three gaussians")
print("Spin multiplicity = 1")
print("Charge = 0")

# Second quantization in creation/anhilation operators

print("\nThe molecular Hamiltonian in the second quantization is: H_1 + H_2")

integrals = h2_molecule.get_integrals()

one_electron_hamiltonian = integrals[0]
two_electron_hamiltonian = integrals[1]

print("\nH_1 = \n")
h1 = ""
for i in range(2):
    for j in range(2):
        #str_coefficient =  '{:22}'.format( str(one_electron_hamiltonian[i][j]) )
        str_coefficient =  str(one_electron_hamiltonian[i][j])
        #literal_coef = '{:8}'.format("a\u2020" + str(i) + "a"+ str(j))
        literal_coef = "[a\u2020" + str(i) + "a"+ str(j) + "]"
        h1 += str_coefficient  + literal_coef 
        if not (i==1 and j==1):
            h1 += "  + " 

print(h1)

print("\nH_2 = \n")
h2 = ""

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                str_coefficient =  str(two_electron_hamiltonian[i][j][k][l])
                literal_coef = "[a\u2020" + str(i) + "a\u2020" + str(j) + "a" + str(k) + "a" + str(l) + "]"
                h2 += str_coefficient  + literal_coef 
                if not (i == 1 and j== 1 and k == 1 and l == 1):
                    h2 += " + " 
        h2+= "\n"

print(h2)

# Mapping to qubits by Bravyi-Kitaev
from openfermion.transforms import get_fermion_operator, bravyi_kitaev

h2_qubit_hamiltonian = bravyi_kitaev(get_fermion_operator(h2_molecule.get_molecular_hamiltonian() ))

print(h2_qubit_hamiltonian)
