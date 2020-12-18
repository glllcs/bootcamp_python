class Matrix:

    def __init__(self, arg1, arg2=None):
        if isinstance(arg1, list):
            pre_data = arg1
            pre_shape = arg2
            if not(arg2 is None or (isinstance(arg2, tuple) and
               len(arg2) == 2 and isinstance(arg2[0], int) and
               isinstance(arg2[1], int) and arg2[0] > 0 and arg2[1] > 0)):
                raise TypeError("The second argument must be a tuple of "
                                "positive non-zeros integers (rows,columns)")
        elif isinstance(arg1, tuple) and len(arg1) == 2 and arg2 is None:
            pre_shape = (arg1[0], arg1[1])
            if (pre_shape[0] <= 0 or pre_shape[1] <= 0):
                raise TypeError("The shape must be of positive non-zeros "
                                "integers")
            pre_data = []
            for _ in range(pre_shape[0]):
                line = []
                for _ in range(pre_shape[1]):
                    line.append(0.0)
                pre_data.append(line)
        else:
            raise TypeError("You must initialize the matrix with either:\n"
                            "- the elements of the matrix as a list of lists\n"
                            "- a shape (rows, columns)\n"
                            "- the expected elements and shape")
        columns = len(pre_data[0])
        self.data = []
        for row in range(len(pre_data)):
            if columns != len(pre_data[row]):
                raise TypeError("There aren't the same number of elements "
                                "in every row")
            line = []
            for elem in pre_data[row]:
                try:
                    line.append(float(elem))
                except ValueError:
                    raise ValueError("Every element in matrix must be a "
                                     "number")
            self.data.append(line)
        self.shape = (row+1, columns)
        if pre_shape is not None and (pre_shape[0] != self.shape[0] or
           pre_shape[1] != self.shape[1]):
            raise ValueError(f"The shape given {pre_shape} doesn't match with "
                             f"the result matrix {self.shape}")

    def __str__(self):
        txt = "(Matrix [["
        for line in self.data:
            for elem in line:
                txt += f'{elem}, '
            txt += "\b\b], ["
        txt += "\b\b\b\b]]) "
        return(txt)

    def __repr__(self):
        return self.__str__() + ', shape == ' + str(self.shape)

    def __add__(self, second):
        if isinstance(second, Matrix):
            if self.shape != second.shape:
                raise ValueError("Matrix with differents dimensions can't "
                                 "be added")
            rows = self.shape[0]
            cols = self.shape[1]
            new = Matrix((rows, cols))
            for r in range(rows):
                for c in range(cols):
                    new.data[r][c] = (self.data[r][c] + second.data[r][c])
        else:
            raise ValueError("A matrix can only be added to another matrix")
        return new

    def __radd__(self, second):
        raise ValueError(f"A {type(second)} cannot be added to a matrix")

    def __sub__(self, second):
        if isinstance(second, Matrix):
            return self.__add__(second.__mul__(-1))
        else:
            raise ValueError("A matrix can only be subtracted from another "
                             "matrix")

    def __rsub__(self, second):
        raise ValueError(f"A {type(second)} cannot be subtracted by a matrix")

    def __truediv__(self, second):
        if isinstance(second, (int, float)):
            rows = self.shape[0]
            cols = self.shape[1]
            new = Matrix((rows, cols))
            for r in range(rows):
                for c in range(cols):
                    new.data[r][c] = (self.data[r][c] / second)
        else:
            raise ValueError("A matrix can only be divided by a scalar")
        return new

    def __rtruediv__(self, second):
        raise ValueError(f"A {type(second)} cannot be divided by a matrix")

    def __mul__(self, second):
        if isinstance(second, Matrix):
            if self.shape[1] != second.shape[0]:
                raise ValueError("The number of columns of the first matrix "
                                 "must be equal to the rows of the second "
                                 "matrix/vector")
            rows = self.shape[0]
            cols = second.shape[1]
            new = Matrix((rows, cols))
            for r_1 in range(self.shape[0]):
                for c_2 in range(second.shape[1]):
                    for c_r in range(self.shape[1]):
                        new.data[r_1][c_2] += self.data[r_1][c_r] *\
                                              second.data[c_r][c_2]
        elif isinstance(second, (int, float)):
            rows = self.shape[0]
            cols = self.shape[1]
            new = Matrix((rows, cols))
            for r in range(rows):
                for c in range(cols):
                    new.data[r][c] = (self.data[r][c] * second)
        else:
            raise ValueError("A matrix can only be multiplied by another "
                             "matrix or by a scalar")
        return new

    def __rmul__(self, second):
        if isinstance(second, (int, float)):
            return self.__mul__(second)
        else:
            raise ValueError("A matrix can only be multiplied by another "
                             "matrix or by a scalar")
