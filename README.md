# Manual Classification

This repository contains python scripts that can be used for manually classifying tweets from a MongoDB.

-----------------------

### Config file

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
