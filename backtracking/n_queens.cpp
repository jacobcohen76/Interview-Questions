#include <functional>
#include <iostream>
#include <string>
#include <vector>

std::string FormatBoard(uint64_t n, const std::vector<std::string>& board)
{
    std::string formatted(2 * n * n, 0);
    size_t i = -1;
    for (uint64_t row = n - 1; row != -1; --row)
    {
        for (char ch : board[row])
        {
            formatted[++i] = ch;
            formatted[++i] = ' ';
        }
        formatted[i - 1] = '\n';
    }
    return formatted;
}

constexpr uint64_t Diag(uint64_t n, uint64_t row, uint64_t col)
{
    return n + row - col - 1;
}

constexpr uint64_t Anti(uint64_t n, uint64_t row, uint64_t col)
{
    return row + col;
}

void n_queens(int n)
{
    std::vector<bool> cols(n, true);
    std::vector<bool> diags(2 * n - 1, true);
    std::vector<bool> antis(2 * n - 1, true);
    std::vector<std::string> board(n, std::string(n, '.'));

    std::function<bool(uint64_t, uint64_t)> can_put = [&](uint64_t row, uint64_t col)
    {
        return cols[col] && diags[Diag(n, row, col)] && antis[Anti(n, row, col)];
    };
    std::function<void(uint64_t, uint64_t)> put_queen = [&](uint64_t row, uint64_t col)
    {
        cols[col] = false;
        diags[Diag(n, row, col)] = false;
        antis[Anti(n, row, col)] = false;
        board[row][col] = 'Q';
    };
    std::function<void(uint64_t, uint64_t)> remove_queen = [&](uint64_t row, uint64_t col)
    {
        cols[col] = true;
        diags[Diag(n, row, col)] = true;
        antis[Anti(n, row, col)] = true;
        board[row][col] = '.';
    };
    std::function<void(uint64_t, uint64_t)> worker = [&](uint64_t no_queens, uint64_t row)
    {
        if (no_queens)
        {
            for (uint64_t col = 0; col < n; ++col)
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
            std::cout << FormatBoard(n, board) << std::endl;
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