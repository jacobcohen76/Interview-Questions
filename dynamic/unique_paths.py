import collections

from typing import List, Tuple

def unique_paths_dynamic(src: Tuple[int, int], dst: Tuple[int, int]) -> int:

    def make_table(src: Tuple[int, int], dst: Tuple[int, int]) -> List[List[int]]:
        src_x, src_y = src
        dst_x, dst_y = dst
        return [[0 for col in range(src_x, dst_x + 1)] for row in range(src_y, dst_y + 1)]

    def in_bounds(table: List[List[int]], x: int, y: int) -> bool:
        return 0 <= y and y < len(table) and 0 <= x and x < len(table[y])
    def left(x: int, y: int) -> Tuple[int, int]:
        return x - 1, y
    def up(x: int, y: int) -> Tuple[int, int]:
        return x, y - 1

    table = make_table(src, dst)
    table[-1][-1] = 1
    fringe = collections.deque([(len(table[-1]) - 1, len(table) - 1)])

    while fringe:
        px, py = fringe.popleft()
        ux, uy = up(px, py)
        if in_bounds(table, ux, uy):
            if table[uy][ux] == 0:
                fringe.append((ux, uy))
            table[uy][ux] += table[py][px]
        lx, ly = left(px, py)
        if in_bounds(table, lx, ly):
            if table[ly][lx] == 0:
                fringe.append((lx, ly))
            table[ly][lx] += table[py][px]
    return table[0][0]

def unique_paths_recursive(src: Tuple[int, int], dst: Tuple[int, int]) -> int:
    def worker(x: int, y: int) -> int:
        if (x, y) == src:
            return 1
        elif x < 0 or y < 0:
            return 0
        else:
            return worker(x - 1, y) + worker(x, y - 1)
    return worker(*dst)

print(unique_paths_dynamic((1, 1), (5, 3)))
print(unique_paths_recursive((1, 1), (5, 3)))