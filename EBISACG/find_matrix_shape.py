def find_matrix_shape(matrix):
    """
    Find the shape of a matrix.
    Parameters:
        matrix (list of lists): A 2D list representing the matrix
    Returns:
        tuple: A tuple (rows, columns) representing the matrix shape
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows, cols

# Example usage
if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matrix:")
    for row in matrix:
        print(row)

    shape = find_matrix_shape(matrix)
    print(f"\nShape of the matrix: {shape}")
