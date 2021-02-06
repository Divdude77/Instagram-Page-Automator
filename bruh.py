from time import sleep
import os
import shutil
import praw
import urllib.request
from instabot import Bot
from PIL import Image

subreddit = "memes"
redditor = ""
file_type = ""
submitted_memes = []
posted = 0
post_limit = 2
clientid = "bIrkuHmRWfmg1g"
clientsecret = "QrgQHUG5yhbsIVa2HJDqlCrE2_OsAg"
username = "ENTER YOUR USERNAME HERE"      # Enter your username here
password = "ENTER YOUR PASSWORD HERE"      # Eter your password here
memeskip = 3
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

while True:

    # Getting Meme from Reddit

    n = 1
    for submission in reddit.subreddit(subreddit).hot(limit=100):
        n += 1
        if n > memeskip:
            meme_url = submission.url
            meme_id = submission.id
            file_type = meme_url[-1:-4:-1][-1:0:-1] + "g"
            if file_type == "jpg":
                if submission.id not in submitted_memes:
                    urllib.request.urlretrieve(meme_url, "meme.jpg")        # Download the meme (jpg)
                    redditor = submission.author.name
                    redditor = "u/" + redditor
                    break
                else:
                    continue
            elif file_type == "png":
                if submission.id not in submitted_memes:
                    urllib.request.urlretrieve(meme_url, "meme.png")        # Download the meme (png)
                    mem = Image.open("meme.png")
                    memjpg = mem.convert("RGB")                             # Convert it to jpg
                    memjpg.save("meme.jpg")
                    os.remove("meme.png")
                    redditor = submission.author.name
                    redditor = "u/" + redditor
                    break
                else:
                    continue
            else:
                continue
    submitted_memes.append(submission.id)
    caption = submission.title + "\n \nPosted in r/" + subreddit + " by " + redditor

    # Post Meme on Insta

    bot.upload_photo("meme.jpg", caption=caption)
    try:
        os.remove("meme.jpg.REMOVE_ME")
        posted += 1
    except OSError as error:
        os.remove("meme.jpg")

    # Wait for an Hour

    if posted == post_limit:
        print("Post cooldown...")
        sleep(post_cooldown)
        posted = 0

    # Switch the Subreddit

    if subreddit == "memes":
        subreddit = "dankmemes"
        memeskip = 0
    elif subreddit == "dankmemes":
        subreddit = "memes"
        memeskip = 3
