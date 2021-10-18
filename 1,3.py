pip show numpy

A = np.random.radint(0, 10, size=(4,5))
print(A)
A[1], A[3] = A[3], A[1]
print('New A:')
print(A)