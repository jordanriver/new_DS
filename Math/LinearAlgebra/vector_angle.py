import numpy as np


def main():

    def calculate_vector_angle(v: np.array) -> float:
        """Calculate the angle of a vector in degrees

        Args:
            v (np.array): a 2D vector

        Returns:
            float: the angle of the vector in degrees
        """
        # calculate vector angle in radians
        rads = np.arctan2(v[0], v[1])

        # Convert radians to degrees
        angle = round(rads * 180 / np.pi, 2)

        return angle


if __name__ == "__main__":
    main()
