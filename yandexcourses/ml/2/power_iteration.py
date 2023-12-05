import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    n = data.shape[0]
    r = np.ones((n, 1))
    a = data
    for k in range(num_steps):
        ar = a.dot(r)
        r = ar / np.linalg.norm(ar)
        mu = (r.T.dot(a.dot(r)) / r.T.dot(r))[0, 0]
        if np.array_equal(a.dot(r), mu * r):
            break
    return (float(mu), r.T[0])