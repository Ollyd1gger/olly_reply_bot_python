#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import glob
import random
import os
import re
import urllib2
from time import gmtime, strftime
import time
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from pytz import timezone
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def ogi():
    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN_KEY = keys['access_token_key']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)


    if(api):
        print "connected"

    data = urllib2.urlopen('https://www.exchangerate-api.com/USD/TRY?k='#paste that site's apikey here)
    for line in data: # files are iterable

                a = "Dolar:" + line+" TRY"

                data3 = urllib2.urlopen('https://www.exchangerate-api.com/EUR/TRY?k='#paste that site's apikey here)
                data4 = urllib2.urlopen('https://www.exchangerate-api.com/GBP/TRY?k='#paste that site's apikey here)
    for line3 in data3:
                euro = "Euro:" + line3+" TRY"

    for line4 in data4:
                pound = "Pound:" + line4+" TRY"
                date = strftime("%Y-%m-%d %H:%M:%S")







                abuzer = "%s\n%s\n%s\n%s ///ollybot" % (euro,a,pound,date)
                print abuzer
                img = Image.open("images/ogul.jpg")
                draw = ImageDraw.Draw(img)
#font = ImageFont.truetype(<font-file>, <font-size>)
                font = ImageFont.truetype("ziyvercan.otf", 24)
# draw.text((x, y),"zarbohan",(r,g,b))
                draw.text((300, 220),abuzer + "\n" + a,font=font, fill="green")
                img.save('sample-out1.jpg')
                file = open('sample-out1.jpg', 'rb')
                data = file.read()
                abuzer = api.search("exchange rate")
                for line in abuzer:
                    sn = line.user.screen_name
                    a = line.text
                    print "\n" + "@" +sn + "  " + a
                    r = api.update_with_media(filename="sample-out1.jpg",status="@%s " % sn,in_reply_to_status_id=line.id)
                    print "gonderdim panps"
                    time.sleep(900)




ogi()



