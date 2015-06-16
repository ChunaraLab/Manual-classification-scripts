import pymongo, sys, json
from pymongo import MongoClient

###############################################
# Simple DB tagging stats
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
tagField    = json['tweets']['tag']

print 'Total tweets in the DB:', db[collection].count()
tagged = db[collection].find({ tagField: { '$exists' : True, '$nin': [""]} }).count()
print 'Tagged:', tagged
print 'Percentage: {0}%'.format((tagged * 100) / db[collection].count())
positive = db[collection].find({tagField:4}).count()
negative = db[collection].find({tagField:2}).count()
neutral = db[collection].find({tagField:1}).count()
unrelated = db[collection].find({tagField:3}).count()
print 'Positive: {0}, Negative: {1}, Neutral: {2}, Unrelated: {3}'.format(positive, negative, neutral, unrelated)