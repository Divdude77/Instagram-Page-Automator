'''
###################################
#  INSTAGRAM MEME PAGE AUTOMATOR  #
#          BY Divdude77           #
###################################
'''
#############################################
# READ readme.md BEFORE RUNNING THIS SCRIPT #
#############################################

import os
import shutil
import praw
import urllib.request
import csv
from instabot import Bot
from PIL import Image
from datetime import date
from time import sleep

subreddits = ["memes", "dankmemes"]
subreddit = subreddits[0]
redditor = ""
file_type = ""
posted = 0
post_limit = 2
clientid = "ENTER YOUR CLIENT ID HERE"     # Enter your client ID here
clientsecret = "ENTER YOUR CLIENT SECRET HERE"  # Enter your client secret here
username = "ENTER YOUR USERNAME HERE"      # Enter your username here
password = "ENTER YOUR PASSWORD HERE"      # Eter your password here
memeskip = 1
post_cooldown = 10800


# Deleting Config Folder (Folder causes error if not deleted)

try:
    shutil.rmtree("config")
except OSError as error:
    print()

# Creating a Reddit Instance

reddit = praw.Reddit(
    client_id=clientid,
    client_secret=clientsecret,
    user_agent="memeboi"
)

# Initializing the Instabot

bot = Bot()
bot.login(username=username, password=password)     #Logging in to insta account

# Writing Function to Count Difference of Days Between Today and Given Date

def daysdiff(day):
    d1 = [int(i) for i in day.split('-')]
    d2 = [int(i) for i in str(date.today()).split('-')]
    if d1[:2] == d2[:2]:
        return d2[2] - d1[2]
    elif d1[0] == d2[0]:
        if d1[1]<d2[1]:
            return ((30-d1[2]) + d2[2] + 30 * (d2[1]-d1[1]-1))
        
while True:

    # Getting Submitted Memes List

    f = open("posted.csv","r")
    submitted_memes = []
    for i in csv.reader(f):
        submitted_memes.append(i[0])
    f.close()

    # Getting Meme from Reddit

    n = 0
    for submission in reddit.subreddit(subreddit).hot(limit=100):
        if n >= memeskip:
            meme_url = submission.url
            meme_id = submission.id
            file_type = meme_url[-1:-4:-1][-1:0:-1] + "g"
            if file_type == "jpg":
                if submission.id not in submitted_memes:
                    urllib.request.urlretrieve(meme_url, "meme.jpg")  # Download the meme (jpg)
                    redditor = submission.author.name
                    redditor = "u/" + redditor
                    break
                else:
                    continue
            elif file_type == "png":
                if submission.id not in submitted_memes:
                    urllib.request.urlretrieve(meme_url, "meme.png")  # Download the meme (png)
                    mem = Image.open("meme.png")
                    memjpg = mem.convert("RGB")  # Convert it to jpg
                    memjpg.save("meme.jpg")
                    os.remove("meme.png")
                    redditor = submission.author.name
                    redditor = "u/" + redditor
                    break
                else:
                    continue
            else:
                continue
        n += 1

    # Save Posted id Onto File 

    f = open("posted.csv","a")
    csv.writer(f).writerow([submission.id,date.today()])  
    f.close()

    # Create Post Caption

    caption = submission.title + "\n \nPosted in r/" + subreddit + " by " + redditor + "\n \n#meme #memes #funny #dankmemes #memesdaily #funnymemes #lol #follow #humor #like #dank #love #instagram #memepage #dankmeme #tiktok #comedy #lmao #fun #anime #ol #dailymemes #edgymemes #offensivememes #memestagram #bhfyp #instagood #funnymeme #memer #bhfyp"

    # Post Meme on Insta

    try:
        bot.upload_photo("meme.jpg", caption=caption)
    except OSError as error:
        pass

    # Delete Posted Meme

    try:
        os.remove("meme.jpg.REMOVE_ME")
        posted += 1
    except OSError as error:
        os.remove("meme.jpg")

    # Delete old Saved ids

    f = open("posted.csv","r")
    currrentdata = []
    for i in csv.reader(f):
        if daysdiff(i[1]) >= 30:
            continue
        else:
            currrentdata.append(i)
    f.close()
    f = open("posted.csv","w")
    csv.writer(f).writerows(currrentdata)
    f.close()
    
    # Wait for an Hour

    if posted == post_limit:
        print("Post cooldown...")
        sleep(10800)
        posted = 0

    # Switch the Subreddit

    if subreddits.index(subreddit) == len(subreddits) - 1:
        subreddit = subreddits[0]
    else:
        subreddit = subreddits[subreddits.index(subreddit)+1]
