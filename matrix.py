def determinant(self):
    """
    Calculates the determinant of a 1x1 or 2x2 matrix.
    """
    if not self.is_square():
        raise(ValueError, "Cannot calculate determinant of non-square matrix.")
    if self.h > 2:
        raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

    # TODO - your code here
    if self.h == 1:
        return self.g[0][0] # a 1x1 matrix
    else:
        return ((self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0])) # a 2x2 matrix
    # TODO - your code here

def trace(self):
    """
    Calculates the trace of a matrix (sum of diagonal entries).
    """
    if not self.is_square():
        raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

    # TODO - your code here
    sum = []
    for i in range(self.h):
        for j in range(self.w):
            if i == j:
                sum = sum + self.g[i][j]
    return sum
    # TODO - your code here

def inverse(self):
    """
    Calculates the inverse of a 1x1 or 2x2 Matrix.
    """
    if not self.is_square():
        raise(ValueError, "Non-square Matrix does not have an inverse.")
    if self.h > 2:
        raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

    # TODO - your code here
    if self.h == 1:
        return 1/self.g[0][0]
    else:
        identity_matrix = identity(self.h)
        return (1/determinant(self.g))*((trace(self.g)*identity_matrix)-self.g)
    # TODO - your code here

def T(self):
    """
    Returns a transposed copy of this Matrix.
    """
    # TODO - your code here
    transpose = []
    for col in range(self.w):
        new_row = []
        for row in range(self.h):
            new_row.append(self.g[row][col])
        transpose.append(new_row)
    return transpose
    # TODO - your code here
