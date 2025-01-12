import numpy as np

def compute_cross_product(array1, array2):
    """
    Returns the cross product of two arrays.
    """
    return np.cross(array1, array2)

# Example usage
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(compute_cross_product(arr1, arr2)) 