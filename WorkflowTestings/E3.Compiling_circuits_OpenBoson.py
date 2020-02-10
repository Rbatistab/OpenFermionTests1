# Bose-Hubabrd Hamiltonian, via openfermion:

from openfermion.hamiltonians import bose_hubbard

H = bose_hubbard(2, 2, tunneling = 1, interaction = 1.5, chemical_potential = 0.5)
print("Bose-Hubabrd Hamiltonian, via openfermion:\n")
print(H)

# SFOpenBoson plugin:

import strawberryfields as sf                   # this line generates an error
# ImportError: cannot import name 'root_scalar' from 'scipy.optimize' (/home/hp/anaconda3/lib/python3.7/site-packages/scipy/optimize/__init__.py)
from strawberryfields.ops import Fock
from sfopenboson.ops import BoseHubbardPropagation

t = 0.1                                         #time evolution in t = 0.1
eng, q = sf.Engine(4)
with eng:
    # creation of 2 qumode quantum circuit
    Fock(2) | q[0]                              # System initialized in Fock state |2,0,0,0>
    BoseHubbardPropagation(H, t, k=20) | q      # Lie product formula truncated to 20 terms
    
state = eng.run('fock', cutoff_dim = 3)
print("And via SFOpenBoson:\n")
eng.print_applied()
