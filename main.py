from match import Match
from api import Api
import config


def main():
    game = config.GAME

    if game == "Test":
        agent = Api()
        user = Api('1099', '1320')
        board_size = int(input("Board Size? (Default 3)\nsize: ") or "3")
        target_size = int(input("Target? (Default is 3)\ntarget: ") or "3")

        game = Match(agent, user, size=board_size, target=target_size)
        print(f"Game created! gameId: {game.gameId}")
        game.play()

    elif game == "Test Continue":
        agent = Api()
        user = Api('1099', '1320')
        gameId = input("Game Id?\ngameId: ")
        game = Match(agent, user, gameId=gameId)
        game.play()

    elif game == "Opponent New":
        agent = Api()
        opponent = int(input("Other Team Id?\nteamId: ") or "1320")
        board_size = int(input("Board Size? (Default 3)\nsize: ") or "3")
        target_size = int(input("Target? (Default is 3)\ntarget: ") or "3")
        game = Match(agent, opponent, size=board_size, target=target_size)
        print(f'Game Started with opponent {opponent} with game id {game.gameId}')
        game.play()

    elif game == "Opponent Join":
        agent = Api()
        opponent = int(input("Other Team Id?\nteamId: "))
        gameId = int(input("Game Id?\ngameId: "))
        game = Match(agent, opponent, gameId=gameId)
        print(f'Game Started with opponent {opponent} with game id {game.gameId}')
        game.play(we_start=False)


if __name__ == "__main__":
    main()
