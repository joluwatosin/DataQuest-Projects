""" I'll be writing scripts to answer some main questions:

What words appear most often in the headlines?
What domains were submitted most often to Hacker News?
At what times are the most articles submitted?
"""

def load_data():
    import pandas as pd
    data = pd.read_csv('hn_stories.csv')
    data.columns = ['submission_time', 'upvotes', 'url' ,'headline']
    return data
