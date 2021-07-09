import math
from sympy import symbols, Eq, solve


def solve_for_vars(data , function):
  new_array = []
  for values in data:
    row = [function(values[0]), values[1]]
    print(row)
    new_array.append(row)
  return new_array


a = symbols('a')
b = symbols('b')
y = solve_for_vars([(1,2.4),(2,3.5),(3,4.9),(4.7.2)], lambda x: math.e**(x + a) + (b*x)**0.5 )