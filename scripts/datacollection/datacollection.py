import twitter
import random
from datetime import datetime
import time
import pickle

def get_valid_users(api = None, num_ids = 0, run_limit = None):
	assert isinstance(api, twitter.Api)
	assert num_ids > 0 and num_ids < 10000
	ids_left_to_gen = num_ids
	ids_list = []
	old_list = []
	users = []

	random.seed(datetime.now())

	while ids_left_to_gen > 0:
		print(api.CheckRateLimit("https://api.twitter.com/1.1/users"))
		if run_limit is not None:
			if run_limit == 0:
				break
			else:
				run_limit -= 1

		for i in range(100):
			user_id = int(random.random() * 2147483647 * 2)
			if user_id in old_list:
				i -= 1
				continue
			else:
				ids_list.append(user_id)

		print("Searching for {} ids".format(100))
		retval = api.UsersLookup(user_id = ids_list, include_entities = False)
		users += retval
		print("Got back {} valid ids".format(len(retval)))
		print("Total valid ids = {}".format(len(users)))

		ids_left_to_gen = num_ids - len(users)
		old_list = ids_list
		ids_list = []

	if len(users) > num_ids:
		print("Got more than we wanted, removing {} users".format(ids_left_to_gen))
		del users[ids_left_to_gen:]

	return users

def save_users(user_list, file_name="user_list"):
	assert isinstance(user_list, list)
	assert len(user_list) > 0 
	assert isinstance(user_list[0], twitter.models.User)

	pickle.dump(user_list, open( "datacollection/storage/{}.db".format(file_name), "wb" ))

def load_users(file_name="user_list"):
	user_list = pickle.load( open( "datacollection/storage/{}.db".format(file_name), "rb" ))

	return user_list