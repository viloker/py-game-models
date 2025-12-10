import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as data:
        players = json.load(data)
    for player in players:

        player_race = players[player]["race"]

        race = (Race.objects
                .get_or_create(name=player_race["name"],
                               description=player_race["description"]))

        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race[0]
            )

        player_guild = players[player]["guild"]
        if player_guild:
            guild = Guild.objects.get_or_create(
                name=player_guild["name"],
                description=player_guild["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race[0],
            guild=None if guild is None else guild[0]
        )


if __name__ == "__main__":
    main()
