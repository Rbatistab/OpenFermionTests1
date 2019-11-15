# This is very basic configuration for H2 in OpenFermion for it's use in
# posterior documents

# A. Molecule specification and input generation:

from openfermion.hamiltonians import MolecularData

geometry = [['H',[0,0,0]],['H',[0,0,0.74]]]
basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)

