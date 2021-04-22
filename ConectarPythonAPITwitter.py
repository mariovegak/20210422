# Import del Package Twitter
import tweepy
# Datos para Authentication
consumer_key = 'AGREGAR consumer_key'
consumer_secret = 'AGREGAR consumer_secret'
accessToken = 'AGREGAR accessToken'
accessTokenSecret = 'AGREGAR accessTokenSecret'
# Ingreso al Api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
# Datos para busqueda
keyword ='temblor'
noOfTweet = 50
# Abro cursor
tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
#imprime resultado de busqueda
print("--------------")
for tweet in tweets:
    if "Chile" in tweet.user.location:
        print(tweet.user.screen_name)
        print(tweet.user.location)
        print(tweet.created_at)
        print(tweet.text)
        print("--------------")


