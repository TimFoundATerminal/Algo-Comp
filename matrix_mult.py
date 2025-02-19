import numpy as np

def strassens_matrix_mult(a: np.array, b: np.array) -> np.array:
    """Strassens matrix multiplication algorithm"""

    n = len(a)
    # check n is a power of 2
    if n & (n - 1) != 0 and n != 0:
        raise ValueError("Matrix dimensions must be a power of 2")

    # Base cases
    if n == 1:
        return a * b
    
    # split the matrix into 4 quadrants
    a11, b11 = a[:n//2, :n//2], b[:n//2, :n//2]
    a12, b12 = a[:n//2, n//2:], b[:n//2, n//2:]
    a21, b21 = a[n//2:, :n//2], b[n//2:, :n//2]
    a22, b22 = a[n//2:, n//2:], b[n//2:, n//2:] 

    # calculate the 7 products
    M1 = strassens_matrix_mult(a11 + a22, b11 + b22)
    M2 = strassens_matrix_mult(a21 + a22, b11)
    M3 = strassens_matrix_mult(a11, b12 - b22)
    M4 = strassens_matrix_mult(a22, b21 - b11)
    M5 = strassens_matrix_mult(a11 + a12, b22)
    M6 = strassens_matrix_mult(a21 - a11, b11 + b12)
    M7 = strassens_matrix_mult(a12 - a22, b21 + b22)
    c11 = M1 + M4 - M5 + M7
    c12 = M3 + M5
    c21 = M2 + M4
    c22 = M1 - M2 + M3 + M6

    # combine the results
    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

def main():
    a = np.array([
        [1, 2], 
        [3, 4]
    ])
    b = np.array([
        [5, 6], 
        [7, 8]
    ])
    c = strassens_matrix_mult(a, b)
    
    print("Matrix a: \n", a)
    print("Matrix b: \n", b)
    print("Matrix c: \n", c)
    print("Matrix Answer: \n", np.matmul(a, b))
    print("Matrix multiplication successful")

if __name__ == "__main__":
    main()
