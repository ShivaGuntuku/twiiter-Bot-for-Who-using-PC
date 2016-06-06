import tweepy
from whoUse import who 

auth = tweepy.OAuthHandler('Consumer Key', 'Consumer Secret')
auth.set_access_token('Access Key', 'Access Secret token')
# Access Key,Access Secret token ,consumer key,consumer secret avilable at https://apps.twitter.com/
# After creating the new app in twitter


api = tweepy.API(auth)

def tweeterPost():
	tweets= api.user_timeline(id =737677214330720256,count = 5)
	for tweet in tweets:
		if "#toJarvis" in tweet.text:
			return tweet.text
			break
		else: 
			pass 
	return "no such tweet"

def jarvis_replay():
	s = who()
	#status update with media
	api.update_with_media(filename = s,status = '#fromJarvis')