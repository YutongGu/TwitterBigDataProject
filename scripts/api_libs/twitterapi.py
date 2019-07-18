import twitter
import json
import sys
import os
import pprint

try:
	with open("api_keys/twitter_api_keys.secret", "r") as f:
		tw_api_keys = json.loads(f.read())
except FileNotFoundError:
	print("ERROR: twitter_api_keys does not exist")
	print("Generating file to input twitter api keys in api_keys/")
	empty_tw_api_keys = {
						"consumer_key":"",
					   	"consumer_secret":"",
					   	"access_token_key":"",
					   	"access_token_secret":""
				  		}
	os.mkdir("api_keys")
	with open("api_keys/twitter_api_keys.secret", "w") as f:
		f.write(json.dumps(empty_tw_api_keys, indent=4))
finally:
	print("Exiting program")
	sys.exit()

twitter_api = twitter.Api(consumer_key = tw_api_keys["consumer_key"],
			      consumer_secret = tw_api_keys["consumer_secret"],
                  access_token_key = tw_api_keys["access_token_key"],
                  access_token_secret = tw_api_keys["access_token_secret"],
                  sleep_on_rate_limit = True)