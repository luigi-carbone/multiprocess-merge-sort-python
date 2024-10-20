import numpy
import numpy as np

def merge(A, p, q, r):

    n1 = q - p + 1
    n2 = r - q

    L = np.zeros(n1 + 1)
    R = np.zeros(n2 + 1)

    L[:n1] = A[p:p + n1]
    R[:n2] = A[q+1:q+1+n2]

    L[n1] = numpy.inf
    R[n2] = numpy.inf

    i = 0
    j = 0
    for k in range(p, r+1):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
