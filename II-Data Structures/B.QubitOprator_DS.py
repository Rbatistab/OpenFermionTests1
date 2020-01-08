# B. QubitOperator DS
from openfermion.ops import QubitOperator

print("O = Z1Z2 + X1 + X2:")
O = QubitOperator('Z1 Z2') + QubitOperator('X1') + QubitOperator('X2')
print(O)

print("\nTake (O in {X,Y,Z}, i in N_0) -> O_i:")
print("\nAs hash:")
O = QubitOperator( ((1, 'X'), (2, 'X')) )
print(O)

print("\nAs string rep:")
O = QubitOperator('X1 X2')
print(O)
