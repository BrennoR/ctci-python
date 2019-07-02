# Eight Queens
# TODO: Optimize solution


class Solution:

    def __init__(self):
        self.sol_list = []
        self.count = 0

    def eight_queens(self):
        row = 0
        no_set = set()
        sol_set = set()
        self.queens_recurse(row, no_set, sol_set)
        return self.sol_list

    def queens_recurse(self, row, no_set, sol_set):
        if row < 8:
            for col in range(8):
                no_set_copy = no_set.copy()
                sol_set_copy = sol_set.copy()
                if (row, col) not in no_set_copy:
                    sol_set_copy.add((row, col))
                    for n in range(8):
                        no_set_copy.add((row, n))
                        no_set_copy.add((n, col))
                    dpu, dpd, dnu, dnd = (row - 1, col + 1), (row + 1, col + 1), (row - 1, col - 1), (row + 1, col - 1)
                    for d, z in zip((dpu, dpd, dnu, dnd), ((-1, 1), (1, 1), (-1, -1), (1, -1))):
                        i = d[0]
                        j = d[1]
                        while 0 <= i < 8 and 0 <= j < 8:
                            no_set_copy.add((i, j))
                            i += z[0]
                            j += z[1]
                    if row == 7 and len(sol_set_copy) == 8:
                        self.sol_list.append(sol_set_copy)
                    self.queens_recurse(row + 1, no_set_copy, sol_set_copy)

    def visualize_queens(self):
        board_list = []
        for sol in self.sol_list:
            board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

            for r, c in sol:
                board[r][c] = 'O'

            board_list.append(board)

        for board in board_list:
            print('=' * 50)
            for row in board:
                print(row)


if __name__ == '__main__':
    queens = Solution()
    queens_list = queens.eight_queens()
    queens.visualize_queens()
