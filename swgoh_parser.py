import json

import api
import json_parsing

class SWGOHParser():
    setup = 0

    def __init__(self):
        creds_file = open("credentials.json", "r")
        credentials = json.loads(creds_file.read())
        creds_file.close()
        self.swgoh_api = api.SWGOHAPI(credentials)

    def _setup(self, allycodes):
        if self.setup == 0:
            players = self.swgoh_api.get_players(allycodes)
            #guilds = self.swgoh_api.get_guilds(allycodes)
            #roster = self.swgoh_api.get_roster(allycodes)
            #units = self.swgoh_api.get_units(allycodes)
            #zetas = self.swgoh_api.get_zetas()
            #squads = self.swgoh_api.get_squads()
            #events = self.swgoh_api.get_events()
            #campaign = self.swgoh_api.get_campaign()

            for player in players:
                json_file = "json/player/" + str(player["allyCode"]) + "-player.json"
                f = open(json_file, "w")
                f.write(json.dumps(player, indent=2))
                f.close()

            self.setup = 1
        else:
            pass
   
    def get_player_characters(self, allycodes):
        self._setup(allycodes)
        player_dict = json_parsing.get_player_characters(allycodes)
        player_list = []
        for player in player_dict:
            message = f'{player["player"]}\n'
            player_list.append(message)
        return player_list
        

if __name__ == '__main__':
    swgoh = SWGOHParser()
    print(swgoh.get_player_characters([894763269, 413422952, 548343166, 422562814]))

"""
creds = open("credentials.json", "r")
credentials = json.loads(creds.read())
swgoh = api.SWGOHAPI(credentials)

allycode = [413422952]
player_json = json.loads(json.dumps(swgoh.get_players(allycode)[0]))
print(f'Player Name: {player_json["name"]}')
print(f'Player lvl: {player_json["level"]}')

f = open("temp.txt", "w")
f.write('')
f.close()
for character in player_json['roster']:
    f = open("temp.txt", "a")
    f.write(character['nameKey'])
    f.close()
"""