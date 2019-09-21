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
    sum = 0.0
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
    inverse = []
    if self.h == 1:
        temp = []
        temp.append(1/self.g[0][0])
        inverse.append(temp)
    else:
        identity_matrix = identity(self.h)
        det_term = 1/self.determinant()
        trace_term = self.trace()
        # implement intermediate scaling step locally
        # trace_x_I = trace_term * identity_matrix
        trace_x_I = []
        for i in range(len(self.g)):
            temp_row = []
            for j in range(len(self.g[i])):
                temp_row.append(trace_term * identity_matrix[i][j])
            trace_x_I.append(temp_row)
        # implement sub-traction locally
        # sub_term = trace_x_I - self.g
        sub_term = []
        for i in range(len(trace_x_I)):
            temp_row = []
            for j in range(len(trace_x_I[i])):
                temp_row.append(trace_x_I[i][j] - self.g[i][j])
            sub_term.append(temp_row)
        # implement final scaling step locally
        # inverse = det_term * sub_term
        inverse = []
        for i in range(len(sub_term)):
            temp_row = []
            for j in range(len(sub_term[i])):
                temp_row.append(det_term * sub_term[i][j])
            inverse.append(temp_row)
    return Matrix(inverse)
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
    return Matrix(transpose)
    # TODO - your code here

def __add__(self,other):
    """
    Defines the behavior of the + operator
    """
    if self.h != other.h or self.w != other.w:
        raise(ValueError, "Matrices can only be added if the dimensions are the same")
    #
    # TODO - your code here
    #
    matrix_sum = []
    for i in range(self.h):
        row = []
        for j in range(self.w):
            row.append(self.g[i][j] + other.g[i][j])
        matrix_sum.append(row)
    return Matrix(matrix_sum)
    # TODO - your code here

def __neg__(self):
    """
    Defines the behavior of - operator (NOT subtraction)

    Example:

    > my_matrix = Matrix([ [1, 2], [3, 4] ])
    > negative  = -my_matrix
    > print(negative)
      -1.0  -2.0
      -3.0  -4.0
    """
    #
    # TODO - your code here
    #
    matrix_neg = []
    for i in range(self.h):
        row = []
        for j in range(self.w):
            row.append(0-self.g[i][j])
        matrix_neg.append(row)
    return Matrix(matrix_neg)
    # TODO - your code here

def __sub__(self, other):
    """
    Defines the behavior of - operator (as subtraction)
    """
    #
    # TODO - your code here
    #
    matrix_sub = []
    for i in range(self.h):
        row = []
        for j in range(self.w):
            row.append(self.g[i][j] - other.g[i][j])
        matrix_sub.append(row)
    return Matrix(matrix_sub)
    # TODO - your code here

# TODO - your code here
# Utility functions for matrix multiplication
def get_row(matrix, row_num):
    return matrix[row_num]
def get_col(matrix, col_num):
    col = []
    for i in range(len(matrix)):
        col.append(matrix[i][col_num])
    return col
def dot_product(row_a, row_b):
    sum = 0
    for i in range(len(row_a)):
        sum = sum + (row_a[i] * row_b[i])
    return sum
# TODO - your code here

def __mul__(self, other):
    """
    Defines the behavior of * operator (matrix multiplication)
    """
    #
    # TODO - your code here
    #
    final_matrix = []
    for i in range(self.h):
        temp_row = []
        for j in range(other.w):
            # take dot-product of row of
            # matrix in 1st arg with col of
            # matrix in 2nd arg
            temp_row.append(dot_product(get_row(self.g, i), get_col(other.g, j)))
        final_matrix.append(temp_row)
    return Matrix(final_matrix)
    # TODO - your code here

def __rmul__(self, other):
    """
    Called when the thing on the left of the * is not a matrix.

    Example:

    > identity = Matrix([ [1,0], [0,1] ])
    > doubled  = 2 * identity
    > print(doubled)
      2.0  0.0
      0.0  2.0
    """
    if isinstance(other, numbers.Number):
        #
        # TODO - your code here
        #
        scaled_matrix = []
        for i in range(self.h):
            temp_row = []
            for j in range(self.w):
                temp_row.append(other * self.g[i][j])
            scaled_matrix.append(temp_row)
        return Matrix(scaled_matrix)
        # TODO - your code here
