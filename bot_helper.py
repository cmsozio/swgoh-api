def grab_allycodes(content):
    content = content.split()
    content.pop(0)
    allycodes = []
    for allycode in content:
        if '-' in allycode:
            return f'Ally code must be a number, do not add \'-\' in your ally codes.'
            