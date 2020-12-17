from matrix import Matrix

m1 = Matrix([[0,1,2,3], [0,2,4,6]])
# merror = Matrix([[0,1,2], [0,2,4,6]])
# merror = Matrix([[0,1,'a'], [0,2,4,6]])
m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]], (4,2))
# merror = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]], (8,2))
m3 = Matrix((4,7))
# merror = Matrix(2)
# merror = Matrix((1, 0))
m4 = Matrix([[10,20,30,40], [-10,-20,-30,-40]])

#print(m2.__repr__())

print(m1)
print(m4)
print(m1+m4)
print(m1-m4)