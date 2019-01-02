import tweepy as tp
import time 
import os

print('this is my twitter bot')

CONSUMER_KEY = 'jshSDd5N5Q1ZPb4l511vSwtL0'
CONSUMER_SECRET = 'uD6Z5N81O6KFvYOMG81tnHIXAwaFLT4m7gtzeSlbIxz3Av7xNj'
ACCESS_KEY = '22637016-woGjjUDoT29ulE69mn1EkDmg9oCdDvYn7Ux9EZlHU'
ACCESS_SECRET = 'FVCQcITlcVxVSkFYGE00wlngHUehzpUI2RaEzHOXNysq5'


auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# os.chdir('')
# for model_image in os.listdir('.'):
#     api.update_with_media(model_image)
#     time.sleep()