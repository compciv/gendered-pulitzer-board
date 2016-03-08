from os.path import join
import json
WRANGLED_DATA_FILENAME = join('tempdata', 'babynames', 'wrangledbabynames.json')
# boy this is bad practice...but it's fast...
NAMES_DATA_ROWS = json.load(open(WRANGLED_DATA_FILENAME))

def detect_gender(name):
    # prepare an empty result just in case the given name is not found in our database
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        # find first row...
        if name.lower() == row['name'].lower():
            # this should be the match
            result = row
            # since each name only shows up once in our list
            # we can break early rather than iterating through the rest of NAMES_DATA_ROWS
            break
    # if no match was found, result is what it was at the beginning
    return result
