from tictactoe import TicTacToe
import config


def find_max(val1, val2, p1, p2):
    if val2 > val1:
        return val2, p2
    else:
        return val1, p1


def find_min(val1, val2, p1, p2):
    if val2 < val1:
        return val2, p2
    else:
        return val1, p1


def minimax(game, depth, maximizer, point=None, alpha=float("-inf"), beta=float("inf")):
    """Minimax algorithm for adversarial search using alpha beta pruning"""

    # Initially the point is empty, and it is initialized with 0,0 tuple
    if point:
        game.mark_coordinate((point[0], point[1]), 1 if maximizer else -1)
    else:
        point = (0, 0)

    # Max depth reached
    if depth == 0 or game.filled():
        return heuristic(game, point), point

    # Interchangeably apply minimize and maximize operations
    if maximizer:
        value = float("-inf")
        for coordinate in game.get_possible_moves():
            value, point = find_max(value, minimax(game, depth - 1, maximizer, (coordinate[0], coordinate[1]),
                                                   alpha, beta)[0], point, tuple(coordinate))
            alpha = max(value, alpha)
            game.reset_coordinate((coordinate[0], coordinate[1]))

        return value, point

    # minimizer turn
    else:
        value = float("inf")
        for coordinate in game.get_possible_moves():
            value, point = find_max(value, minimax(game, depth - 1, not maximizer, (coordinate[0], coordinate[1]),
                                                   alpha, beta)[0], point, tuple(coordinate))
            beta = max(value, beta)
            game.reset_coordinate((coordinate[0], coordinate[1]))

        return value, point


def heuristic(game, last):
    """The heuristic to evaluate the possible options"""
    # Based on the last movement, decide whose turn

    char_turn = 0
    if game.board[last[0]][last[1]] == 1:
        char_turn = 1
    elif game.board[last[0]][last[1]] == -1:
        char_turn = -1

    max_util = 0
    factor = 0
    checked_char = 1

    # Checking consecutive characters with 1 in vertical, horizontal and diagonal manner
    start_point = [last[0] - (game.target - 1), last[1]]
    for i in range(game.target):
        if 0 <= start_point[0] <= last[0]:
            utility = 0
            if start_point[0] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0] + j][start_point[1]] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility = 0
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] += 1

    start_point = [last[0], last[1] - (game.target - 1)]
    for i in range(game.target):
        if 0 <= start_point[1] <= last[1]:
            utility = 0
            if start_point[1] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0]][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[1] += 1

    start_point = [last[0] - (game.target - 1), last[1] - (game.target - 1)]
    for i in range(game.target):
        if 0 <= start_point[0] <= last[0] and 0 <= start_point[1] <= last[1]:
            utility = 0
            if (start_point[0] + (game.target - 1) < len(game.board) and start_point[1] + (game.target - 1) < len(
                    game.board)):
                for j in range(game.target):
                    if game.board[start_point[0] + j][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] += 1
        start_point[1] += 1

    start_point = [last[0] + (game.target - 1), last[1] - (game.target - 1)]
    for i in range(game.target):
        if len(game.board) > start_point[0] >= last[0] and 0 <= start_point[1] <= last[1]:
            utility = 0
            if start_point[0] - (game.target - 1) >= 0 and start_point[1] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0] - j][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] -= 1
        start_point[1] += 1

    checked_char = -1
    # Checking consecutive characters with -1 in vertical, horizontal and diagonal manner
    start_point = [last[0] - (game.target - 1), last[1]]
    for i in range(game.target):
        if 0 <= start_point[0] <= last[0]:
            utility = 0
            if start_point[0] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0] + j][start_point[1]] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] += 1

    start_point = [last[0], last[1] - (game.target - 1)]
    for i in range(game.target):
        if 0 <= start_point[1] <= last[1]:
            utility = 0
            if start_point[1] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0]][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[1] += 1

    start_point = [last[0] - (game.target - 1), last[1] - (game.target - 1)]
    for i in range(game.target):
        if 0 <= start_point[0] <= last[0] and 0 <= start_point[1] <= last[1]:
            utility = 0
            if (start_point[0] + (game.target - 1) < len(game.board) and start_point[1] + (game.target - 1) < len(
                    game.board)):
                for j in range(game.target):
                    if game.board[start_point[0] + j][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] += 1
        start_point[1] += 1

    start_point = [last[0] + (game.target - 1), last[1] - (game.target - 1)]
    for i in range(game.target):
        if len(game.board) > start_point[0] >= last[0] and 0 <= start_point[1] <= last[1]:
            utility = 0
            if start_point[0] - (game.target - 1) >= 0 and start_point[1] + (game.target - 1) < len(game.board):
                for j in range(game.target):
                    if game.board[start_point[0] - j][start_point[1] + j] == checked_char:
                        utility += 1
            if utility == game.target and checked_char == char_turn:
                return float('inf')
            if checked_char == char_turn:
                utility -= 1
            if utility > max_util:
                max_util = utility
                factor = 0
            elif utility == max_util:
                factor += 1
        start_point[0] -= 1
        start_point[1] += 1

    return max_util + (factor / config.MARGIN)
