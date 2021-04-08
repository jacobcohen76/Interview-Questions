#include <functional>
#include <iostream>
#include <vector>

void n_queens(int n)
{
    std::vector<bool> cols(n, true);
    std::vector<bool> diags(2 * n - 1, true);
    std::vector<bool> antis(2 * n - 1, true);
    std::vector<std::vector<char>> board(n, std::vector<char>(n, '.'));

    std::function<int(int, int)> diag = [&](int row, int col)
    {
        return n + row - col - 1;
    };

    std::function<int(int, int)> anti = [&](int row, int col)
    {
        return row + col;
    };

    std::function<bool(int, int)> can_put = [&](int row, int col)
    {
        return cols[col] && diags[diag(row, col)] && antis[anti(row, col)];
    };

    std::function<void(int, int)> put_queen = [&](int row, int col)
    {
        cols[col] = false;
        diags[diag(row, col)] = false;
        antis[anti(row, col)] = false;
        board[row][col] = 'Q';
    };

    std::function<void(int, int)> remove_queen = [&](int row, int col)
    {
        cols[col] = true;
        diags[diag(row, col)] = true;
        antis[anti(row, col)] = true;
        board[row][col] = '.';
    };

    std::function<std::string()> format_board = [&]()
    {
        std::string str(2 * n * n, '?');
        int i = -1;
        for (int row = n - 1; row > -1; --row)
        {
            for (int col = 0; col < n; ++col)
            {
                str[++i] = board[row][col];
                str[++i] = (col < n - 1) ? ' ' : '\n';
            }
        }
        return str;
    };

    std::function<void(int, int)> worker = [&](int no_queens, int row)
    {
        if (no_queens)
        {
            for (int col = 0; col < n; ++col)
            {
                if (can_put(row, col))
                {
                    put_queen(row, col);
                    worker(no_queens - 1, row + 1);
                    remove_queen(row, col);
                }
            }
        }
        else
        {
            std::cout << format_board() << '\n';
        }
    };
    worker(n, 0);
}

int main(int argc, char* argv[])
{
    for (size_t i = 1; i < argc; ++i)
    {
        n_queens(std::stoi(argv[i]));
    }
}