# Instagram-Page-Automator
## $\textcolor{red}{\textsf{DEPRECATED: This project is no longer functional due to changes in Instagram's API.}}$

Automate your instagram meme page using this program! This script takes memes from reddit after every specified time interval and automatically posts it to your instagram meme page! It also credits the redditor who made the meme. You can also customize it to any other subreddit you'd like!

## BEFORE RUNNING:
This program uses the reddit API wrapper for python (PRAW), so make sure you have the PRAW module installed. Look under the PRAW setup heading for more. 
It also uses InstaBot, which is a custom instagram API, so make sure you have that installed as well. Look under the InstaBot setup heading for more.
Also, you will need to have the modules: os, urllib.request, shutil, and PIL, which usually come installed with python. With the latest commit, all posted meme records will be saved in a .csv file on your computer.

## PRAW SETUP:
First of all, install PRAW by typing this into your command line interface:  ``pip install praw``
After installing, you will need to create a reddit app which will allow this API to connect to reddit.
For this, you need to have a reddit account. 

### Creating a reddit app:

On the old reddit website (old.reddit.com), login and then go to Preferences (top right) -> Apps (in the bar on top) -> Create Another App... (scroll down).
Then, name it anything, and for redirect uri, type: http://reddit.com/ , and click create app.
Now, the weird characters right under your app name is client ID, and the weird characters given after "Secret:" is your client secret. Open the python script and put the client ID and client seret values to the variables clientid and clientsecret respectively (line 15 and 16).

Thats all the setup required for PRAW!

## INSTABOT SETUP:
First of all, install InstaBot by typing this into your command line interface: ``pip install instabot``
Once installed, open the python script and change the username and password variables (line 17 and 18) to the username and password of your instagram meme account respectively.

Thats all the setup required for InstaBot!

## .CSV FILE
Download the included .csv file and keep it in the same directory as the script, or create a new one with the name *posted.csv* with atleast one sample record as seen in the posted.csv file included.

## VARIABLE USES:
* *subreddits* is a list containing the subreddits to be browsed. It switches to the next subreddit every post. The current subreddit value is stored in a variable called subreddit. You can add more subreddits to this list.

* *redditor* is the name of the person who made the meme. It is updated everytime a meme is selected.

* *file_type* is used to check whether the meme is a jpg or png. If its a png, it will be converted to jpg. Any other format will be skipped, as it can't be posted.

* *post_limit* is used to specify how many memes you want to post every interval. Its set to two by default.

* *post_cooldown* is used to specify how long you want to wait before posting a new meme (in seconds). Its set to three hours by default.

* *memeskip* is used to skip the first meme as they are announcements in most subreddits. This variable can be set to 0 to prevent skipping.

## NOTE:
This bot is completely safe as the instagram account details are stored locally on your device.


                 
