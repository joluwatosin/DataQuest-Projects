"""
Looking at time when the most articles are submitted
"""
import read
from dateutil.parser import parse

data = read.load_data()

def hour_extractor(columns):
    time = parse(columns)
    hour = time.hour
    return hour

data['hour'] = data['submission_time'].apply(hour_extractor)

print(data['hour'].value_counts())
