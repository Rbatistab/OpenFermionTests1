# F. InteractionRDM:
 
from openfermion.hamiltonians import MolecularData
 
geometry = [['H',[0,0,0]],['H',[0,0,0.74]]]
basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)

# it is required a previous CISD calculation on h2_molecule

cisd_two_rdm = h2_molecule.get_molecular_rdm()
print(cisd_two_rdm)
