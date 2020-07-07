import tweepy
from random import randint

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.search('#BotNamorada')

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

frase = ''

print(frase)

for mention in mentions:
    frase = frases[randint(0, 8)]
    print(str(mention.id) + ' - ' + mention.text)
    api.update_status('@' + mention.user.screen_name + frase, mention.id)