import json
import requests
import time

# A lot of inspration taken from the following users: platzman, shittybill, and MarTrepodi (thanks :D)

class SWGOHAPI():
    # Urls
    base_url = 'https://api.swgoh.help'
    urls = {
        'signin': '/auth/signin',
        'players': '/swgoh/players',
        'guilds': '/swgoh/guilds',
        'roster': '/swgoh/roster',
        'units': '/swgoh/units',
        'zetas': '/swgoh/zetas',
        'squads': '/swgoh/squads',
        'events': '/swgoh/events',
        'campaign': '/swgoh/battles',
        'data': '/swgoh/data'
    }

    #Token Information
    token = ""
    time_left_token = 0

    # Parameters used for future API requests
    parameters = {
        'allycodes': [],
        'language': 'eng_us',
        'enums': True
    }
    
    def __init__(self, credentials):
        # Set up the payload to be sent to the API
        self.payload =  'username=' + credentials['username']                   # Username
        self.payload += '&password=' + credentials['password']                  # Password
        self.payload += '&grant_type=password'                                  # Grant Type of Client
        self.payload += '&client_id=' + credentials['client_id']                # Client ID of api.swgoh.help account
        self.payload += '&client_secret=' + credentials['client_secret']        # Client Secret of swgoh.gg account

        self._get_access_token()

    def _get_access_token(self):
        # Token already exists, no need to get another one
        if self.time_left_token > 0:    
            return self.token
        
        # Formulate the http request
        signin_url = self.base_url + self.urls['signin']
        http_header = {"content-type": "application/x-www-form-urlencoded"}
        endcoded_response = requests.request('POST', signin_url, headers=http_header, data=self.payload, timeout=10)

        # If the request was not excepted return some error message to client
        if endcoded_response.status_code != 200:
            error = 'Login Failed!'
            data = {"status_code": endcoded_response.status_code, "message": error}
            return data

        # Decode response and grab the token to use for further requests to the API
        response = json.loads(endcoded_response.content.decode('utf-8'))
        self.token = "Bearer " + response['access_token']
        self.time_left_token = time.time() + response['expires_in'] - 30
        return self.token

    def _get_api(self, url, parameters):
        self._get_access_token()
        http_header = {"content-type": "application/json", "authorization": self.token}
        encoded_response = requests.request('POST', url, headers=http_header, data=json.dumps(parameters), timeout=10)
        if encoded_response.status_code != 200:
            error = 'Cannot GET ' + url
            data = {"status_code": encoded_response.status_code, "message": error}
            return data
        response = json.loads(encoded_response.content.decode('utf-8'))
        return response

    def get_players(self, ally_codes):
        players_url = self.base_url + self.urls['players']
        self.parameters['allycodes'] = ally_codes
        return self._get_api(players_url, self.parameters)

    def get_guilds(self, ally_codes):
        guilds_url = self.base_url + self.urls['guilds']
        self.parameters['allycodes'] = ally_codes
        return self._get_api(guilds_url, self.parameters)

    def get_roster(self, ally_codes):
        roster_url = self.base_url + self.urls['roster']
        self.parameters['allycodes'] = ally_codes
        return self._get_api(roster_url, self.parameters)

    def get_units(self, ally_codes):
        units_url = self.base_url + self.urls['units']
        self.parameters['allycodes'] = ally_codes
        return self._get_api(units_url, self.parameters)
    
    def get_zetas(self):
        zetas_url = self.base_url + self.urls['zetas']
        parameters = {'structure': False}
        return self._get_api(zetas_url, parameters)
    
    def get_squads(self):
        squads_url = self.base_url + self.urls['squads']
        parameters = {'structure': False}
        return self._get_api(squads_url, parameters)

    def get_events(self):
        events_url = self.base_url + self.urls['events']
        parameters = {'language': 'eng_us', 'enums': True}
        return self._get_api(events_url, parameters)
    
    def get_campaign(self):
        campaign_url = self.base_url + self.urls['campaign']
        parameters = {'language': 'eng_us', 'enums': True}
        return self._get_api(campaign_url, parameters)

if __name__ == '__main__':
    creds = open("credentials.json", "r")
    credentials = json.loads(creds.read())
    api = SWGOHAPI(credentials)
    ally_code =  [413422952, 548343166, 894763269, 422562814] #413-422-95
    #spencer_code = [548343166]
    #cody_code = [894763269]\
    
    f = open("player.json", "w")
    f.write(json.dumps(api.get_players(ally_code), indent=2))
    f.close()
    """
    f = open("guild.json", "w")
    f.write(json.dumps(api.get_guilds(ally_code), indent=2))
    f.close()
    f = open("roster.json", "w")
    f.write(json.dumps(api.get_roster([413422952]), indent=2))
    f.close()
    f = open("units.json", "w")
    f.write(json.dumps(api.get_units([413422952]), indent=2))
    f.close()
    f = open("zetas.json", "w")
    f.write(json.dumps(api.get_zetas(), indent=2))
    f.close()
    f = open("squads.json", "w")
    f.write(json.dumps(api.get_squads(), indent=2))
    f.close()
    f = open("events.json", "w")
    f.write(json.dumps(api.get_events(), indent=2))
    f.close()
    f = open("campaign.json", "w")
    f.write(json.dumps(api.get_campaign(), indent=2))
    f.close()
    """
    