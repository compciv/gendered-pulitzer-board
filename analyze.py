from settings import CLASSIFIED_DATA_FILENAME
from os.path import join
from csv import DictReader


all_members = list(DictReader(open(CLASSIFIED_DATA_FILENAME)))


# people are in the list multiple times
# so create a dictionary based on nid to get a unique list
unique_members = {}
for d in all_members:
    unique_members[d['nid']] = d

genderdict = {'M': [], 'F': [], 'NA': []}
for nid, person in unique_members.items():
    gd = person['gender']
    genderdict[gd].append(person)

print("Since 1968, the estimated gender breakdown for the Pultizer Board membership is:")
print("\tF:", len(genderdict['F']))
print("\tM:", len(genderdict['M']))
fm_ratio = round(100 * len(genderdict['F'])/len(genderdict['M']))
print("\tF/M:", str(fm_ratio) + '%')

print("-----------------------------------------")
print("Now let's do a decade-by-decade breakdown")
# Now let's do this same calculation by decade:
for decade in [1960, 1970, 1980, 1990, 2000, 2010]:
    # because the data came in CSV, the "year" for each member row is still a string
    # so we can still take advantage of it
    decade_members = []
    for member in all_members:
        dyr = member['year'][0:3] + '0' # i.e. "1968" is now "196" + "0"
        if int(dyr) == decade:
            decade_members.append(member)
    # now that decade_members contains all members in a given decade
    # we can repeat the previous rigamrole of getting unique_members
    # and doing genderdict, etc.
    # ...mind that you use decade_members instead of all_members
    unique_members = {}
    for d in decade_members:
        unique_members[d['nid']] = d

    genderdict = {'M': [], 'F': [], 'NA': []}
    for nid, person in unique_members.items():
        gd = person['gender']
        genderdict[gd].append(person)

    print(decade)
    print("\tF:", len(genderdict['F']))
    print("\tM:", len(genderdict['M']))
    fm_ratio = round(100 * len(genderdict['F'])/len(genderdict['M']))
    print("\tF/M:", str(fm_ratio) + '%')
