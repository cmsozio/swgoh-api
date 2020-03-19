import discord
import datetime
import json

import swgoh_parser as swgoh

sp = swgoh.SWGOHParser()

allycode_error = 'Error: Ally code must be a number, do not add \'-\' in your ally codes.'

def register(author, content):
    json_file = "json/allycodes.json"
    f = open(json_file, "r")
    try:
        allycodes = json.loads(f.read())
    except:
        allycodes = {}
    f.close()
    try:
        allycodes[str(author)]
        return 'You have already registered your allycode.'
    except:
        f = open(json_file, "w")
        allycodes.update({str(author): content.split()[1]})
        f.write(json.dumps(allycodes, indent=2))
        f.close()
        return 'Added your allycode.'

def legendaries(author, content):
    allycode = content.split()[1]
    if '-' in allycode:
        return allycode_error
    else:
        title = str(author) + " Legendaries"
        color = discord.Colour.from_rgb(84, 121, 128)
        embed = discord.Embed(  title=title, 
                        type="rich",
                        color=color,
                        datetime=datetime.datetime()
                    )
        legends = ""
        for legendary in sp.get_legendary_characters(allycode):
            legends += legendary + "\n"
        embed.add_field(name="Legendaries:", value=legends)
        return embed

def characters(author, content):
    allycode = content.split()[1]
    if '-' in allycode:
        return 