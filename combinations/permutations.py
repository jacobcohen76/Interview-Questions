from typing import Any, List

def permutations(pool: List[Any]):
    def swap(i: int, j: int) -> None:
        pool[i], pool[j] = pool[j], pool[i]
    def worker(i: int, n: int):
        if i + 1 == n:
            print(pool)
        else:
            for j in range(i, n):
                swap(i, j)
                worker(i + 1, n)
                swap(j, i)
    return worker(0, len(pool))

permutations([1, 2, 3])
