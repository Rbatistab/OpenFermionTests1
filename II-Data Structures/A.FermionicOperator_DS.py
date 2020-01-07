# A. FermionOperator data structure

from openfermion.ops import FermionOperator

# supposing p = 1, q = 0:i
a_p_dagger = FermionOperator('1^ ')
a_q = FermionOperator('0')

print(a_p_dagger)
print(a_q)

W = (1 + 2j) * FermionOperator('4^ 3 9 3^ ') - 4 * FermionOperator('2')
print("A fermion operator example: \nW = (1 + 2j)a^_4a_3a_9a^_3 - 4a_2\n W =")
print(W)
