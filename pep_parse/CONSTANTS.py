import datetime as dt

peps_filename_format = 'results/pep_%Y-%m-%dT%H-%M-%S.csv'
statuses_filename_format = 'results/status_summary_%Y-%m-%d_%H-%M-%S.csv'

PEPS_FILENAME = dt.datetime.now().strftime(peps_filename_format)
STATUSES_FILENAME = dt.datetime.now().strftime(statuses_filename_format)
