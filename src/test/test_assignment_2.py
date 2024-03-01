import sys
from pathlib import Path
import numpy as np

# Add the parent directory to sys.path to import the main module
parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir)
from main.assignment_2 import nevilles_interpolation, newton_coef, newton_forward, hermite_polynomial, cubic_spline_interpolation

def test_functions():
    print("Testing nevilles_interpolation:")
    print(nevilles_interpolation([3.6, 3.8, 3.9], [1.675, 1.436, 1.318], 3.7))

    print("Testing newton_coef:")
    print(newton_coef([7.2, 7.4, 7.5, 7.6], [23.5492, 25.3913, 26.8224, 27.4589]))

    print("Testing newton_forward:")
    print(newton_forward(newton_coef([7.2, 7.4, 7.5, 7.6], [23.5492, 25.3913, 26.8224, 27.4589]), [7.2, 7.4, 7.5, 7.6],  7.3))

    print("Testing hermite_polynomial:")
    print(hermite_polynomial([3.6, 3.8, 3.9], [1.675, 1.436, 1.318], [-1.195, -1.188, -1.182]))

    print("Testing cubic_spline_interpolation:")
    print(cubic_spline_interpolation([2, 5, 8, 10], [3, 5, 7, 9]))

if __name__ == '__main__':
    test_functions()