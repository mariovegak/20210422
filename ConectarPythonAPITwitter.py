# Biblioteca Interface Twitter
import tweepy
# Datos para Authentication
consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
accessToken = 'access Token'
accessTokenSecret = 'access TokenSecret'
# Ingresa al Api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
# Datos para busqueda
keyword ='temblor'
noOfTweet = 10
tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
#imprime resultado de busqueda
print("--------------")
for tweet in tweets:
    print(tweet.text)
    print("--------------")


