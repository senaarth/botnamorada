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

FILE_NAME = 'last_seen_id.txt'

# Verify the last tweet responded from the previous usage of the program
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# Register the id of the las tweet responded at the end of the program
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# Looking for every tweet with the specific hashtag that were tweeted after the last seen tweet
last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.search(
                        q = '#BotNamorada',
                        since_id = last_seen_id)
# 1280603158591549440
# 1280610805113815040

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
for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    frase = frases[randint(0, 8)]
    api.update_status('@' + mention.user.screen_name + frase, mention.id)