#!/usr/bin/python3

from pynotifier import Notification
import requests
import random

randomNumber = 0
quote = ""
def getQuotes():
    link = "https://anime-chan.herokuapp.com/api/quotes?anime=naruto"
    response = requests.get(link)
    quote = response.json()
    randomNumber = random.randint(0, len(quote))
    return quote[randomNumber]["quote"]+ " ~" + quote[randomNumber]["character"]
print("Fetching quote. . .")
Notification(
            title='Quote of the day:',
            description = getQuotes(),
            #icon_path='',
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()

print("Done!")
