import os

help = '''
{0}help will send show you, well, this message.

{0}astropic [optional: YYYY-MM-DD] will show you an NASA/APOD entry of the date.

{0}moon to fetch Moon's current phase. Currently only supports today's phase. 

{0}wiki [article title] to get you the link to the article. Don't mistype!

This bot was created by Naufal (flairue).

>>> Dibuat dalam rangka menunaikan tugas komunas.
'''.format(os.environ['COMMANDPREF'])

#{0}whattime will tell you current UTC time. Use +-[your timezone] to convert the UTC time to your timezone.