import random
import datetime

def podshet_lit():
    num = 8
    day_or_night = "ночь"

    if day_or_night == 'день':
        date = datetime.time(7,00)

    else:
        date = datetime.time(19,00)

    print(date.strftime("%H:%M"))

    for i in range(1,num+1):
        date += datetime.timedelta(minutes = 1)
        print(date)

podshet_lit()