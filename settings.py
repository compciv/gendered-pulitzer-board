from os.path import join
from os import makedirs

DATA_DIR = 'tempdata'
PAGES_DIR = join(DATA_DIR, 'pages')
makedirs(PAGES_DIR, exist_ok=True)

WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled_data.csv')
WRANGLED_DATA_HEADERS = ['year', 'nid', 'first_name', 'last_name', 'job_title', 'employer']

CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_data.csv')

