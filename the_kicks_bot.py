import tweepy as tp
import time 
import os

print('this is my twitter bot')

CONSUMER_KEY = 'jshSDd5N5Q1ZPb4l511vSwtL0'
CONSUMER_SECRET = 'uD6Z5N81O6KFvYOMG81tnHIXAwaFLT4m7gtzeSlbIxz3Av7xNj'
ACCESS_KEY = '22637016-woGjjUDoT29ulE69mn1EkDmg9oCdDvYn7Ux9EZlHU'
ACCESS_SECRET = 'FVCQcITlcVxVSkFYGE00wlngHUehzpUI2RaEzHOXNysq5'


auth = tp.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)


mentions = api.mentions_timeline()
for mention in mentions:
    print(str(mention.id) + ' - ' + mention.text)
    if '#helloworld' in mention.text.lower():
        print('found hello world dawgggg')
        print('responding back')
        api.update_status('@' + mention.user.screen_name + '#helloworld back at you', mention.id)

# os.chdir('')
# for model_image in os.listdir('.'):
#     api.update_with_media(model_image)
#     time.sleep()