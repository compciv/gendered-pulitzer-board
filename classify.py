from settings import WRANGLED_DATA_FILENAME, CLASSIFIED_DATA_FILENAME
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender

CLASSIFIED_DATA_HEADERS = ['year', 'nid', 'first_name', 'last_name', 'gender', 'job_title', 'employer',
                            'usable_name', 'ratio']

def get_usable_name(namestr):
    """
    `namestr` is something like "William B"
    this function splits namestr by whitespace and returns
      the first element, i.e. "William"
    """
    return namestr.split(' ')[0]

# Set up the new data file
w = open(CLASSIFIED_DATA_FILENAME, 'w')
dw = DictWriter(w, fieldnames=CLASSIFIED_DATA_HEADERS)
dw.writeheader()

# Open the non-gender classified data file
with open(WRANGLED_DATA_FILENAME) as r:
    datarows = list(DictReader(r))
    # read each row
    ct = 0
    for row in datarows:
        usablename = get_usable_name(row['first_name'])
        ct += 1
        print("Row:", ct, "extracting --", usablename, "-- from:", row['first_name'])
        gender_result = detect_gender(usablename)
        # now add usable_name and gender data to each row
        row['usable_name'] = usablename
        row['gender'] = gender_result['gender']
        row['ratio'] = gender_result['ratio']
        dw.writerow(row)
