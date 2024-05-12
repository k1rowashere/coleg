import numpy as np
import matplotlib.pyplot as plt
import timeit as ti
import sys


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


if __name__ == '__main__':
    print('start')
    sys.stdout.flush()

    graph_data = []
    N = [2**x for x in range(1, 10)]
    BLOCK_SIZE = [2**x for x in range(3, 7)]

    for n in N:
        A = np.random.randint(100, size=(n, n))
        B = np.random.randint(100, size=(n, n))

        col = []
        for block_size in BLOCK_SIZE:
            t = ti.timeit(lambda: matmul(A, B, block_size), number=1)

            print(f'{n},{block_size},{t}')
            sys.stdout.flush()

            col.append(t)
        graph_data.append(col)

    # line plot using matplotlib (each block size is a different line)
    transposed = np.array(graph_data).T

    for block_size, row in zip(BLOCK_SIZE, transposed):
        plt.plot(N, row, label=f'block size = {block_size}')

    plt.xscale('log', basex=2)
    plt.xlabel('Matrix size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()
