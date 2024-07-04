import numpy as np
import sys
sys.path.append('C:\Users\jorda\Documents\studies\DScourse\Math\LinearAlgebra')
from Math.LinearAlgebra.vector_multiplication_proof import vector_vector_product


def main():

    def vector_norm(v: np.array) -> np.array:
        v_norm = np.sqrt(sum(v.apply(lambda d: d**2)))
        return v_norm

    v = np.array([1, 2, 3])

    print(vector_norm(v))

    # def calculate_angle_between_vectors(v: np.array, u: np.array) -> float:
    # Normalize vectors
