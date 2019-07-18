import twitter
import json

with open("api_keys/twitter_api_keys.secret") as f:
	tw_api_keys = json.loads(f.read())

tw_api = twitter.Api(consumer_key = tw_api_keys["consumer_key"],
			      consumer_secret = tw_api_keys["consumer_secret"],
                  access_token_key = tw_api_keys["access_token_key"],
                  access_token_secret = tw_api_keys["access_token_secret"],
                  sleep_on_rate_limit = True)