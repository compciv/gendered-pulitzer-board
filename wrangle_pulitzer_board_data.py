from settings import PAGES_DIR, WRANGLED_DATA_FILENAME, WRANGLED_DATA_HEADERS
from os.path import join, basename, splitext
from glob import glob
import csv
import json

filenames = glob(join(PAGES_DIR, '*.json'))

datapersons = []
for fn in filenames:
    print("opening", fn)
    data = json.load(open(fn))
    year = splitext(basename(fn))[0]

    for person in data:
        d = {'year': year}
        d['nid'] = person['nid']
        d['first_name'] = person['field_first_name']['und'][0]['safe_value'].strip()
        d['last_name'] = person['field_last_name']['und'][0]['safe_value']
        if person['field_employer']: # apparently this can be empty!
            d['employer'] = person['field_employer']['und'][0]['safe_value']
        d['job_title'] = person['field_job_title']['und'][0]['safe_value']
        datapersons.append(d)


with open(WRANGLED_DATA_FILENAME, 'w') as w:
    dw = csv.DictWriter(w, fieldnames = WRANGLED_DATA_HEADERS)
    dw.writeheader()
    for dp in datapersons:
        dw.writerow(dp)
