import db

def get_player_characters(allycode):
    db.check_document("players", {"_id": allycode})
    document = db.query_documents("players", {"_id": allycode, "roster": 1})[0]
    roster = document["roster"]
    character_list = []
    for character in roster:
        character_list.append(character["nameKey"])
    return character_list


"""
def get_legendary_characters(allycode):
    legendaries = ("GENERALKENOBI", "HANSOLO", "R2D2", "EMPERORPALPATINE", "COMMANDERLUKESKYWALKER", "CHEWBACCA", "PADMEAMIDALA")# Tuple of Legendaries
    player_json = get_player_json_file(allycode)
    legen_characters = []
    for character in player_json["roster"]:
        if character["defId"] in legendaries:
            legen_characters.append(character["nameKey"])
    return legen_characters
"""
""" Testing


characters = get_player_characters(413422952)
for character in characters:
    print(character)
"""