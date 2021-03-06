# Manual Classification

This repository contains python scripts that can be used for manually classifying tweets from a MongoDB.

### Getting Started

* Clone: `git clone https://github.com/ChunaraLab/Manual-classification-scripts.git`
* Create config file (*see below*): `vi config.json`
* Run a script and tag away!

-----------------------

## Config file

You need a `config.json` file in order to run the scripts. It will contain all the parameters of your data (keys, tags, etc.) as well as your mongodb setup. 
> Here is a sample configuration:

```json
{
  "mongodb": {
    "host": "localhost",
    "port": 27017
  },
  "db" : {
  	"name": "myDatabase",
  	"collection": "myCollection",
  	"username": "myUsername",
  	"password": "myPassword"
	},
  "tweets" : {
    "text": "tweetTextKey",
    "author": "tweetAuthorKey"
  }
}
```

## simple-tagging.py

Straightforward manual tagging looping through the tweets.

```bash
python simple-tagging.py
```

## tag-keyword.py

Lets you tag tweets based on a simple keyword search.

```bash
python tag-keyword.py 'searchKeyword'
```

## mass-tag.py

Lets you perform a mass tag on tweets matching a regex. Useful when running into a frequent pattern (such as retweets).

```bash
python mass-tag.py '.*someregex.*' tag
```

## db-stats.py

Simple script to print a few stats about the tagging state of the database.

```bash
python db-stats.py
```

## TO-DO

- [ ] Generalize tags / classes in `config.json` (currently only works with 1,2,3,4 tags)
- [ ] Ability to enter tag without RETURN key (move to next in cursor after inputting only 1 char).