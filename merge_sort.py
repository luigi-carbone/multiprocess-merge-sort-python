from merge import merge
import numpy as np


def merge_sort(A, p, r):
    if (p < r):
        q = np.floor((p+r)/2).astype(int)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

