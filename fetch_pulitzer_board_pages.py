from settings import PAGES_DIR
from os.path import join
import requests
import csv
import json
PULITZER_TAXONOMY_FILENAME = 'pulitzer-taxonomy.csv'
BASE_PULITZER_BOARD_URL = 'http://www.pulitzer.org/cache/api/1/board/year/%s/raw.json'

pulitzer_year_data = list(csv.reader(open(PULITZER_TAXONOMY_FILENAME)))


for year, year_id in pulitzer_year_data:
    url = BASE_PULITZER_BOARD_URL % str(year_id)
    headers = {'Referer': 'http://www.pulitzer.org/'}
    print("Downloading from", url)
    resp = requests.post(url, headers=headers)
    respdata = resp.json()
    fname = join(PAGES_DIR, str(year) + '.json')
    print("...Writing to", fname)
    with open(fname, 'w') as w:
        # just save it as plain ol text for now
        w.write(json.dumps(respdata, indent=2))



