from merge_sort import merge_sort
from merge import merge
import numpy as np
import sys
import time
import multiprocessing
np.set_printoptions(threshold=np.inf)

def parallel_merge_sort(subarray, left_index, right_index):
    merge_sort(subarray, left_index, right_index - 1)
    return subarray

if __name__=='__main__':
    n_elements = int(sys.argv[1])
    max_value = int(sys.argv[2])
    left_index = 0
    right_index = n_elements

    A = np.random.randint(0, max_value, n_elements)
    A1 = A[:A.shape[0] // 2]
    A2 = A[A.shape[0] // 2:]

    A3 = A[:A.shape[0] // 4]
    A4 = A[A.shape[0] // 4:A.shape[0] // 2]
    A5 = A[A.shape[0] // 2: 3 * A.shape[0] // 4]
    A6 = A[3 * (A.shape[0] // 4):]



    # Running on a single process
    start = time.time()
    merge_sort(A, left_index, right_index - 1)
    end = time.time()
    print(f'Execution time with one process: {end - start}')


    # Running on two processes
    pool = multiprocessing.Pool(processes=2)

    start = time.time()
    result1 = pool.apply_async(parallel_merge_sort, (A1, left_index, A1.shape[0]))
    result2 = pool.apply_async(parallel_merge_sort, (A2, left_index, A2.shape[0]))

    A1_sorted = result1.get()
    A2_sorted = result2.get()

    B = np.concatenate((A1_sorted, A2_sorted))
    merge(B, left_index, A.shape[0] // 2, right_index - 1)
    end = time.time()
    print(f'Execution time with two process: {end - start}')



    # Running on four processes

    pool = multiprocessing.Pool(processes=4)

    start = time.time()
    result3 = pool.apply_async(parallel_merge_sort, (A3, left_index, A3.shape[0]))
    result4 = pool.apply_async(parallel_merge_sort, (A4, left_index, A4.shape[0]))
    result5 = pool.apply_async(parallel_merge_sort, (A5, left_index, A5.shape[0]))
    result6 = pool.apply_async(parallel_merge_sort, (A6, left_index, A6.shape[0]))

    A3_sorted = result3.get()
    A4_sorted = result4.get()
    A5_sorted = result5.get()
    A6_sorted = result6.get()


    C1 = np.concatenate((A3_sorted, A4_sorted))
    C2 = np.concatenate((A5_sorted, A6_sorted))
    merge(C1, left_index, C1.shape[0] // 2, right_index//2 - 1)
    merge(C2, left_index, C2.shape[0] // 2, right_index//2 - 1)

    C = np.concatenate((C1, C2))
    merge(C, left_index, C.shape[0] // 2, right_index - 1)

    end = time.time()
    print(f'Execution time with four process: {end - start}')
