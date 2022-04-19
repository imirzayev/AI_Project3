import config
import requests


class Api:
    def __init__(self, user_id=config.USER_ID, team_id=config.TEAM_ID, api_key=config.API_KEY) -> None:
        self.user_id = user_id
        self.api_key = api_key
        self.team_id = team_id

    def create_team(self, name):
        """Creating a team"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'name': name,
            'type': 'team'
        }

        response = requests.post(config.API_INDEX, headers=headers, data=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def add_member_to_team(self, teamId, userId):
        """Adding a member to the team"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'member',
            'teamId': teamId,
            'userId': userId
        }

        response = requests.post(config.API_INDEX, headers=headers, data=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def remove_member_from_team(self, teamId, userId):
        """Removing a member from the team"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'removeMember',
            'teamId': teamId,
            'userId': userId
        }

        response = requests.post(config.API_INDEX, headers=headers, data=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def get_team_members(self, teamId):
        """Getting the members of the team"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'team',
            'teamId': teamId
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def get_my_teams(self):
        """Getting teams of the user"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'myTeams'
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def get_my_games(self):
        """Getting the games of the current user"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'myGames'
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def create_a_game(self, team2, size=3, target=3):
        """Creating a game to play"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'game',
            'teamId1': self.team_id,
            'teamId2': team2,
            'gameType': 'TTT',
            'boardSize': size,
            'target': target

        }

        response = requests.post(config.API_INDEX, headers=headers, data=data)

        if response.ok:
            # print(response.json())
            return response.json()['gameId']
        else:
            print("Error: ", response.text)

    def get_my_open_games(self):
        """Getting the open games of the user"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'myOpenGames'
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def make_move(self, gameId, move):
        """Making given move on the game"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'move',
            'gameId': str(gameId),
            'teamId': str(self.team_id),
            'move': f'{move[0]}, {move[1]}'

        }

        response = requests.post(config.API_INDEX, headers=headers, data=data)

        if response.ok:
            # print(response.json())
            # print(f'Making move in game {gameId} by {self.team_id}')
            return response.json()
        else:
            print("Error: ", response.text)

    def get_moves(self, gameId, count=1):
        """Getting lates moves"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'moves',
            'gameId': gameId,
            'count': count
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def get_board_string(self, gameId):
        """Getting the board string"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'boardString',
            'gameId': gameId
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)

    def get_board_map(self, gameId):
        """Getting the board map"""

        headers = {
            "User-Agent": config.USER_AGENT,
            'x-api-key': self.api_key,
            'userId': self.user_id
        }

        data = {
            'type': 'boardMap',
            'gameId': gameId
        }

        response = requests.get(config.API_INDEX, headers=headers, params=data)

        if response.ok:
            # print(response.json())
            return response.json()
        else:
            print("Error: ", response.text)


if __name__ == '__main__':
    api = Api('1099', '1320')
    api.make_move(3550, (1, 1))
    api.get_board_string(3550)
    api.get_moves(1319)
