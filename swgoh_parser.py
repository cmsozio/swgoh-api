import json

import api
import query as q

class SWGOHParser():
    is_setup = 0

    def __init__(self):
        creds_file = open("credentials.json", "r")
        credentials = json.loads(creds_file.read())
        creds_file.close()
        self.swgoh_api = api.SWGOHAPI(credentials)

    def setup(self, allycode):
        if self.is_setup == 0:
            test = self.swgoh_api.get_players(allycode)
            try:
                error = test["message"]
                return error
            except:
                players = self.swgoh_api.get_players(allycode)
                self.json_creater("player", allycode, players)
                guilds = self.swgoh_api.get_guilds(allycode)
                self.json_creater("guilds", allycode, guilds)
                roster = self.swgoh_api.get_roster(allycode)
                self.json_creater("roster", allycode, roster)
                #units = self.swgoh_api.get_units(allycode)
                #zetas = self.swgoh_api.get_zetas()
                #squads = self.swgoh_api.get_squads()
                #events = self.swgoh_api.get_events()
                #campaign = self.swgoh_api.get_campaign()
                self.is_setup = 1
                return 'Ok'
        else:
            pass

    def json_creater(self, directory, allycode, content):
        json_file = "json/" + directory + "/" + str(allycode) + "-" + directory + ".json"
        f = open(json_file, "w")
        f.write(json.dumps(content, indent=2))
        f.close()
   
    def get_player_characters(self, allycodes):
        #response = self._setup(allycodes)
        player_dict = q.get_player_characters(allycodes)
        player_list = []
        for player in player_dict:
            message = player["player"] + "\n"
            player_list.append(message)
        return player_list

    def get_legendary_characters(self, allycode):
        #self._setup(allycode)
        return q.get_legendary_characters(allycode)
        
"""
if __name__ == '__main__':
    swgoh = SWGOHParser()
    #print(swgoh.get_player_characters([894763269, 413422952, 548343166, 422562814]))
    print(swgoh.get_player_characters([413422952]))


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