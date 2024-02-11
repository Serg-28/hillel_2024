class Player:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


for player in team:
    print(player)

print("\n")


def dedup(collection):
    players_names = set()

    for team_player in collection:
        if team_player.first_name not in players_names:
            yield team_player
            players_names.add(player.first_name)


for player in dedup(team):
    print(player)
