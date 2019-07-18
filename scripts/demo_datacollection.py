from api_libs.twitterapi import *
import datacollection.datacollection as datacollection

def main():
	users = datacollection.get_valid_users(tw_api, 10)
	datacollection.save_users(users)
	
	print("Saved the following users:")
	print(users)
	
	loaded_users = datacollection.load_users()
	
	print("Loaded the following users:")
	print(loaded_users)

if __name__ == '__main__':
	main()
