import tweepy

auth = tweepy.OAuthHandler('lFhJWDKllzNWWX9oL84cKbfRy', 'rA3t7Qv4JHUAMDmNEqDmTVse6JN1LtPKEHGK1X5xsyHSWx2dKa')
auth.set_access_token('256408868-aFNw3RVCmajKqTNcJLRzSLmaMPXoZ81fFCVYBt2u', 'O0F94bsnYDJYSwJotK0V49dKv9fL5MDXiWUOhMz0CGHNx')

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

#tweeterPost()
	
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text
#api.update_status('tweepy + oauth!')
#print api.me()

#print api.get_status(256408868)
#print api.get_user('shiva_guntuku')
# api.send_direct_message(screen_name= 'shiva7244',text = 'Hai Jarvis')
# print 'success'
#print api.sent_direct_messages(since_id = 'shiva7244')
#print api.follower_ids
#print tweeterPost()
# def twitterTest():
# 	tweets= api.user_timeline(id =737677214330720256, count = 1)
# 	print tweets
# 	tweet = tweets[0]
# 	return tweet.created_at
# 	return tweet.text
# print twitterTest()
#for update Status
#api.update_status('Play Music.')

#tweets of user
# public_tweets = api.user_timeline(id =737677214330720256)
# for tweet in public_tweets:
# 	print tweet.text

#created at
#public_tweets = api.user_timeline(id =737677214330720256)
#tweet = public_tweets[0]
#for tweet in public_tweets:
#print  'status:{0} id:{1} '.format(tweet.text,tweet.id)
#print tweet.created_at
#status_Info = 'status:{0} id:{1} '.format(tweet.text,tweet.id)
