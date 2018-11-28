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

def moonpic(pos):
    p = 0
    if pos > 0.5:
        p = math.pi
    return "https://www.timeanddate.com/scripts/moon.php?i={0}&p={1}".format(pos, p)

#Main function
def Moon(content):
    date = content.replace("moon ", "")

    if date == "":
        return "Sorry, it's not supported yet!"
    else:
        date = None
    
    pos = position(date)
    idx, phname = phase(pos)

    captions = {
        0: "No Moon tonight. Bring out your telescopes!",
        1: "Look at that cute little crescent.",
        2: "Halfway there.",
        3: "She's fat.",
        4: "WATCH OUT FOR WEREWOLVES!",
        5: "She's getting thinner. Is she on diet?",
        6: "She's old but she's happy.",
        7: "It's fading away..."
    }

    pic = moonpic(pos)
    return "It's {0}. {1} \n {2} {3}".format(phname, captions[idx], pic, idx)

poses = [0.01 * i for i in range(100)]
for i in poses:
   print(i, phase(dec(i)))

print(Moon("moon"))