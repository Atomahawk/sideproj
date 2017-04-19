pip install tweepy
pip install textblob

python3

from textblob import TextBlob

# Demo:

	#Piece of text as blob variable
	wiki = TextBlob("Andrew is tired but has to still do these silly exercises")

	#fragment parts of speech using tags attribute
	wiki.tags

	#tokenize using words attribute
	wiki.words

	# show sentiment polarity on a scale of -1 to 1.
	wiki.sentiment.polarity


consumer_key = XXTdwvfGWYCM2upkMR8I0hT7g
consumer_secret = NFl4ZDWh3DasZKJHK6LQlzFfruCoG1FGZVksTWDWKWIStqlDPu

#access API
access_token = 4444031112-M79vgAu1pEOyNpcRIQHbE4e4554ULUJMt73uIrG
access_token_secret = UFzPmArgox7tjHGhcC7PFMOKrNsxOVdGSzv7hmXim3Vy0

# authentication (login via code)
auth = tweepy.0AuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# with API variable, we can do the commented methods
api = tweepy.API(auth)

	# Create Tweets, Delete TWeets, Find Twitter Words


# Search tweets that contain word "Trump"
# Collect tweets in public_tweets
public_tweets = api.search ('Trump')

for tweet in public_tweets:
	print(tweet.text) #for all twitter text
	analysis = TextBlob(tweet.text)  #store tweet text in "analysis"
	print(analysis.sentiment) #print analysis sentiment polarity
	# (polarity, subjectivity (measure of fact)