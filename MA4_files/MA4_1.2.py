# MA4_1.2
# Niklas Eckert Elfving

from math import *
from scipy.special import gamma
import random
from time import perf_counter

start = perf_counter()
# Parameters
d = 11 #(input('Give number of dimensions: '))
n = 10_000_000 #int(input('Give number of points: '))
r = 1


# lambda funktion that creates a coordinate with list comprehension
coordinate = lambda dim : [random.uniform(-1, 1) for i in range(dim)]

# Checks if a coordinate is in sphere, if it is coordinate returned
def is_in_sphere(coordinate):
    value = 0
    for i in range(0, len(coordinate)):
        value += coordinate[i]**2
    if value <= 1:
        return True
    else:
        return False 

coordinates = [coordinate(d) for i in range(n)] # make coordinates
in_sphere = list(filter(is_in_sphere, coordinates)) # coordinates in sphere, filter used

Volume_Exact = (pi**(d/2)/(gamma(d/2 + 1)))*(r**d) # Exact solution
Volume_Approx = (2**d)*len(in_sphere)/len(coordinates) # Approx solution

print(f'Exact Volume       : {Volume_Exact}')
print(f'Approx Volume      : {Volume_Approx}')

end = perf_counter()

print(f'Programme ran for {end-start} seconds')



