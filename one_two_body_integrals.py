from openfermion.hamiltonians import MolecularData
from openfermionpsi4 import run_psi4

geometry = [['H', [0,0,0] ],
            ['H', [0,0,0.74] ]]

basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)

h2_molecule = run_psi4( h2_molecule,
                        run_mp2=True,
                        run_cisd=True,
                        run_ccsd=True,
                        run_fci=True)

two_electron_integrals = h2_molecule.two_body_integrals
one_electron_integrals = h2_molecule.one_body_integrals

print("Two electron integrals:\n")
print(two_electron_integrals)
print("One electron integrals:\n")
print(one_electron_integrals)

orbitals = h2_molecule.canonical_orbitals

print("Orbital coefficients:\n")
print(orbitals)

