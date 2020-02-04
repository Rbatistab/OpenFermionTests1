# This is very basic configuration for H2 in OpenFermion for it's use in
# posterior documents
 
# A. Molecule specification and input generation:
 
from openfermion.hamiltonians import MolecularData
 
geometry = [['H',[0,0,0]],['H',[0,0,0.74]]]
basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = MolecularData(geometry, basis, multiplicity, charge)

# D. Molecular data structure

from openfermion.ops import InteractionOperator

core_constant, one_body_integrals, two_body_integrals = (h2_molecule.get_active_space_integrals(occupied_indices=None,
                                                                                                active_indices=None))
# Original code takes arguments(occupied_indices,active_indices) and raises an exception for not being defined any of them, in the
# documentation says get_active_space_integrals(occupied_indices=None, active_indices=None) to restrict a molecule to at a spatial orbital
# level on active space
# ask Mauricio for suitable numbers
active_space_hamiltonian = InteractionOperator( core_constant,
                                                one_body_integrals,
                                                two_body_integrals)
