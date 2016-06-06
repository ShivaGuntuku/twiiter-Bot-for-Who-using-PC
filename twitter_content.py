import tweepy
from whoUse import who 

auth = tweepy.OAuthHandler('8h3KjUnCx0hnAzhUYfDUElPVZ','8RfORD2WksfHjpHJ0ouPpgFCT3TBzmjmaX2pSSOZttZGPouYIO')
auth.set_access_token('737677214330720256-87kKS5cd2jOEoZPcBqrG6oaHhnHvM1f','TD6Viw1tW5NnIaYFPG6LD0tHMDCSsYsZuqb3GLrzOQeEh')

api = tweepy.API(auth)
def jarvis_replay():
	s = who()
	#status update with media
	api.update_with_media(filename = s,status = '#fromJarvis')

#jarvis_replay()



