import math
import numpy as np

from typing import Tuple

# O(1)
def fib_binet(n: int) -> int:
    sqrt_5 = math.sqrt(5)
    term_1 = math.pow((1.0 + sqrt_5) / 2.0, n)
    term_2 = math.pow((1.0 - sqrt_5) / 2.0, n)
    return (term_1 - term_2) / sqrt_5

# O(log n)
def fib_matrix(n: int) -> int:
    def matrix_power(
            m11: int, m12: int,
            m21: int, m22: int, n: int
        ) -> Tuple[int, int, int, int]:
        r11, r12 = 1, 0
        r21, r22 = 0, 1
        while n:
            if n & 1:
                r11, r12, \
                r21, r22, = r11 * m11 + r12 * m21, r11 * m12 + r12 * m22, \
                            r21 * m11 + r22 * m21, r21 * m12 + r22 * m22,
            m11, m12, \
            m21, m22, = m11 * m11 + m12 * m21, m11 * m12 + m12 * m22, \
                        m21 * m11 + m22 * m21, m21 * m12 + m22 * m22,
            n //= 2
        return r11, r12, \
               r21, r22,
    return matrix_power(1, 1,
                        1, 0, n)[2]

# O(log n)
def fib_matrix_np(n: int) -> int:
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
print(fib_binet(n))
print(fib_matrix(n))
print(fib_matrix_np(n))
print(fib_dynamic(n))
print(fib_recursive(n))