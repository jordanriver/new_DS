import numpy as np


def main():
    # Define two vectors
    v1 = np.array([1, 2])
    v2 = np.array([2, 3])

    # Calculate the vector product of a vector and a scalar
    def vector_scalar_product(v: np.array, s: int) -> np.array:
        """Calculate the product of a vector and a scalar

        Args:
            v (np.array): a 2D vector
            s (int): a scalar

        Returns:
            np.array: the product of the vector and the scalar
        """
        return v * s

    def vector_vector_product(v1: np.array, v2: np.array) -> int:
        """Calculate the product of two vectors

        Args:
            v1 (np.array): a 2D vector
            v2 (np.array): a 2D vector

        Returns:
            int: the product of the two vectors
        """
        return np.dot(v1, v2)


if __name__ == "__main__":
    main()
