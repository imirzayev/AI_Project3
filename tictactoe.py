class TicTacToe:
    def __init__(self, board_size, target) -> None:
        self.board_size = board_size
        self.board = [[0 for col in range(board_size)] for row in range(board_size)]
        self.target = target

    def get_possible_moves(self):
        """Getting the coordinates of available moves"""
        availables = []
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 0:
                    availables.append((i, j))
        return availables

    def win_check(self, last):
        """Check whether win happened based on last move"""

        player = 0
        if self.board[last[0]][last[1]] == 1:
            player = 1
        elif self.board[last[0]][last[1]] == -1:
            player = -1

        winner = 0
        if player == 1:
            winner = 0
        else:
            winner = 1

        vertical_cnt = 0
        for row in self.board:
            if row[last[1]] == player:
                vertical_cnt += 1
                if vertical_cnt == self.target:
                    return True, winner
            else:
                vertical_cnt = 0

        horizontal_cnt = 0
        for x in self.board[last[0]]:
            if x == player:
                horizontal_cnt += 1
                if horizontal_cnt == self.target:
                    return True, winner
            else:
                horizontal_cnt = 0

        diagonal_1_cnt = 0
        i, j = last[0], last[1]
        while i < self.board_size and j < self.board_size:
            if self.board[i][j] == player:
                diagonal_1_cnt += 1
                if diagonal_1_cnt == self.target:
                    return True, winner
            else:
                diagonal_1_cnt = 0
            i += 1
            j += 1

        diagonal_2_cnt = 0
        i, j = last[0], last[1]
        while i >= 0 and j >= 0:
            if self.board[i][j] == player:
                diagonal_2_cnt += 1
                if diagonal_2_cnt == self.target:
                    return True, winner
            else:
                diagonal_2_cnt = 0
            i -= 1
            j -= 1

        diagonal_3_cnt = 0
        i, j = last[0], last[1]
        while i >= 0 and j < self.board_size:
            if self.board[i][j] == player:
                diagonal_3_cnt += 1
                if diagonal_3_cnt == self.target:
                    return True, winner
            else:
                diagonal_3_cnt = 0
            i -= 1
            j += 1

        diagonal_4_cnt = 0
        i, j = last[0], last[1]
        while i < self.board_size and j >= 0:
            if self.board[i][j] == player:
                diagonal_4_cnt += 1
                if diagonal_4_cnt == self.target:
                    return True, winner
            else:
                diagonal_4_cnt = 0
            i += 1
            j -= 1

        if self.filled():
            return False, 2
        return False, -1

    def filled(self):
        """Check whether the board is filled"""
        return all(all(v != 0 for v in row) for row in self.board)

    def empty(self):
        """Check whether the board is empty"""
        return all(all(v == 0 for v in row) for row in self.board)

    def mark_coordinate(self, coordinate, char):
        """Updating the array with given character located at given coordinate"""
        self.board[coordinate[0]][coordinate[1]] = char

    def reset_coordinate(self, coordinate):
        """Removing the character from the given coordinate"""
        self.board[coordinate[0]][coordinate[1]] = 0

    def __str__(self) -> str:
        st = ''
        for row in self.board:
            for x in row:
                st += str(x)
                st += ' '
            st += '\n'
        return st
