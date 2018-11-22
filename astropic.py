import os
import config
os.environ["NASA_API_KEY"] = config.NASA_API_KEY
#import requests

def getAPOD(message):
    from nasa import apod

    if len(message.split()) == 1:
        date = None
    else:
        date = message.split()[1]

    pic = apod.apod(date)
    return pic.url, pic.title, pic.explanation

print(str('hello world noice'.split()[1:]))
