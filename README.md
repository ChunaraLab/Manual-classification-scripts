# Manual Classification

This repository contains python scripts that can be used for manually classifying tweets in a mongodb.

-----------------------

### Config file

You need a `config.json` file in order to run the scripts. It will contain all the parameters characteristic your data, as well as your mongodb setup. 
> Here is a sample configuration:

```json
{
  "mongodb": {
    "host": "localhost",
    "port": 27017
  },
  "db" : {
  	"name": databaseName,
  	"collection": collectionName,
  	"username": yourUsername,
  	"password": yourPassword
	},
  "tweets" : {
    "text": tweetTextKey,
    "author": tweetAuthorKey
  }
}
```
