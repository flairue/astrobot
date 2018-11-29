whine = '''You can just look at your own device, you know.
But I'm a bot, so what do choice do I have. Here it is.'''
'''
def now(message):
    import datetime

    cut = message.replace('whattime', '')
    try:
        tz = int(cut)
    except:
        tz = 0

    time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=tz)))
    return time
'''
from datetime import datetime
import math

def date_to_jd(year, month, day):
    """
    Convert a date to Julian Day.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
    
    Returns
    -------
    jd : float
        Julian Day
        
    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day
    
    >>> date_to_jd(1985,2,17.25)
    2446113.75
    
    """


    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    
    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)
        
    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
        
    D = math.trunc(30.6001 * (monthp + 1))
    
    jd = B + C + D + day + 1720994.5
    
    return jd

def Julian(content):
    date = datetime.now()
    if len(content.split()) == 2:
        try:
            date = datetime.strptime(content.split()[1], "%Y-%m-%d")
        except:
            return "Check your date, maybe?"
    else:
        return "Check your date, maybe?"

    day = date.day + date.hour/24 + date.minute/(24 * 60) + date.second/(24 * 3600)
    jd = date_to_jd(date.year, date.month, day)
    
    return "The JD of the date is {0}. You're welcome.".format(jd)