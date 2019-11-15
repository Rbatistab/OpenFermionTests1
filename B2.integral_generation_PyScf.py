# A. Molecule specification and input generation

from openfermion.hamiltonians import MolecularData


geometry = [['H', [0,0,0] ],
            ['H', [0,0,0.74] ]]

basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)

# B. Integral generation

from openfermionpyscf import run_pyscf

h2_molecule = run_pyscf( h2_molecule,
                        run_mp2=True,
                        run_cisd=True,
                        run_ccsd=True,
                        run_fci=True)

h2_filename = h2_molecule.filename
h2_molecule.save()

h2_molecule2 = MolecularData(filename=h2_filename)

one_body_integrals = h2_molecule.one_body_integrals
print("One body integral: \n")
print(one_body_integrals)

two_body_integrals = h2_molecule.two_body_integrals
print("Two body integral: \n")
print(two_body_integrals)


