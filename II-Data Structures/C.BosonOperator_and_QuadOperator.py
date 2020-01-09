# C. BosonOperator and QuadOperator

from openfermion.ops import BosonOperator, QuadOperator

print("Bosonic Operator b^3b5b^1b4, note ordering:")
O = BosonOperator('3^ 5 1^ 4')
print(O)

print("\nNormal ordering of bosonic operator b0b^0 = I + b^0b0:")
from openfermion.utils import normal_ordered
NOP = normal_ordered(BosonOperator('0 0^'))
print(NOP)


print("\nQuadrature Operators: \nQO = ")
QO = QuadOperator('q0 p1 q3')
print(QO)
QON = normal_ordered(QuadOperator('p0 q0'), hbar = 2)
print("\nNormal ordering:")
print(QON)

print("\nTransformation between Boson and Quad operators:")
from openfermion.transforms import get_quad_operator, get_boson_operator
O2 = get_boson_operator(QO, hbar = 2)
print("\nTrasnforming from quadOp QO to a bosonic operator:")
print(O2)
