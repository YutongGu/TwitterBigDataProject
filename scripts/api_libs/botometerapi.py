import botometer
import json
import son
import sys
import os
import pprint

try
	with open("api_keys/rapid_api_key.secret", "r") as q:
		rapid_api_key = json.loads(q.read())
except FileNotFoundError :
	print("ERROR: rapid_api_key does not exist")
	print("generating file to input rapid api key in api_keys/")
	empty_rapid_api_key = {
						"rapid_api_key" : ""
						}
with open("api_keys/rapid_api_key.secret", "w") as q:
	q.write(json.dumps(empty_rapid_api_key, indent = 4))
print("Exiting program")
sys.exit()

botometer_api = botometer.Api(rapid_api_key = rapid_api_key)
