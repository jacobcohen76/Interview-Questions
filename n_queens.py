import copy

from typing import List

def n_queens(n: int) -> int:
    def make_board(n: int) -> List[List[str]]:
            return [['.'] * n for i in range(n)]
        
    def diag(row: int, col: int) -> int:
        return n - 1 + row - col
    
    def anti(row: int, col: int) -> int:
        return row + col
    
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
        
    def can_put_queen(row: int, col: int) -> bool:
        return cols[col] and diags[diag(row, col)] and antis[anti(row, col)]
    
    def worker(no_queens: int, row: int) -> None:
        if no_queens:
            for col in range(n):
                if can_put_queen(row, col):
                    put_queen(row, col)
                    worker(no_queens - 1, row + 1)
                    remove_queen(row, col)
        else:
            for row in board:
                print(' '.join(row))
            print()
            # solutions.append([''.join(board_row) for board_row in board])

    cols = [True] * n
    diags = [True] * (2 * n - 1)
    antis = [True] * (2 * n - 1)
    board = make_board(n)
    solutions = []
    worker(n, 0)
    
    for board in solutions:
        for row in board:
            print(' '.join(row))
        print()
    
    return solutions


n_queens(15)