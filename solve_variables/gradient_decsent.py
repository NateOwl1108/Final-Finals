import math
from sympy import symbols, Eq, solve

def create_array(data, function, constants):
  new_array = []
  for values in data:
    row = [function(values[0], constants[0], constants[1])]
    new_array.append(row)
  return new_array

def calc_gradient(self, data,function): 
    #- computes the partial derivatives of the RSS with respect to each coefficients
    for row in data:

      
    return central_differences

def solve_for_vars(data , function, initial):
  prediction = create_array(data,function,initial)
  if 
  


a = symbols('a')
b = symbols('b')
y = solve_for_vars([(1,2.4),(2,3.5),(3,4.9),(4.7.2)], lambda x,a,b: math.e**(x + a) + (b*x)**0.5, (-1,3) )