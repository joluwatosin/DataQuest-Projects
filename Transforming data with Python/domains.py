"""
This looks at What domains were submitted most often to Hacker News
"""
import read
data = read.load_data()

domains = data['url'].value_counts()

#Showing only the top 100 domains
domains = domains[0:100]

#print(domains.loc[0:100])

for name, row in domains.items():
    print("{0}: {1}".format(name, row))