from os.path import join, basename
import json
BABY_DATA_DIR = join('tempdata', 'babynames')
WRANGLED_DATA_FILENAME = join(BABY_DATA_DIR, 'wrangledbabynames.json')
START_YEAR = 1900
END_YEAR = 1981
years = list(range(START_YEAR, END_YEAR, 5))

# namesdict sees all names
namesdict = {}
for year in years:
    # get the file for this particular year
    filename = join(BABY_DATA_DIR, 'yob' + str(year) + '.txt')
    print("Parsing", filename)
    # open that file, read it completely in mydict
    with open(filename, 'r') as thefile:
        for line in thefile:
            name, gender, count = line.split(',')
            if not namesdict.get(name): # need to initialize a dict for this name
                namesdict[name] = {'F': 0, 'M': 0}
            # unlike in past exercises, because we're reading multiple years
            # we will be adding to these dicts more than twice (i.e. M and F, and for every year combo)
            # so mind that += operator
            namesdict[name][gender] += int(count)

# Wait till every year is done
my_awesome_list = []
# just the same as it was for g.py, except no "year"
for name, babiescount in namesdict.items():
    xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
    # finally, add our new dict, xdict, to my_awesome_list
    my_awesome_list.append(xdict)

with open(WRANGLED_DATA_FILENAME, 'w') as j:
    j.write(json.dumps(my_awesome_list, indent=2))


