import os
import config
os.environ["NASA_API_KEY"] = config.NASA_API_KEY
#import requests

def getAPOD(message):
    from nasa import apod

    date = message.replace('apod', '')
    if date == '':
        pic = pic = apod.apod(date=None)
    else:
        pic = apod.apod(date[1:])
    return pic.url, pic.title, pic.explanation
