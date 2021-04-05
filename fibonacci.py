import numpy as np

# O(log n)
def fib_matrix(n: int) -> int:
    mat = np.array([[1, 1],
                    [1, 0]], int)
    res = np.identity(2, int)
    while n:
        if n & 1:
            res = mat @ res
        mat = mat @ mat
        n //= 2
    return res[0][1]

# O(n)
def fib_dynamic(n: int) -> int:
    table = [1] * n
    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]
    return table[-1]

# O(2^n)
def fib_recursive(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

n = 42
print(fib_matrix(n))
print(fib_dynamic(n))
print(fib_recursive(n))