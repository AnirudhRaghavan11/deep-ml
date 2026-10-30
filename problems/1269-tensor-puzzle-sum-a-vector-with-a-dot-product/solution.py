import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    array1 = np.ones(a.size)

    return np.dot(array1, a)
