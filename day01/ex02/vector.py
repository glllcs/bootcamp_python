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
        txt = "[ "
        for elem in self.values:
            txt += f'{elem}, '
        txt += "\b\b ]"
        return(txt)
    
    def __add__(self, second):
        """Addition between two vectors of same dimension (m * 1)"""
        if (self.size != second.size):
            raise ("vectors dont't have same dimension")
        new = []
        for i in range(self.size):
            new.append(self.values[i] + second.values[i])
        return Vector(new)
            
