from openfermion.hamiltonians import fermi_hubbard

x_dim = 4
y_dim = 1
periodic = True
chemical_potential = 0
tunneling = 1.0
coulomb = 4.0
of_hubbard_hamiltonian = fermi_hubbard(x_dim, y_dim, tunneling, coulomb, chemical_potential, spinless=False)
                    #paper says chemical_potential=None, but arises error
print(of_hubbard_hamiltonian)
