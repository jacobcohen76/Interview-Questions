import copy
import itertools
import sys

from typing import List

def n_queens(n: int) -> int:

    def make_board(n: int) -> List[List[str]]:
        return [['.'] * n for i in range(n)]
    
    def format_board(board: List[List[str]]) -> str:
        return '\n'.join(' '.join(row) for row in reversed(board))
        
    def diag(row: int, col: int) -> int:
        return n + row - col - 1
    
    def anti(row: int, col: int) -> int:
        return row + col

    def can_put(row: int, col: int) -> bool:
        return cols[col] and diags[diag(row, col)] and antis[anti(row, col)]

    def put_queen(row: int, col: int) -> None:
        cols[col] = False
        diags[diag(row, col)] = False
        antis[anti(row, col)] = False
        board[row][col] = 'Q'
        
    def remove_queen(row: int, col: int) -> None:
        cols[col] = True
        diags[diag(row, col)] = True
        antis[anti(row, col)] = True
        board[row][col] = '.'
    
    def worker(no_queens: int, row: int) -> None:
        if no_queens:
            for col in range(n):
                if can_put(row, col):
                    put_queen(row, col)
                    worker(no_queens - 1, row + 1)
                    remove_queen(row, col)
        else:
            print('Solution #%i:\n%s' % (next(sol_count) + 1, format_board(board)))

    cols = [True] * n
    diags = [True] * (2 * n - 1)
    antis = [True] * (2 * n - 1)
    board = make_board(n)
    sol_count = itertools.count()
    worker(n, 0)
    return next(sol_count)

if __name__ == '__main__':
    for arg in sys.argv:
        if arg.isdigit():
            print('n_queens(%s) = %i' % (arg, n_queens(int(arg))))