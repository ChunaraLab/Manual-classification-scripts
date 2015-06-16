import pymongo, sys, json
from pymongo import MongoClient

###############################################
# Run as `python tag-keyword.py searchkeyword`
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

# Stop if no keyword arguments
if len(sys.argv) == 1:
	sys.exit('\nRun script as: \'python script.py keyword\' to search DB.')

# Finding tweets based on Regex
keyword = sys.argv[1]
regex = '.*' + keyword + '.*'
matches = db[collection].find({'lang':'en', 'newtag': { '$exists': True, '$nin': ["3", "2", "1", "4", 1, 2, 3, 4]}, tweetText: { '$regex': regex } } )
length = matches.count()

# Exit if no tweets found
if length == 0:
	sys.exit('No tweets found.')
raw_input('Found {1} untagged tweets with keyword \'{0}\' (ENTER to continue) '.format(keyword, length))

print '\nLet\'s start tagging. Enter 0 to STOP. \n'

# Loop through results to tag
for tweet in matches:
	print '\n{0}>> {1}'.format(tweet[tweetAuthor].encode('utf-8'), tweet[tweetText].encode('utf-8'))
	valid_tags = set([1, 2, 3, 4])
	newtag = input('Tag (Positive=4, Negative=2, Neutral=1, Unrelated=3): ')
	if newtag in valid_tags:
		db[collection].update({ tweetID:tweet[tweetID]}, {'$set':{ 'newtag':newtag }}, upsert=False, multi=False)
	else:
		if newtag == 0:
			print '\nAlright, see you later.'
			break
		else:
			print 'Not a valid tag. Press 0 to exit.'
	print ''
print 'Done!'
