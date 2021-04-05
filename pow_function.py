# https://leetcode.com/problems/powx-n/

# https://en.wikipedia.org/wiki/Exponentiation_by_squaring
# b ** n = b * (b ** 2) ** ((n - 1) / 2) if n is odd
#              (b ** 2) ** (n / 2)       else

def pow_recursive(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        return pow_recursive(1.0 / x, -n)
    elif n & 1:
        return pow_recursive(x * x, n // 2) * x
    else:
        return pow_recursive(x * x, n // 2)

def pow_iterative(x: float, n: int) -> float:
    res = 1.0
    if n < 0:
        x = 1.0 / x
        n = -n
    while n:
        if n & 1:
            res *= x
        x *= x
        n //= 2
    return res

test_pow_recursive = lambda x, n: print('pow_recursive(%f, %i) = %f' % (x, n, pow_recursive(x, n)))
test_pow_iterative = lambda x, n: print('pow_iterative(%f, %i) = %f' % (x, n, pow_iterative(x, n)))

test_pow_recursive(2.0, -2)
test_pow_iterative(2.0, -2)