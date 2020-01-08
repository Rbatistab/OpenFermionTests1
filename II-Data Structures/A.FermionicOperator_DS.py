# A. FermionOperator data structure

from openfermion.ops import FermionOperator

# supposing p = 1, q = 0:i
a_p_dagger = FermionOperator('1^ ')
a_q = FermionOperator('0')

print("Printing fermionic operators:\n")
print("a^dagger_p:")
print(a_p_dagger)
print("a_q:")
print(a_q)

W = (1 + 2j) * FermionOperator('4^ 3 9 3^ ') - 4 * FermionOperator('2')
print("\nA fermion operator example: \nW = (1 + 2j)a^_4a_3a_9a^_3 - 4a_2\n W =")
print(W)

from openfermion.utils import normal_ordered
W_normal_ordered = normal_ordered(W)

print("\nNormal Ordered W:")
print(W_normal_ordered)

W_i = 3 * W - W ** 2

print("\n3W - W^2, normal ordered:")
print(normal_ordered(W_i))

print("\nLadder Operators:")
print("\n() -> 1:")
O_1 = FermionOperator()
print(O_1)

print("\n((2,0), ) -> a_2:")
O_2 = FermionOperator( ((2, 0), )  )
print(O_2)

print("\n((4,1),(9,0)) -> a^dagger_4a_9:")
O_3 = FermionOperator( ((4, 1), (9, 0))  )
print(O_3)

print("\n((4,1),(3,0),(9,0),(3,1)) -> a^dagger_4a_3a_9a^dagger_3:")
O_4 = FermionOperator( ((4, 1), (9, 0), (3, 1) ) )
print(O_4)










