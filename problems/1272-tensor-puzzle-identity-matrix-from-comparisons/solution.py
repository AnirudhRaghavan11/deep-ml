import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    rows = np.arange(n)[:,None] #so here, this means it's the shape (n,1)
    cols = np.arange(n)[None,:] #so here, this is the shape, (1,n)
    return (rows==cols).astype(np.float64)
