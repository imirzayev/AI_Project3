from api import Api
import time
from adversarial import minimax
from tictactoe import TicTacToe


def show_board(agent, gameId):
    """Displaying the current state of the board"""

    rows = agent.get_board_string(gameId)['output'].split("\n")
    for row in rows:
        if row != '':
            game_row = "|"
            for c in row:
                game_row = game_row + c + '|'
            print(game_row)
        else:
            continue


class Match:
    def __init__(self, agent, opponent, size=3, target=3, gameId=None) -> None:
        self.agent = agent
        self.opponent = opponent
        self.game_states = {'-1': 'Continues', '0': 'Agent Win', '1': 'Opponent Win', '2': 'Draw'}

        # Game does not exists, create one
        if not gameId:
            if isinstance(opponent, Api):
                # Creating game for test match
                print("Test Match")
                self.test_match = True
                self.gameId = self.agent.create_a_game(opponent.team_id, size, target)
            else:
                # Create a Game with opponent
                self.test_match = False
                self.gameId = self.agent.create_a_game(opponent, size, target)

            # Getting the board information
            self.size, self.target = size, target

        # Game exists
        else:
            # Test match for existing game
            if isinstance(opponent, Api):
                print("Test Match for Existing Game")
                self.test_match = True
            else:
                # Match with opponent for existing game
                self.test_match = False

            # Get board information and game ID
            self.size, self.target = self.get_board_info(gameId)
            self.gameId = gameId

        # Initialize the tictactoe board
        self.board = TicTacToe(self.size, self.target)

    def get_board_info(self, gameId):
        """Getting size and target information about the current already started game"""

        board = self.agent.get_board_string(gameId)

        size = len(board['output'].split("\n")[0])
        target = int(board['target'])
        return size, target

    def get_agent_input(self):
        """The input from adversarial search agent"""

        move = minimax(self.board, 1, True)[1]
        made_move = False
        while not made_move:

            move_response = dict(self.agent.make_move(self.gameId, move))

            if move_response["code"] == "OK":
                made_move = True
                return move
            else:
                continue

        return move

    def get_opponent_input(self, we_start):
        """The function that checks whether it is the opponents turn and gets the move from it"""

        last_move = dict(self.agent.get_moves(self.gameId, 1))

        # The game just started
        if last_move["code"] == "FAIL":
            if last_move["message"] == "No moves" and we_start:
                # It it our turn
                print("Our agent made first move")
                return True
            elif last_move["message"] == "No moves" and not we_start:
                # It is opponents turn
                print("Opponent has made first move")
                return False

        # Check whether last moving team is updated
        elif last_move["moves"][0]["teamId"] == self.agent.team_id:
            print("Waiting for opponents move.")
            return False

        # Opponent made a move
        else:
            return True

    def play(self, we_start=True):
        """Main function responsible for interchangable play of agent and opponent"""

        if we_start:
            turn = 0
        else:
            turn = 1

        game_state = -1

        while game_state == -1:

            if self.test_match:
                show_board(self.agent, self.gameId)

                if turn == 0:
                    move = self.get_agent_input()
                    print(f'Agent moved {move}')

                    turn = not turn
                    self.board.mark_coordinate(move, 1)
                    game_state = self.board.win_check(move)[1]
                else:
                    move = self.get_move_user()
                    print(f'Manual input moved {move}')

                    turn = not turn
                    self.board.mark_coordinate(move, -1)
                    game_state = self.board.win_check(move)[1]

                print("Game: ", self.game_states[str(game_state)])
            else:
                if self.get_opponent_input(we_start=we_start):
                    move_response = dict(self.agent.get_moves(self.gameId, 1))

                    if move_response["code"] != "FAIL":
                        move = (int(move_response["moves"][0]["move"].split(',')[0]),
                                int(move_response["moves"][0]["move"].split(',')[1]))

                        self.board.mark_coordinate(move, -1)

                        game_state = self.board.win_check(move)[1]
                        show_board(self.agent, self.gameId)
                        print(f"Game State after Opponents Move: {self.game_states[str(game_state)]}\n")

                        # If game is win/lose/draw
                        if game_state != -1:
                            break

                    # Our Turn
                    print("Our agent playing")

                    move = self.get_agent_input()
                    self.board.mark_coordinate(move, 1)
                    game_state = self.board.win_check(move)[1]

                    show_board(self.agent, self.gameId)
                    print(f"Game State after our Move: {self.game_states[str(game_state)]}\n")
                else:
                    # Wait a little before following API call
                    time.sleep(5)
                    continue

        print(f"GAME OVER! game_state: {self.game_states[str(game_state)]}\n")
        show_board(self.agent, self.gameId)
