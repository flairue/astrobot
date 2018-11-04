import os
import config
os.environ["NASA_API_KEY"] = config.NASA_API_KEY
#import requests

def getAPOD(message):
    from nasa import apod

    date = message.replace('astropic', '')
    if date == '':
        date = None
    pic = apod.apod(date[1:])
    return pic.url, pic.title, pic.explanation
