"""
Adapted from Sean B. Palmer's code
By: flairue
"""

import math
from datetime import datetime
from decimal import Decimal
dec = Decimal


def position(now=None):
    if now == None:
        now = datetime.now()

    diff = now - datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)

def phase(pos):
    index = round((pos * dec(8)) + dec("0.5"))
    phasename = {
      0: "New Moon", 
      1: "Waxing Crescent", 
      2: "First Quarter", 
      3: "Waxing Gibbous", 
      4: "Full Moon", 
      5: "Waning Gibbous", 
      6: "Last Quarter", 
      7: "Waning Crescent"
    }
    return index, phasename[int(index) & 7]

def moonpic(i):
    p = 0
    if i > 0.5:
        p = math.pi
    return "https://www.timeanddate.com/scripts/moon.php?i={0}&p={1}".format(i, p)

#Main function
def Moon(content):
    if len(content.split()) == 1:
        date = None
    else:
        date = datetime.strptime(content.split()[1], "%Y-%m-%d")
    
    pos = position(date)
    idx, phname = phase(pos)
    illum = math.sin(pos/dec(0.5) * dec(math.pi/2))

    captions = {
        0: "THAT'S NO MOON!",
        1: "Look at that cute little crescent.",
        2: "Halfway there.",
        3: "She's fat.",
        4: "WATCH OUT FOR WEREWOLVES!",
        5: "She's getting thinner. Is she on diet?",
        6: "She's old but she's happy.",
        7: "It's fading away..."
    }

    pic = moonpic(illum)
    return "It's {0}. {1} \n {2}".format(phname, captions[idx & 7], pic)

print(Moon("moon 2018-11-07"))