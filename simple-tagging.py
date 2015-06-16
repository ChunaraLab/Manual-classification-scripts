import pymongo, sys, json
from pymongo import MongoClient

###############################################
# Run as `python simple-tagging.py`
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
tagField    = json['tweets']['tag']

# Finding tweets based on Regex
matches = db.hpv.find({'lang':'en', tagField: { '$exists': True, '$nin': [1, 2, 3, 4]} }).limit(500)
length = matches.count()

# Exit if no tweets found
if length == 0:
	sys.exit('No tweets found.')

print '\nLet\'s start tagging. Enter 0 to STOP. \n'

# Loop through results to tag
for tweet in matches:
	print '\n{0}>> {1}'.format(tweet[tweetAuthor].encode('utf-8'), tweet[tweetText].encode('utf-8'))
	valid_tags = set([1, 2, 3, 4])
	newtag = input('Tag (Positive=4, Negative=2, Neutral=1, Unrelated=3): ')
	if newtag in valid_tags:
		db.hpv.update({ tweetID:tweet[tweetID]}, {'$set':{ tagField:newtag }}, upsert=False, multi=False)
	else:
		if newtag == 0:
			print '\nAlright, see you later.'
			break
		else:
			print 'Not a valid tag. Press 0 to exit.'
	print ''
print 'Done!'
