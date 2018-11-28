from os import environ #import config
#os.environ["NASA_API_KEY"] = NASA_API_KEY
#import requests

api = environ["NASA_API_KEY"]
def getAPOD(message):
    from nasa import apod

    if len(message.split()) == 1:
        date = None
    else:
        date = message.split()[1]

    pic = apod.apod(date)
    return pic.url, pic.title, pic.explanation