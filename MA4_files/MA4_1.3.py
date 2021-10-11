# MA4_1.3
# Same as 1.2 but multiproccessing

from time import perf_counter as pc
import concurrent.futures as future
from math import *
from scipy.special import gamma
import random

##########################################################################################
def one_monte_carlo(n):
    print(f"Performing monte carlo {n}")
    d = 11
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

    #Volume_Exact = (pi**(d/2)/(gamma(d/2 + 1)))*(r**d) # Exact solution
    Volume_Approx = (2**d)*len(in_sphere)/len(coordinates) # Approx solution

    #print(f'Exact Volume       : {Volume_Exact}')
    #print(f'Approx Volume      : {Volume_Approx}')
    
    return Volume_Approx
###############################################################################################


if __name__ == "__main__":
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        parameters = [1_000_000, 1_000_000, 1_000_000, 1_000_000, 1_000_000, 
                      1_000_000, 1_000_000, 1_000_000, 1_000_000, 1_000_000]
        results = ex.map(one_monte_carlo, parameters)
    lst = list(results)
    result = sum(lst)/len(lst)
    print(f'Volume_Approx : {result}')
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

# Serially 10_000_000 = 56.74 seconds (And shit hits the fan quite literally)
# Parallell 10 * 1_000_000 = 21.19 seconds
# Roughly three times as fast