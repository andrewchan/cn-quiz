from itertools import count
import math

def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next cube is evenly
    divisible by provided argument (reminder of the division of the cube
    and the argument is zero).
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    
    if not modulus:
        return []

    if modulus == 0 or modulus == 1:
        return []

    if type(modulus) not in [int, long, float]:
        return []
    
    if math.isnan(modulus):
        return []

    result = []
    for i in count(1):
        cube = i**3
        if cube % modulus != 0:
            result.append(cube)
        else:
            break
    return result

    
    
