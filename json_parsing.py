import json

def get_player_characters(allycodes):
    players = []
    for allycode in allycodes:
        player_dict = {}
        player_file = "json/player/" + str(allycode) + "-player.json"
        f = open(player_file)
        player_json = json.loads(f.read())
        player_name = player_json["name"]
        characters = []
        for character in player_json["roster"]:
            characters.append(character["nameKey"])
        player_dict.update({"player": player_name, "characters": characters})
        players.append(player_dict)
    return players
