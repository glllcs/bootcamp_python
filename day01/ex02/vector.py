class Vector:

    def __init__(self, argument):
        if isinstance(argument, list):
            v = argument
        elif isinstance(argument, int):
            v = list(range(argument))
        elif isinstance(argument, tuple) and len(argument) == 2:
            v = list(range(argument[0], argument[1]))
        else:
            raise ("Argument not valid")
        self.values = []
        for i in v:
            self.values.append(float(i))
        self.size = len(self.values)

    def __str__(self):
        txt = "(Vector [ "
        for elem in self.values:
            txt += f'{elem}, '
        txt += "\b\b ])"
        return(txt)

    def __repr__(self):
        return self.__str__() + ', size == ' + str(self.size)

    def __add__(self, second):
        if isinstance(second, (int, float)):
            new = [x + second for x in self.values]
        elif isinstance(second, Vector):
            if self.size != second.size:
                raise ValueError("Vectors don't have same dimension")
            new = []
            for i in range(self.size):
                new.append(self.values[i] + second.values[i])
        else:
            raise ValueError("A vector can only be added to another "
                             "vector or to a scalar")
        return Vector(new)

    def __radd__(self, second):
        return self.__add__(second)

    def __sub__(self, second):
        if isinstance(second, (int, float)):
            new = [x - second for x in self.values]
        elif isinstance(second, Vector):
            if self.size != second.size:
                raise ValueError("Vectors don't have same dimension")
            new = []
            for i in range(self.size):
                new.append(self.values[i] - second.values[i])
        else:
            raise ValueError("A vector can only be subtracted from another "
                             "vector or from a scalar")
        return Vector(new)

    def __rsub__(self, second):
        if isinstance(second, (int, float)):
            new = [second - x for x in self.values]
            return Vector(new)
        else:
            raise ValueError("A vector can only be subtracted from another "
                             "vector or a scalar")

    def __truediv__(self, second):
        if not isinstance(second, (int, float)):
            raise ValueError("A vector can only be divided by a scalar")
        new = [x / second for x in self.values]
        return Vector(new)

    def __rtruediv__(self, second):
        raise ValueError(f"A {type(second)} cannot be divided by a vector")

    def __mul__(self, second):
        if isinstance(second, (int, float)):
            new = [x * second for x in self.values]
            return Vector(new)
        elif isinstance(second, Vector):
            if self.size != second.size:
                raise ValueError("Vectors don't have same dimension")
            new = 0
            for i in range(self.size):
                new += (self.values[i] * second.values[i])
            return (new)
        else:
            raise ValueError("A vector can only be multiplicated by a scalar "
                             "or by another vector (dot product)")

    def __rmul__(self, second):
        return self.__mul__(second)
