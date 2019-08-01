from api_libs.twitterapi import *
import datacollection.datacollection as datacollection

def main():
	loaded_users = datacollection.load_users()
	print("Loaded the following users:")
	print(loaded_users)

	random_users = datacollection.get_random_users(twitter_api, 10)
	print("Generated the following random users:")
	print(random_users)

	searched_users = datacollection.search_users(twitter_api, 10, term='Trump')
	print("Got the following users from searching Trump")
	print(searched_users)

	print("Saving searched users")
	datacollection.save_users(searched_users)	

if __name__ == '__main__':
	main()
