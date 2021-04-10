import collections

from typing import List, Tuple

def spiral_traversal(grid: List[List[int]]) -> None:
    def in_bounds(grid: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[row])
    def north(row: int, col: int) -> Tuple[int, int]:
        return row + 1, col
    def east(row: int, col: int) -> Tuple[int, int]:
        return row, col + 1
    def south(row: int, col: int) -> Tuple[int, int]:
        return row - 1, col
    def west(row: int, col: int) -> Tuple[int, int]:
        return row, col - 1
    directions = [east, south, west, north]
    curr_dir = 0

    visited = {(0, 0)}
    fringe = collections.deque([(0, 0)])
    while fringe:
        curr_pos = fringe.popleft()
        next_pos = directions[curr_dir](*curr_pos)
        if next_pos in visited or not in_bounds(grid, *next_pos):
            curr_dir = (curr_dir + 1) % len(directions)
            next_pos = directions[curr_dir](*curr_pos)
        if next_pos not in visited and in_bounds(grid, *next_pos):
            fringe.append(next_pos)
        curr_row, curr_col = curr_pos
        print(grid[curr_row][curr_col])

spiral_traversal([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
