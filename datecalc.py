whine = '''You can just look at your own device, you know.
But I'm a bot, so what do choice do I have. Here it is.'''

def now(message):
    import datetime

    cut = message.replace('whattime', '')
    try:
        tz = int(cut)
    except:
        tz = 0

    time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=tz)))
    return time
