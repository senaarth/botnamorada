import tweepy
from random import randint

#Setting Product Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Looking for every tweet with the specific hashtag
mentions = api.search('#BotNamorada')

# Setting a group of phrases to the bot responses
frases = [
    ' Te amo amor...',
    ' Quer namorar comigo?',
    ' Dez reais e eu namoro voce!',
    ' #ENJOADOZ 16/07 LANÇAMENTO DO @ehobrilho',
    ' Mal conheço e já amo...',
    ' Já estou encomendando o vestido!',
    ' Quando será nosso casório?',
    ' Acho que vi um gatinho...',
    ' Chamou amor?', 
]
# Declaring the variable that is going to be in the tweet
frase = ''

# For every mention: choose a random phrase and respond the tweet with the right id from the user 
for mention in mentions:
    frase = frases[randint(0, 8)]
    api.update_status('@' + mention.user.screen_name + frase, mention.id)