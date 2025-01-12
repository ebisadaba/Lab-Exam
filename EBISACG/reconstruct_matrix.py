import numpy as np

def reconstruct_matrix(U, S, V):
    """
    Reconstruct the original matrix using SVD components.
    Parameters:
        U (numpy.ndarray): Left singular vectors
        S (numpy.ndarray): Singular values
        V (numpy.ndarray): Right singular vectors
    Returns:
        numpy.ndarray: Reconstructed matrix
    """
    S_matrix = np.diag(S)  # Convert S (1D array) into a diagonal matrix
    reconstructed = np.dot(U, np.dot(S_matrix, V))
    return reconstructed

# Example usage:
if name == "main":
    # Original matrix
    A = np.array([[1, 2], [3, 4], [5, 6]])
    print("Original Matrix:")
    print(A)

    # Perform SVD
    U, S, V = np.linalg.svd(A, full_matrices=False)
    print("\nSVD Components:")
    print("U:\n", U)
    print("S:\n", S)
    print("V:\n", V)

    # Reconstruct the matrix
    A_reconstructed = reconstruct_matrix(U, S, V)
    print("\nReconstructed Matrix:")
    print(A_reconstructed)