import numpy as np
import timeit as ti


def matmul(a, b, block_size):
    n = len(a)
    c = np.zeros((n, n))

    for i0 in range(0, n, block_size):
        for j0 in range(0, n, block_size):
            for k0 in range(0, n, block_size):
                # block matrix multiplication
                for i in range(i0, min(i0 + block_size, n)):
                    for j in range(j0, min(j0 + block_size, n)):
                        for k in range(k0, min(k0 + block_size, n)):
                            c[i, j] += a[i, k] * b[k, j]

    return c


def matmul_optimized(a, b, block_size):
    n = len(a)
    i = n//block_size
    c = np.zeros((n, n))

    for i0, j0, k0 in np.ndindex(i, i, i):
        i0 *= block_size
        j0 *= block_size
        k0 *= block_size
        # block matrix multiplication
        for i in range(i0, min(i0 + block_size, n)):
            for j in range(j0, min(j0 + block_size, n)):
                for k in range(k0, min(k0 + block_size, n)):
                    c[i, j] += a[i, k] * b[k, j]

    return c


if __name__ == '__main__':
    for n in [2**x for x in range(7, 10)]:
        A = np.random.randint(100, size=(n, n))
        B = np.random.randint(100, size=(n, n))
        for block_size in [2**x for x in range(0, 9)]:
            t = ti.timeit(lambda: matmul(A, B, block_size), number=1)
            print(f'{n},{block_size},{t}')
