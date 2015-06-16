import pymongo, sys, json
from pymongo import MongoClient

###############################################
# Run as `python mass-tag.py regex tag`
###############################################

# Load config from JSON
with open('config.json') as data_file:
	json = json.load(data_file)

# Connect to DB
client = MongoClient(json['mongodb']['host'], json['mongodb']['port'])
db = client['admin']
db.authenticate(json['db']['username'], json['db']['password'])
db = client[json['db']['name']]
collection  = json['db']['collection']
tweetText   = json['tweets']['text']
tweetAuthor = json['tweets']['author']
tweetID     = json['tweets']['id']

# Not enough arguments
if len(sys.argv) < 3:
	sys.exit('\nRun script as: python mass-tag.py \'regex\' \'tag\'')

# Check how many and give option to stop
regex = sys.argv[1]
newtag = sys.argv[2]
matches = db.hpv.find({'lang':'en', 'newtag': { '$exists': True, '$nin': ["3", "2", "1", "4", 1, 2, 3, 4]}, tweetText: { '$regex': regex } } )

# Exit if no tweets found
if matches.count() == 0:
	sys.exit('No untagged tweets found with that regex')

raw_input('Found {0} untagged tweets with regex {1} (ENTER to set tag:{2} for ALL) '.format(matches.count(), regex, newtag))
# Loop through results to tag
for tweet in matches:
	db.hpv.update({ tweetID:tweet[tweetID]}, {'$set':{ 'newtag':newtag }}, upsert=False, multi=True)
print 'Done! Running query again to check:'
matches = db.hpv.find({'lang':'en', 'newtag': { '$exists': True, '$nin': ["3", "2", "1", "4", 1, 2, 3, 4]}, 't': { '$regex': regex } } )
print 'There are {0} untagged tweets now.'.format(matches.count())
