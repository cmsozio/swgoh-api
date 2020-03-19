import json

def get_player_json_file(allycode):
    player_file = "json/player/" + str(allycode) + "-player.json"
    f = open(player_file, "r")
    json_file = json.loads(f.read())
    f.close()
    return json_file

def get_player_characters(allycode):
    players = []
    player_dict = {}
    player_json = get_player_json_file(allycode)
    player_name = player_json["name"]
    characters = []
    for character in player_json["roster"]:
        characters.append(character["nameKey"])
    player_dict.update({"player": player_name, "characters": characters})
    players.append(player_dict)
    return players

def get_legendary_characters(allycode):
    legendaries = ("GENERALKENOBI", "HANSOLO", "R2D2", "EMPERORPALPATINE", "COMMANDERLUKESKYWALKER", "CHEWBACCA", "PADMEAMIDALA")# Tuple of Legendaries
    player_json = get_player_json_file(allycode)
    legen_characters = []
    for character in player_json["roster"]:
        if character["defId"] in legendaries:
            legen_characters.append(character["nameKey"])
    return legen_characters

