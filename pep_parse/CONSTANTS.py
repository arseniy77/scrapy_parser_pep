import datetime as dt

statuses_filename_format = 'status_summary_%Y-%m-%d_%H-%M-%S.csv'
STATUSES_FILENAME = dt.datetime.now().strftime(statuses_filename_format)
BASE_DIR = 'results'
